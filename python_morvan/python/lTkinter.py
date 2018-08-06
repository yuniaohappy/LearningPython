"""tkinter的Label和Button标签和按钮"""
import tkinter as tk
window = tk.Tk()
window.title("my window")
window.geometry('200x100')
l = tk.Label(window, text="this is tk",bg="green")
l.pack()
window.mainloop()