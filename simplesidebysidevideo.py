import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files in a column
    for i in range(1, 6):
        gif_path = f"{i}.gif"
        st.image(gif_path, use_column_width=True, caption=f"Video {i}", format='GIF')

if __name__ == "__main__":
    main()
