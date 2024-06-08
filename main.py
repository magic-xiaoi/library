import pymysql
import PyQt5  as qt
from ui import *



if __name__ == "__main__":
    app = QApplication(sys.argv)
    col = Controller()
    col.show_login()

    sys.exit(app.exec_())
    pass


