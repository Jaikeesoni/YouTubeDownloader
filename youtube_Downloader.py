import streamlit as st
from pytube import YouTube
import os

# Function to download YouTube video
def download_video(url, resolution, download_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()
        stream.download(output_path=download_path)
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit UI
def main():
    st.title("YouTube Downloader")

    # Input URL
    url = st.text_input("Enter YouTube video URL:", "")

    # Quality/Resolution selection
    resolution_options = ["360p", "720p", "1080p"]
    resolution = st.selectbox("Select resolution:", resolution_options)

    # Download path selection
    download_path = st.text_input("Enter download path:", "")

    # Download button
    if st.button("Download"):
        if url == "":
            st.warning("Please enter a valid YouTube video URL.")
        elif download_path == "":
            st.warning("Please enter a download path.")
        elif not os.path.isdir(download_path):
            st.error("Invalid download path. Please enter a valid directory path.")
        else:
            download_video(url, resolution, download_path)

if __name__ == "__main__":
    main()
