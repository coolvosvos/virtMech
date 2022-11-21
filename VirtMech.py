from pynput import keyboard
import pyglet
from tkinter import *
from io import BytesIO




effect = pyglet.resource.media('mecKeyb.mp3', streaming=False)
is_on=False

def song():
    effect.play()

def on_release_keyb(key):
    song()

window=Tk()
window.title('Virtual Mechanic')
window.geometry("300x200")


statusLabel=Label(window,
    text="Mechanic Keyboard Sound OFF",
    fg="red",
    font=("Helvetica",12))

statusLabel.pack(pady=20)

def switch():
    global is_on
    global listener

    if is_on:
        on_button.config(image=off)
        statusLabel.config(text="Mechanic Keyboard Sound OFF", fg="red")
        is_on=False
        listener.stop()  # stop thread
        listener.join()  # wait till thread really ends its job
        listener = None
    else:
        on_button.config(image=on)
        statusLabel.config(text="Mechanic Keyboard Sound ON", fg="green")
        is_on=True
        listener = keyboard.Listener(
            on_release=on_release_keyb)
        listener.start()


on=PhotoImage(file="on.png")
off=PhotoImage(file="off.png")


on_button=Button(window,image=off,bd=0,command=switch)
on_button.pack(pady=50)


window.mainloop()


