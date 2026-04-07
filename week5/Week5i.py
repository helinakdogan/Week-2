# Context menu

import tkinter as tk

def on_right_click(event):
    # Positions the menu at the mouse's absolute screen coordinates (root x,y)
    # event.x_root, event.y_root returns the coordinate of the mouse relative to the top left corner of the screen.
    # event.x, event.y returns the coordinate of the mouse relative to the top left corner of the widget.
    context_menu.tk_popup(event.x_root, event.y_root)

win = tk.Tk()
win.geometry("300x300")
win.title("Week 5")

# Create an info label
tk.Label(win, text="Right-click to open context menu.").pack(pady=10, side="bottom")

# Create a context (popup) menu
context_menu = tk.Menu(win, tearoff=False)
context_menu.add_command(label="Cut")
context_menu.add_command(label="Copy")
context_menu.add_command(label="Paste")
context_menu.add_separator()
context_menu.add_command(label="Exit", command=win.destroy)

# Bind the right mouse button to open the context menu
win.bind("<Button-3>", on_right_click)

win.mainloop()
