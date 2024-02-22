import streamlit as st
from PIL import Image

def center_crop(image, crop_size):
    width, height = image.size
    left = (width - crop_size[0]) // 2
    top = (height - crop_size[1]) // 2
    right = (width + crop_size[0]) // 2
    bottom = (height + crop_size[1]) // 2
    return image.crop((left, top, right, bottom))

def main():
    st.title("Side by Side Video Display")

    # Load and display the first GIF with center cropping
    frames1 = load_frames("1.gif")
    cropped_frames1 = [center_crop(frame, (frame.width // 2, frame.height)) for frame in frames1]
    st.image(cropped_frames1, caption='Video 1', use_column_width=True)

    # Load and display the second GIF with center cropping
    frames2 = load_frames("2.gif")
    cropped_frames2 = [center_crop(frame, (frame.width // 2, frame.height)) for frame in frames2]
    st.image(cropped_frames2, caption='Video 2', use_column_width=True)

def load_frames(filename):
    gif = Image.open(filename)
    frames = []
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(len(frames))  # Move to next frame
    except EOFError:
        pass  # End of GIF
    return frames

if __name__ == "__main__":
    main()
