import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_products(url, output_file="products.csv"):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    products = []
    for item in soup.select(".product-item"):
        product = {
            "name": item.select_one(".product-title").text.strip(),
            "price": item.select_one(".product-price").text.strip(),
            "rating": item.select_one(".product-rating").text.strip(),
            "scraped_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        products.append(product)
    
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)
    
    print(f"✅ Scraped {len(products)} products → saved to {output_file}")
    return products

# Example usage
scrape_products("https://example.com/products")