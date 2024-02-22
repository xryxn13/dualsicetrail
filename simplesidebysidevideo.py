import streamlit as st
from PIL import Image

def main():
    st.title("GIF Viewer")

    # Display the first frame of each GIF
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        first_frame = Image.open(gif_path)
        st.image(first_frame, use_column_width=True, caption=f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
