from PyQt5.uic import loadUiType
import sys
from os import path
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import form
import Scanner
import cv2


FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "gui.ui")) 
front_addr=''
back_addr=''
class MainApp(QMainWindow, FORM_CLASS):

    

    def __init__(self, parent= None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.front_btn.clicked.connect(self.front)  #nhấn nút gọi hàm font

        self.back_btn.clicked.connect(self.back)  #nhấn nút gọi hàm back

        self.generate_btn.clicked.connect(self.generate) #nhấn nút gọi hàm generate
        

    def front(self):
        global front_addr
        front_addr,_ = QFileDialog.getOpenFileName(self,'Open File','',"Image files(*.jpg *.png *.jpeg)")#load file ảnh từ máy tính
        Scanner.scan(front_addr,"front")  #đầu vào là ảnh, tiến hành cắt các cạnh trả về là hình ảnh temp_back ở thư mục cùng cấp
        #front_addr = str(front_addr)[2:str(front_addr).find(',')-1]
        pixmap = QPixmap("temp_front.jpg") # đặt ảnh cho pixmap
        self.label_imgf.setPixmap(pixmap)  #hiện thị hình ảnh lên cửa sổ
        self.label_imgf.setScaledContents(True) # đặt hình ảnh vừa với tỉ lệ của khung
        
##        
        
##        print ("____",front_addr,"____")

    def back(self):  #như trên
        global back_addr
        back_addr,_ = QFileDialog.getOpenFileName(self,'Open File','',"Image files(*.jpg *.png *.jpeg)")
        Scanner.scan(back_addr,"back")
        #back_addr = str(back_addr)[2:str(back_addr).find(',')-1]
        pixmap = QPixmap("temp_back.jpg")
        
        self.label_imgb.setPixmap(pixmap)
        self.label_imgb.setScaledContents(True)

        #print(input_file1)

##        print ("____",back_addr,"____")
	
  
    def generate(self): #nút thực hiện
        global front_addr,back_addr
        if front_addr=='' or back_addr=='': #kiểm tra có chèn ảnh hay chưa
            QMessageBox.about(self, "Couldn't generate", "Image is not inserted!")
        else:
            form.form("temp_front.jpg","temp_back.jpg") #gọi hàm from
            print("done")
        
   


def main():
    app = QApplication(sys.argv)  #tạo ứng dụng từ thư viện qt5
    window = MainApp()  #gọi cửa sổ mainapp phía trên
    window.show()  #show

    sys.exit(app.exec_())    #thoát


if __name__ == '__main__':
    main()



