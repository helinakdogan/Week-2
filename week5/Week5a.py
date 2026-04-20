# Olay Bağlama I (Fare Tıklaması)

import tkinter as tk
from tkinter import ttk

def on_click(event):
    # Hangi fare tuşuna basıldığını belirler (1: Sol, 2: Orta, 3: Sağ)
    button_name = {1: "Left", 2: "Middle", 3: "Right"}.get(event.num, "Unknown")

    # Tıklama detaylarını (koordinatlar, olay türü, tıklanan buton) bir metinde toplar
    message = f"Clicked at: {event.x}, {event.y}.\n"
    message += f"Screen coordinates: {event.x_root}, {event.y_root}.\n"
    message += f"Event type: {event.type.name}.\n"
    message += f"Clicked button: {button_name}.\n"
    message += f"Button text: {event.widget['text']}.\n"
    
    # Hazırlanan mesajı ekrandaki etikete (label) yazdırır
    lbl.configure(text=message)

win = tk.Tk()
win.geometry("400x250")
win.title("Week 5")

btn_a = ttk.Button(win, text="Button A")
btn_b = ttk.Button(win, text="Button B")
lbl = ttk.Label(win, justify="center")

btn_a.pack(pady=(20, 0))
btn_b.pack(pady=20)
lbl.pack()

# Bazı fare olayları: Button (Tıklama), Button-1 (Sol tık), Button-3 (Sağ tık), ButtonRelease (Tıklamayı bırakma)

# A butonuna herhangi bir fare tuşuyla tıklandığında on_click fonksiyonunu tetikler
btn_a.bind("<Button>", on_click)
# B butonunda sağ tıka (3) basılıp *bırakıldığında* on_click fonksiyonunu tetikler
btn_b.bind("<ButtonRelease-3>", on_click)

# Başlangıçta klavye odağını A butonuna verir
btn_a.focus_set()

win.mainloop()
