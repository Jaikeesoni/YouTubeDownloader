import streamlit as st
import youtube_dl

# Create a Streamlit app
st.title("YouTube Video Downloader")

# Create a text input for the video URL
video_url = st.text_input("Enter the YouTube video URL")

# Create a dropdown menu for the download path
download_path = st.selectbox("Select a download path", ["Downloads", "Desktop", "Documents"])

# Create a button to trigger the download
if st.button("Download Video"):
    # Use youtube-dl to download the video
    ydl_opts = {'outtmpl': f"{download_path}/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Display a success message
    st.success("Video downloaded successfully!")
