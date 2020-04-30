import sys
import os
from PyQt5.QtWidgets import *
import Genarator
from functools import partial
from Tools import *

def click_generate(ui):
    cnt = int(ui.lineEdit.text())
    base = int(ui.lineEdit_2.text())
    path = conver_path(ui.textBrowser.toPlainText())
    rc_codes = generate_rc_code(base, cnt)
    ck_codes = generate_ck_code(cnt)
    pw = generate_pw(cnt)
    data = list(zip(rc_codes, ck_codes, pw))
    write_csv(path, data)
    QMessageBox.information(ui.pushButton, 'Msg', "Done")

def click_choose(ui):
    dir_path = QFileDialog.getExistingDirectory(None, "choose directory", "./")
    ui.textBrowser.setHtml(generate_html_text(dir_path))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Genarator.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(partial(click_generate, ui))
    ui.pushButton_2.clicked.connect(partial(click_choose, ui))
    MainWindow.show()
    sys.exit(app.exec_())
