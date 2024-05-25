import streamlit as st
from pytube import YouTube

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
            try:
                yt = YouTube(url)
                st.write(f"Title: {yt.title}")
                st.write(f"Author: {yt.author}")
                st.write(f"Length: {yt.length} seconds")
                st.write(f"Rating: {yt.rating}")
                st.write("Available Formats:")
                for stream in yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution'):
                    st.write(f"- {stream.resolution} ({stream.mime_type})")
                    if st.button(f"Download {stream.resolution}"):
                        stream.download()
                        st.success("Download completed successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
