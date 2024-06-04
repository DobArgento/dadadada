import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root, width=200, height=200, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame2 = tk.Frame(root, width=100, height=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT, expand=True)

frame3 = tk.Frame(root, width=50, height=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT, expand=True)

root.mainloop()