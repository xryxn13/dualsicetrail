import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files in a row
    for i in range(1, 6):
        st.image(f"{i}.gif", caption=f"Video {i}", use_column_width=True)

if __name__ == "__main__":
    main()
