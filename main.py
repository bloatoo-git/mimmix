import sys
import json
import requests

from PyQt6.QtWidgets import (QApplication, QWidget)



# response = requests.get('https://api.coincap.io/v2/assets')
# data = response.json() if response and response.status_code == 200 else None

# print(data['data'])





class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mimmix')
        self.setGeometry(0, 0, 800, 600)
        self.init_ui()


    def init_ui(self):
        pass
        # create layouts here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show
    sys.exit(app.exec())