import streamlit as st
from IPython.display import display, HTML

def main():
    st.title("GIF Viewer")

    # Display the GIF files
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        html = f'<img src="{gif_path}" width="300">'
        display(HTML(html))
        st.write(f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
