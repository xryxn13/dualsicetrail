import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files using HTML
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        st.markdown(f'<img src="{gif_path}" width="300">', unsafe_allow_html=True)
        st.write(f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
