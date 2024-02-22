import streamlit as st
from PIL import Image

def main():
    st.title("GIF Viewer")

    # Display the GIF files and stop at the last frame
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        st.image(gif_path, use_column_width=True)

        # Open the GIF file using PIL
        with Image.open(gif_path) as img:
            # Get the last frame of the GIF
            img.seek(img.n_frames - 1)
            # Convert the last frame to a static image
            last_frame_img = img.convert("RGB")
            # Display the last frame as a static image
            st.image(last_frame_img, use_column_width=True)

if __name__ == "__main__":
    main()
