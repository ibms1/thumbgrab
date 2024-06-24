import streamlit as st
from pytube import YouTube
from PIL import Image
import requests
from io import BytesIO

# Function to fetch the thumbnail
def fetch_thumbnail(url):
    try:
        # Download video information
        yt = YouTube(url)

        # Download the thumbnail
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)
        thumbnail_image = Image.open(BytesIO(response.content))

        return thumbnail_image, yt.title
    except Exception as e:
        st.error(f"Please Try Again Later")
        return None, None

# Streamlit interface
st.title("YouTube Thumbnail Grabber")

# Input field for video URL
video_url = st.text_input("Enter YouTube video URL:")

if st.button("Grab  Thumbnail"):
    if video_url:
        thumbnail, title = fetch_thumbnail(video_url)
        if thumbnail:
            st.image(thumbnail, caption=f'Thumbnail for: {title}')
    else:
        st.error("Please enter a video URL.")

# CSS مخصص لإخفاء الروابط عند تمرير الفأرة
hide_links_style = """
    <style>
    a {
        text-decoration: none;
        color: inherit;
        pointer-events: none;
    }
    a:hover {
        text-decoration: none;
        color: inherit;
        cursor: default;
    }
    </style>
    """
st.markdown(hide_links_style, unsafe_allow_html=True)