import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files in separate columns
    st.write("Videos")
    with st.columns(5):
        for i in range(1, 6):
            gif_path = f"{i}.gif"
            st.image(gif_path, caption=f"Video {i}", use_column_width=True)

if __name__ == "__main__":
    main()
