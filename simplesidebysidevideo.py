import streamlit as st

def main():
    st.title("GIF Viewer")

    # Display the GIF files side by side
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image("1.gif", use_column_width=True)
    with col2:
        st.image("2.gif", use_column_width=True)
    with col3:
        st.image("3.gif", use_column_width=True)
    with col4:
        st.image("4.gif", use_column_width=True)
    with col5:
        st.image("5.gif", use_column_width=True)

if __name__ == "__main__":
    main()
