import tkinter as tk

root = tk.Tk() # root widget

root.option_add('*tearOff', tk.FALSE) # remove a dashed line from submenus

# create a menubar for the root window
menubar = tk.Menu(root)
root.config(menu=menubar)

# first submenu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: print("New"))
file_menu.add_command(label="Open...", command=lambda: print("Open..."))
file_menu.add_command(label="Save", command=lambda: print("Save"))
file_menu.add_separator() # adds a separator line
file_menu.add_command(label="Exit", command=lambda: print("Exit"))

# second submenu
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=lambda: print("Copy"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste"))
edit_menu.add_separator() # adds a separator line
edit_menu.add_command(label="Find...", command=lambda: print("Find..."))
edit_menu.add_command(label="Replace...", command=lambda: print("Replace..."))

# submenu
tools_menu = tk.Menu(menubar)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Scripts", command=lambda: print("Scripts"))

# submenu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About...", command=lambda: print("About..."))
root.mainloop()
