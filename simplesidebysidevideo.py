import streamlit as st
from PIL import Image, ImageSequence

def main():
    st.title("GIF Viewer")

    # Display the GIF files and stop at the last frame
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        gif_frames = Image.open(gif_path)
        
        # Extract frames from the GIF
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif_frames)]

        # Display each frame of the GIF
        for frame in frames[:-1]:  # Exclude the last frame
            st.image(frame, use_column_width=True)

        # Display the last frame separately
        st.image(frames[-1], use_column_width=True)
        st.write(f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
