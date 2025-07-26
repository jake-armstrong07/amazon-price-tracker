from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from urllib.parse import urlparse, parse_qs
import os

def extract_price(driver, url):
    driver.get(url)
    time.sleep(3)
    try:
        price = driver.find_element("id", "priceblock_ourprice").text
    except:
        price = driver.find_element("id", "priceblock_dealprice").text
    return float(price.replace("₹", "").replace(",", "").strip())

def get_product_id(url):
    return url.split("/dp/")[1].split("/")[0]

def save_price(product_id, price):
    path = f"prices/{product_id}.csv"
    df = pd.read_csv(path) if os.path.exists(path) else pd.DataFrame(columns=["timestamp", "price"])
    df.loc[len(df)] = [pd.Timestamp.now(), price]
    df.to_csv(path, index=False)