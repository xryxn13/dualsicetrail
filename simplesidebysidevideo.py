import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        st.image(gif_path, use_column_width=True)
        st.write(f"Video {i}")
        st.write("---")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")

if __name__ == "__main__":
    main()
