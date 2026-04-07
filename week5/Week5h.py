# Drag pattern (Press, motion, release)

import tkinter as tk

win = tk.Tk()
win.geometry("350x350")
win.title("Week 5")

# Create an info label
tk.Label(win, text="Press Esc to reset.").pack(pady=10, side="bottom")

# Create the draggable label and put it at an absolute position
lbl = tk.Label(win, text="Drag around", padx=12, pady=8, bd=1, relief="solid", bg="lightblue")
lbl.place(x=0, y=0)

# Widget storage for the click offset
lbl._click_offset_x = 0
lbl._click_offset_y = 0

def on_press(event):
    # Store the position where the user clicked inside the widget
    event.widget._click_offset_x = event.x
    event.widget._click_offset_y = event.y
    win.configure(cursor="fleur")  # Sets the mouse cursor to the "move" cursor

def on_motion(event):
    # Compute new top-left (widget) position in window coordinates

    # 1. Convert mouse screen coordinates to window-relative coordinates
    # event.x_root: Global horizontal position on the entire screen (monitor)
    # win.winfo_rootx(): The window's left edge position relative to the screen
    mouse_x_in_window = event.x_root - win.winfo_rootx()
    mouse_y_in_window = event.y_root - win.winfo_rooty()

    # 2. Subtract the initial click offset to keep the mouse pinned to the same spot
    # Without this, the widget's top-left corner would jump directly to the cursor
    new_x = mouse_x_in_window - event.widget._click_offset_x
    new_y = mouse_y_in_window - event.widget._click_offset_y

    # Update the widget's position within the window
    event.widget.place(x=new_x, y=new_y)

def on_release(event):
    win.configure(cursor="") # Resets mouse cursor to the default system cursor

def on_escape(event):
    lbl.place(x=0, y=0)

# Bind mouse and keyboard events
lbl.bind("<Button-1>", on_press)
lbl.bind("<B1-Motion>", on_motion)
lbl.bind("<ButtonRelease-1>", on_release)
win.bind("<Escape>", on_escape)

win.mainloop()
