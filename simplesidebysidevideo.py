import tkinter as tk
from PIL import Image, ImageTk

class VideoPlayer(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Side by Side Video Display")
        
        # Load and display the first GIF with center cropping
        self.frames1 = self.load_frames("1.gif")
        self.cropped_frames1 = [self.center_crop(frame, (frame.width // 4, frame.height // 4, (3 * frame.width) // 4,  (3 * frame.height) // 4)) for frame in self.frames1]
        self.label1 = tk.Label(self)
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        # Load and display the second GIF with center cropping
        self.frames2 = self.load_frames("2.gif")
        self.cropped_frames2 = [self.center_crop(frame, (frame.width // 4, frame.height // 4, (3 * frame.width) // 4, (3 * frame.height) // 4)) for frame in self.frames2]
        self.label2 = tk.Label(self)
        self.label2.grid(row=0, column=1, padx=5, pady=5)

        # Start the GIF animations
        self.animate_gif(self.label1, self.cropped_frames1, 0)
        self.animate_gif(self.label2, self.cropped_frames2, 0)

    def load_frames(self, filename):
        gif = Image.open(filename)
        frames = []
        try:
            while True:
                frames.append(gif.copy())
                gif.seek(len(frames))  # Move to next frame
        except EOFError:
            pass  # End of GIF
        return frames

    def center_crop(self, image, box):
        return image.crop(box)

    def animate_gif(self, label, frames, idx):
        if idx < len(frames):
            photo = ImageTk.PhotoImage(frames[idx])
            label.configure(image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            idx += 1
            self.after(50, lambda: self.animate_gif(label, frames, idx))

if __name__ == "__main__":
    app = VideoPlayer()
    app.mainloop()
