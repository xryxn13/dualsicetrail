import streamlit as st
from PIL import Image

def main():
    st.title("GIF Viewer")

    # Display the GIF files and stop at the last frame
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        gif_frames = Image.open(gif_path)
        
        # Display each frame of the GIF
        for frame in ImageSequence.Iterator(gif_frames):
            st.image(frame, use_column_width=True)
            st.write(f"Video {i}")
            st.write("---")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")

if __name__ == "__main__":
    main()
