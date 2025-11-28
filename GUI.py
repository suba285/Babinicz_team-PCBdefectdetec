import tkinter as tk
from tkinter import PhotoImage
from tkinter import filedialog as fd
from PIL import Image, ImageTk


class Window:
    def __init__(self):
        # window size x and y
        self.windx = 700
        self.windy = 500
        # window spawn offset
        wsoffset = 150

        tile_size = 100

        self.padx = 10
        self.pady = 5

        # image file path
        self.path = ""

        # root creation
        self.root = tk.Tk()
        self.root.geometry(f"{self.windx}x{self.windy}+{wsoffset}+{wsoffset}")
        self.root.resizable(False, False)

        # main canvas creation
        self.canvas = tk.Frame(self.root)
        self.canvas.grid(column=0, row=0)

        # placeholder image
        raw_image = Image.open("./gui_images/placeholder.png")
        res_image = raw_image.resize((300, 200))
        self.image = ImageTk.PhotoImage(res_image)

        # buttonbar of sorts
        self.btnframe = tk.Frame(self.canvas, borderwidth=1, relief="ridge", background="grey")

        lfb = lambda: self.file_browser()  # lambda file browser

        # button setup
        self.quitB = tk.Button(self.btnframe, text="quit", command=self.root.destroy, padx=self.padx, pady=self.pady, width=10)
        self.f_browserB = tk.Button(self.btnframe, text="file browser", padx=self.padx, pady=self.pady, command=lfb, width=10)
        self.checkB = tk.Button(self.btnframe, text="check PCB", padx=self.padx, pady=self.pady, width=10)

        self.img_label = tk.Label(self.canvas, image=self.image, pady=100, padx=100)

        self.checkB.config(state=tk.DISABLED)

    def set_img(self, new_img_path):
        raw_image = Image.open(new_img_path)
        res_image = raw_image.resize((300, 200))
        self.image = ImageTk.PhotoImage(res_image)
        self.img_label.config(image=self.image)

    def file_browser(self):
        fp = fd.askopenfilename(filetypes=[("txt", "*.txt"), ("png", "*.png"), ("jpeg", "*.jpeg")], title="choose file")
        self.checkB.config(state=tk.NORMAL)
        self.path = fp
        if fp != "":
            raw_image = Image.open(fp)
            res_image = raw_image.resize((300, 200))
            self.image = ImageTk.PhotoImage(res_image)
            self.img_label.config(image=self.image)

    def draw_win(self):

        # 'B' as the last char of an element name signifies it is a button

        # gridding
        self.btnframe.pack()

        self.img_label.pack()

        self.quitB.grid(column=0, row=0)
        self.f_browserB.grid(column=1, row=0)
        self.checkB.grid(column=2, row=0)

        self.root.mainloop()


