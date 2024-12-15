import sys
from PyQt6.QtWidgets import QApplication, QMessageBox

app = QApplication(sys.argv)
#Tao hop thong bao
htb = QMessageBox()
#Tieu de
htb.setWindowTitle("Hop thong bao lop PTA06")
#Dat icon
htb.setIcon(QMessageBox.Icon.Warning)
#Thong bao den nguoi dung
htb.setText("Ban co thuc su muon thoat khoi chuong trinh hay khong?")
#Chinh styleSheet
htb.setStyleSheet("background-color: yellow; color:white")
sys.exit(htb.exec())