import streamlit as st
from pytube import YouTube
import os

# Function to download YouTube video
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download()
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit UI
def main():
    st.title("YouTube Video Downloader")

    # Input URL
    url = st.text_input("Enter YouTube video URL:", "")

    # Download button
    if st.button("Download"):
        if url == "":
            st.warning("Please enter a valid YouTube video URL.")
        else:
            download_video(url)

if __name__ == "__main__":
    main()
