import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from predictor import Predictor
from utilities.get_file_name import get_file_name
import os


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

        self.model = Predictor()

        # image file path
        self.path = ""

        # root creation
        self.root = tk.Tk()
        self.root.title("Defect Detect")
        self.root.geometry(f"{self.windx}x{self.windy}+{wsoffset}+{wsoffset}")
        self.root.resizable(False, False)

        # main canvas creation
        self.canvas = tk.Frame(self.root, padx=5, pady=5)
        self.canvas.grid(column=0, row=0)

        # image size
        self.imgx = 500
        self.imgy = 300

        # btn width
        self.btn_width = 15

        # placeholder image
        raw_image = Image.open("./gui_images/placeholder.png")
        res_image = raw_image.resize((self.imgx, self.imgy))
        self.image = ImageTk.PhotoImage(res_image)

        # buttonbar of sorts
        self.btnframe = tk.Frame(self.canvas, borderwidth=1, relief="ridge", background="grey", pady=1, padx=1)

        lfb = lambda: self.file_browser()  # lambda file browser

        # button setup
        self.quitB = tk.Button(self.btnframe, text="quit", command=self.root.destroy, padx=self.padx, pady=self.pady, width=self.btn_width)
        self.f_browserB = tk.Button(self.btnframe, text="file browser", padx=self.padx, pady=self.pady, command=lfb, width=self.btn_width)
        self.checkB = tk.Button(self.btnframe, text="check PCB", padx=self.padx, pady=self.pady, width=self.btn_width,
                                command=lambda: self.set_img(self.path))

        self.img_label = tk.Label(self.canvas, image=self.image)

        self.checkB.config(state=tk.DISABLED)

    def set_img(self, new_img_path):
        file_name = get_file_name(new_img_path)
        self.model.predict(new_img_path)
        result_path = f"./runs/detect/predict/{file_name}.jpg"
        raw_image = Image.open(result_path)
        res_image = raw_image.resize((self.imgx, self.imgy))
        self.image = ImageTk.PhotoImage(res_image)
        self.img_label.config(image=self.image)
        os.remove(result_path)

    def file_browser(self):
        fp = fd.askopenfilename(filetypes=[("png", "*.png"), ("jpeg", "*.jpeg")], title="choose file")
        self.checkB.config(state=tk.NORMAL)
        self.path = fp
        if fp != "":
            raw_image = Image.open(fp)
            res_image = raw_image.resize((self.imgx, self.imgy))
            self.image = ImageTk.PhotoImage(res_image)
            self.img_label.config(image=self.image)

    def draw_win(self):

        # 'B' as the last char of an element name signifies it is a button

        # gridding
        self.btnframe.pack()

        self.img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.quitB.grid(column=0, row=0)
        self.f_browserB.grid(column=1, row=0)
        self.checkB.grid(column=2, row=0)

        self.root.mainloop()


