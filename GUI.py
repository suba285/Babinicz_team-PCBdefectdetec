import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from predictor import Predictor
from utilities.get_file_name import get_file_name
from camera import show_on_camera
import os
import multiprocessing
import time


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
        self.canvas.config(height=self.windy, width=self.windx, pady=1, padx=1)

        # image size
        self.imgx = 500
        self.imgy = 300

        # btn width
        self.btn_width = 10

        # image counter for buttons switching them
        self.img_counter = 0

        # placeholder image
        raw_image = Image.open("./gui_images/placeholder.png")
        res_image = raw_image.resize((self.imgx, self.imgy))
        self.image = ImageTk.PhotoImage(res_image)

        self.paths = []
        self.images = []
        self.images.append(self.image)

        # threads
        self.camps = []
        self.camprun = False

        # buttonbar of sorts
        self.btnframe = tk.Frame(self.canvas, pady=1, padx=1)

        lfb = lambda: self.file_browser()  # lambda file browser

        # button setup
        self.quitB = tk.Button(self.btnframe, text="quit", command=self.root.destroy, width=self.btn_width, height=2)
        self.f_browserB = tk.Button(self.btnframe, text="file browser", command=lfb, width=self.btn_width, height=2)
        self.checkB = tk.Button(self.btnframe, text="check PCB", width=self.btn_width,
                                command=lambda: self.set_img(), height=2)
        self.cameraB = tk.Button(self.btnframe, text="camera", command=lambda: self.cam_proc(), width=self.btn_width, height=2)

        self.leftB = tk.Button(self.canvas, text="<", command=lambda: self.img_dec(), height=2)
        self.rightB = tk.Button(self.canvas, text=">", command=lambda: self.img_inc(), height=2)
        self.leftB.config(state=tk.DISABLED)
        self.rightB.config(state=tk.DISABLED)

        self.img_label = tk.Label(self.canvas, image=self.image)

        self.checkB.config(state=tk.DISABLED)

    def set_img(self):
        self.images = []
        for path in self.paths:
            file_name = get_file_name(path)
            results = self.model.predict(path)
            result_path = f"./runs/detect/predict/{file_name}.jpg"
            raw_image = Image.open(result_path)
            res_image = raw_image.resize((self.imgx, self.imgy))
            image = ImageTk.PhotoImage(res_image)
            self.images.append(image)
            os.remove(result_path)  # deletes every result image after it's been saved into self.images
        if self.img_counter >= len(self.images):
            self.img_counter = 0
        self.img_label.config(image=self.images[self.img_counter])
        os.rmdir("./runs/detect/predict")  # deletes folder after it's been emptied (if it is not deleted,
        # ultralytics creates a new one

    def file_browser(self):
        self.images = []
        # fps = filepaths
        fps = fd.askopenfilenames(filetypes=[("png", "*.png"), ("jpeg", "*.jpeg"), ("jpg", "*.jpg")], title="choose file")
        # button disabling and enabling
        self.checkB.config(state=tk.NORMAL)
        if len(fps) > 1:
            self.leftB.config(state=tk.NORMAL)
            self.rightB.config(state=tk.NORMAL)
            self.checkB.config(text="check PCB's")
        else:
            self.leftB.config(state=tk.DISABLED)
            self.rightB.config(state=tk.DISABLED)
            self.checkB.config(text="check PCB")

        if not fps:
            self.images.append(self.image)
            self.checkB.config(state=tk.DISABLED)

        self.paths = fps
        for fp in fps:
            raw_image = Image.open(fp)
            res_image = raw_image.resize((self.imgx, self.imgy))
            self.images.append(ImageTk.PhotoImage(res_image))

        self.img_label.config(image=self.images[0])

    def img_inc(self):
        self.img_counter += 1
        if self.img_counter >= len(self.images):
            self.img_counter = 0
        self.img_label.config(image=self.images[self.img_counter])

    def img_dec(self):
        self.img_counter -= 1
        if self.img_counter < 0:
            self.img_counter = len(self.images) - 1
        self.img_label.config(image=self.images[self.img_counter])

    def cam_proc(self):
        if self.camprun:
            self.camps[0].terminate()
            time.sleep(0.1)
            if not self.camps[0].is_alive():
                self.camps[0].join(timeout=1.0)
            self.cameraB.config(text="camera")
            self.camprun = False
            self.camps = []
        else:
            camp = multiprocessing.Process(target=show_on_camera)
            self.camps.append(camp)
            self.camps[0].start()
            self.cameraB.config(text="quit camera")
            self.camprun = True

    def draw_win(self):

        # 'B' as the last char of an element name signifies it is a button

        # gridding
        self.btnframe.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.img_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.quitB.grid(column=0, row=0)
        self.f_browserB.grid(column=1, row=0)
        self.checkB.grid(column=2, row=0)
        self.cameraB.grid(column=3, row=0)

        self.leftB.place(relx=0.07, rely=0.45, anchor=tk.CENTER)
        self.rightB.place(relx=0.93, rely=0.45, anchor=tk.CENTER)

        self.root.mainloop()



