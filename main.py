import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tracker import extract_price, save_price, get_product_id
from plotter import plot_price_history
from emailer import send_email
import pandas as pd

def main():
    url = input("Enter Amazon product URL: ").strip()
    email = input("Enter your email: ").strip()

    product_id = get_product_id(url)

    # Setup headless Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        price = extract_price(driver, url)
        print(f"Current price: ₹{price}")
        save_price(product_id, price)
        plot_price_history(product_id)

        df = pd.read_csv(f"prices/{product_id}.csv")
        mean_price = df["price"].mean()

        if price < mean_price:
            send_email(email, "Amazon Price Alert",
                       f"The price for {product_id} dropped to ₹{price} below the mean of ₹{mean_price:.2f}")
            print("Email sent!")

    finally:
        driver.quit()

if __name__ == "__main__":
    os.makedirs("prices", exist_ok=True)
    main()