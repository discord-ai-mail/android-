import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def fetch_images(query, num_images=5):
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all("img")
        img_urls = [img["src"] for img in img_tags if "src" in img][:num_images]
        return img_urls
    else:
        return []

st.title("🔍 Image Fetcher from Web")
query = st.text_input("Enter search query:")
num_images = st.slider("Number of images:", 1, 10, 5)

if st.button("Fetch Images") and query:
    st.write(f"Fetching {num_images} images for: {query}")
    image_urls = fetch_images(query, num_images)
    
    if image_urls:
        for img_url in image_urls:
            response = requests.get(img_url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                st.image(img, caption=query, use_column_width=True)
    else:
        st.error("No images found. Try a different query!")
      
