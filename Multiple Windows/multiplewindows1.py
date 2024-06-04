import tkinter as tk

root = tk.Tk() # we should start from root

root.title("root")

# Create root window contents...
# In Button, command=root.quit kills all windows.

top = tk.Toplevel()
#top = tk.Toplevel(root) # using explicit parent
top.title("top")

# Create top window contents...
# In Button, command=top.destroy only kills the current top window.

root.mainloop() # run the tkinter event loop
#top.mainloop() # also works