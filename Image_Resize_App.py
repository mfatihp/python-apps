"""
Author: Muhammet Fatih POLAT

Purpose:
This app converts images you want with given width and height info.

Required libraries:
1. OpenCV
2. Tkinter

Usage:
In open_image() function, you have to put your desired location to 'initialdir'
In resized() function, you have to put your desired location to 'cv.imwrite()'

"""
import cv2 as cv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


# Take image location
def open_image():
    root.filename = filedialog.askopenfilename(initialdir="*Insert Your Location*",
                                               title="Select an Image",
                                               filetypes=(("png files", "*.png"), ("all files", "*.*")))


# Resize func
def resized(img, w=50, h=50):

    # Read image
    image = cv.imread(img)

    # Resize image
    dsize = (w, h)
    output = cv.resize(image, dsize, interpolation=cv.INTER_AREA)
    
    # Save resized image
    cv.imwrite("/*Insert Your Location*/resized.png", output)

    messagebox.showinfo("Info", message="Resize Complete!")


# GUI
root = Tk()
root.title("Image Resize App")

# Open Button
Label(root, text="Select Image : ").grid(row=1, column=0)
open_button = Button(root, text="Open", command=open_image, bg="#ffffff").grid(row=1, column=1)

# Width entry
Label(root, text="Width : ").grid(row=2, column=0)
width = Entry(master=root, width=50)
width.grid(row=2, column=1)

# Height entry
Label(root, text="Height : ").grid(row=3, column=0)
height = Entry(master=root, width=50)
height.grid(row=3, column=1)

# Confirm and Quit buttons
confirm_button = Button(master=root, text="Confirm", bg="#ffffff",
                        command=lambda: resized(root.filename, int(width.get()), int(height.get())))
confirm_button.grid(row=4, column=1)
quit_button = Button(master=root, text="Quit", bg="#ffffff", fg="red", command=root.quit)
quit_button.grid(row=5, column=1)

# mainloop
root.mainloop()


        


