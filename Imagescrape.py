import streamlit as st
import os
import requests
from serpapi import GoogleSearch

# Streamlit UI
def main():
    st.title("Google Image Scraper")
    
    # User inputs
    search_query = st.text_input("Enter search term:")
    num_images = st.slider("Number of images:", 1, 50, (5))
    folder_path = st.text_input("Enter folder path to save images:", "downloads/")
    scrape_button = st.button("Scrape Images")
    
    if scrape_button:
        if not search_query.strip():
            st.error("Please enter a search term.")
            return
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        st.info("Scraping images... Please wait.")
        scrape_images(search_query, num_images, folder_path)

# Image Scraper Function
def scrape_images(query, num_images, folder):
    params = {
        "q": query,
        "tbm": "isch",
        "api_key": "817b28b53cc1f4911ccda7123cba5359947c36f5e7ae56016706689e86d7b10a"
    }
    search = GoogleSearch(params)
    results = search.get()
    images = results.get("images_results", [])
    
    count = 0
    for img in images[:num_images]:
        img_url = img.get("original")
        if img_url:
            save_image(img_url, folder, count)
            count += 1
    
    st.success(f"Downloaded {count} images to {folder}")

# Save Image Function
def save_image(url, folder, index):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(folder, f"image_{index}.jpg")
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        st.image(file_path, caption=f"Downloaded {index+1}")
    else:
        st.warning(f"Failed to download image {index+1}")

if __name__ == "__main__":
    main()
