# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import scrolledtext

def show_lyrics():
    root = tk.Tk()
    root.title("বাংলা গান")
    root.geometry("500x600")

    # Main frame
    text_area = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        font=("Nirmala UI", 16),   # বাংলা HD font
        padx=10,
        pady=10
    )
    text_area.pack(expand=True, fill="both")

    lyrics = """
গানটি শুনুন:

যদি বিরহ থাকে আমিও থাকি
কে বলো শেষ হবে আগে?
কেন যে এত ভালোবাসা মরে যায়
শুধু সময় মনে রাখে

[Chorus: Ankan Kumar]
এত শূন্যতা এ মনে রাখি যে আমি
দেখে না কেউ তো আর, বলে এ সবই পাগলামি
কাটে না যামিনী, বিরহ যেন কেটে যায়
থামে না বরষা, তোমারে ডাকি যে আমি
(আর)
"""

    text_area.insert(tk.INSERT, lyrics)
    text_area.config(state="disabled")  # Make read-only

    root.mainloop()

show_lyrics()
