import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root, width=200, height=200, bg="yellow")
frame1.pack(fill=tk.BOTH)

frame2 = tk.Frame(root, width=100, height=100, bg="blue")
frame2.pack(fill=tk.BOTH)

frame3 = tk.Frame(root, width=50, height=50, bg="red")
frame3.pack(fill=tk.BOTH)

root.mainloop()