import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
from io import BytesIO

# Function to scrape images from Pinterest
def scrape_pinterest_images(query, num_images=10):
    search_url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    image_tags = soup.find_all("img", limit=num_images)
    
    image_urls = [img["src"] for img in image_tags if "src" in img.attrs]
    
    return image_urls

# Streamlit UI
st.title("Pinterest Image Scraper")

query = st.text_input("Enter a search term:", "Travel destinations")
num_images = st.slider("Number of images", 5, 20, 10)

if st.button("Scrape Images"):
    with st.spinner("Scraping images..."):
        image_urls = scrape_pinterest_images(query, num_images)

    if image_urls:
        st.success(f"Found {len(image_urls)} images!")
        for idx, img_url in enumerate(image_urls):
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption=f"Image {idx+1}")
    else:
        st.error("No images found!")

