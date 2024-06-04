import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None, title="Application"):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title(title)
        self.grid() # self to master
        self.create_widgets()

def create_widgets(self):
    self.label = tk.Label(self, text="Hello")
    self.label.grid() # label to self

if __name__ == "__main__":

    root = tk.Tk()
    app = Application(root)
    #print(app.label["text"]) # Hello
    root.mainloop() # or app.mainloop()