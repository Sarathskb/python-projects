import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.photo = photo
        original_image = image.copy()
        image_label.original_image = original_image

def convert_to_bw():
    if hasattr(image_label, 'original_image'):
        original_image = image_label.original_image
        bw_image = original_image.convert("L")  # Convert to grayscale
        bw_photo = ImageTk.PhotoImage(bw_image)
        image_label.config(image=bw_photo)
        image_label.photo = bw_photo
        image_label.bw_image = bw_image

def save_image():
    if hasattr(image_label, 'bw_image'):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            bw_image = image_label.bw_image
            bw_image.save(save_path)

# Create the main window
root = tk.Tk()
root.title("Image Processor")
root.geometry("500x600")  # Set window size

# Create buttons for opening image, converting to black and white, and saving image
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

bw_button = tk.Button(root, text="Convert to Black and White", command=convert_to_bw)
bw_button.pack(pady=5)

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=5)

# Create a label to display the selected image
image_label = tk.Label(root)
image_label.pack()

root.mainloop()
