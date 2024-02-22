import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files as videos
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        st.video(gif_path, format='video/gif')
        st.write(f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
