import tkinter as tk 

root = tk.Tk()

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.grid()

listbox.insert(tk.END, "a list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(tk.END, item)

button = tk.Button(root, text="Choices", command=lambda:
    print([listbox.get(i) for i in listbox.curselection()]))
button.grid()

root.mainloop()