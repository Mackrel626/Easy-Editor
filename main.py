from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QListWidget, QFileDialog
import os

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

v2 = QHBoxLayout()
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































win.show()
app.exec_()