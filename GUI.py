import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk


class Window:
    def __init__(self):
        # window size x and y
        windx = 700
        windy = 500
        # window spawn offset
        wsoffset = 150

        tile_size = 100

        # root creation
        self.root = tk.Tk()
        self.root.geometry(f"{windx}x{windy}+{wsoffset}+{wsoffset}")
        self.root.resizable(False, False)

        # main canvas creation
        self.canvas = tk.Frame(self.root)
        self.canvas.grid(column=0, row=0)

        self.padx = 10
        self.pady = 5

        # image file path
        self.path = ""

    def file_browser(self):
        fp = fd.askopenfilename(filetypes=[("txt", "*.txt"), ("png", "*.png"), ("jpeg", "*.jpeg")], title="choose file")
        self.path = fp

    def draw_win(self):

        btnframe = tk.Frame(self.canvas, borderwidth=4, relief="ridge")


        # 'B' as the last char of an element name signifies it is a button

        lfb = lambda: self.file_browser()  # lambda file browser

        # button setup
        quitB = tk.Button(self.canvas, text="quit", command=self.root.destroy, padx=self.padx, pady=self.pady)
        f_browserB = tk.Button(self.canvas, text="file browser", padx=self.padx, pady=self.pady, command=lfb)

        # gridding
        quitB.grid(column=0, row=1)
        f_browserB.grid(column=1, row=1)

        self.root.mainloop()


