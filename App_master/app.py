import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Gurgaon Real Estate Price Prediction App",
    page_icon="🏠",
    layout="wide"
)

# Main title
st.title("🏡 Gurgaon Real Estate Price Analysis")

# Load and display the image
import os

image_path = os.path.join(os.path.dirname(__file__), "image.jpg")
image = Image.open(image_path)

st.image(image, caption="Real Estate Deal in Action 🏘️", width=400, use_container_width=False)

# Welcome section
st.markdown("---")
st.markdown("""
## 👋 Welcome to the Gurgaon Property Insights Dashboard

This app empowers you to:
- 📈 Analyze real estate Price trends across Gurgaon
- 🏢 Explore property features like size, location, and amenities
- 📊 Visualize data for better investment decisions
""")

# Highlight box
st.success("🔍 Start exploring by selecting a page from the sidebar!")

