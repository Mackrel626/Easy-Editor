from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog
import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QPixmap

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle("Easy Editor")

btn_directory = QPushButton("Папка")
list_photos = QListWidget()
v1 = QVBoxLayout()
v1.addWidget(btn_directory)
v1.addWidget(list_photos)

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_mirror = QPushButton("Відзеркалнення")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
btn_back = QPushButton("назад")


v2 = QHBoxLayout()
v2.addWidget(btn_back)
v2.addWidget(btn_left)
v2.addWidget(btn_right)
v2.addWidget(btn_mirror)
v2.addWidget(btn_bw)
v2.addWidget(btn_sharp)

picture = QLabel("картинка")
h1 = QVBoxLayout()
h1.addWidget(picture)
h1.addLayout(v2)

h_main = QHBoxLayout()
h_main.addLayout(v1, 20)
h_main.addLayout(h1, 80)

win.setLayout(h_main)

workdir = ''

def filter(files, ext):
    photos = []
    for file in files:
        for e in ext:
            if file.endswith(e):
                photos.append(file)
    return photos

def open_forder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def get_files():
    open_forder()
    files = os.listdir(workdir)
    ext = [".png", '.jpg', '.jpeg']
    list_photos.addItems(filter(files, ext))

btn_directory.clicked.connect(get_files)

class ImangeProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def showImage(self, path):
        picture.hide()
        pixmapimage = QPixmap(path)
        w, h = picture.width(), picture.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)
        picture.show()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path = os.path.join(self.dir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_back():
        pass

    def saveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    

workimage = ImangeProcessor()

def showChosenImage():
    if list_photos.currentRow() >= 0:
        filename = list_photos.currentItem().text()
        workimage.loadImage(workdir,filename)
        Image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(Image_path)

list_photos.currentRowChanged.connect(showChosenImage)

btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_mirror.clicked.connect(workimage.do_flip)
#btn_back.clicked.connect(workimage.do_back)

win.show()
app.exec_()