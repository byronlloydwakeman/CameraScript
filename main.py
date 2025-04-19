# from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk

# define a video capture object
import numpy as np

# Video shit
vid = cv2.VideoCapture(0)


def TakeWebCamPic():
    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Saving image to directory
    return Image.fromarray(image_rgb, "RGB")


# Tkinter shit
# tk = Tk()
root = tk.Tk()
# tk.title("Window")
# tk.geometry("500x500")
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()


# def ShowSavedPhotoOnTkinter():
#     img = PhotoImage(file="my.Png")
#     canvas.create_image(10, 10, anchor=NW, image=img)
#     tk.mainloop()

img = ImageTk.PhotoImage(TakeWebCamPic())
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")


def UpdateImage():
    img2 = ImageTk.PhotoImage(TakeWebCamPic())
    panel.configure(image=img2)
    panel.image = img2


while True:
    UpdateImage()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

# while True:
#
#     # TakeAndSaveWebCam()
#     # ShowSavedPhotoOnTkinter
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
