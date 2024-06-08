from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

from users_class import Lib_User,Lib_Manager
from data_operation.select_operation import select_by_multipy,select_by_multipy_and_id
from data_operation.db_operation import *
import  sys
import os

dir = os.path.dirname(__file__)

# 页面跳转controller
class Controller(object):
    def __init__(self):
        self.loginwin = Login_win()
        self.Mainwin = Main_win()# 用户大厅
        self.AMainwin = AMain_win()# 管理员大厅
        self.Sendwin = Send_win()
        self.Borrowwin = Borrow_win()
        self.Add_Bookwin = Add_Book_win()
        self.Add_Userwin  =Add_User_win()
        self.Delete_Bookwin = Delete_Book_win()
        self.Borrorw_Recordwin =Borrorw_Record_win()
        self.Send_Recordwin  = Send_Record_win()
        self.Borrorwed_Bookwin = Borrorwed_Book_win()
        self.init_signal()

    # 初始化信号
    def init_signal(self):
        self.loginwin.switch_to_main.connect(self.login_to_Main)
        self.loginwin.switch_to_admin_main.connect(self.login_to_AMain)
        self.Sendwin.switch_to_Main.connect(self.Send_to_Main)
        self.Borrowwin.switch_to_main.connect(self.Borrow_to_Main)

        self.Add_Bookwin.switch_to_AMain.connect(self.Add_Book_to_AMain)
        self.Add_Userwin.switch_to_AMain.connect(self.Add_User_to_AMain)
        self.Delete_Bookwin.switch_to_main.connect(self.Delete_Book_to_AMain)
        self.Borrorw_Recordwin.switch_to_main.connect(self.Borrorw_Record_to_AMain)
        self.Send_Recordwin.switch_to_main.connect(self.Send_Record_to_AMain)
        self.Borrorwed_Bookwin.switch_to_AMain.connect(self.Borrorwed_Book_to_AMain)

        # 大厅操作
        self.Mainwin.switch_3.connect(self.Main_to_Send)
        self.Mainwin.switch_2.connect(self.Main_to_Borrow)

        self.AMainwin.switch_add_book.connect(self.AMain_to_Add_book)
        self.AMainwin.switch_add_user.connect(self.AMain_to_Add_user)
        self.AMainwin.switch_del_book.connect(self.AMain_to_del_book)
        self.AMainwin.switch_borrow_log.connect(self.AMain_to_Borrow_Record)
        self.AMainwin.switch_send_log.connect(self.AMain_to_Send_Record)
        self.AMainwin.switch_select_book_borrowed.connect(self.AMain_to_Borrowed_Book)

    # ====================页面跳转函数====================
    def AMain_to_Borrowed_Book(self):
        self.AMainwin.close()
        self.Borrorwed_Bookwin.initUI()
        self.Borrorwed_Bookwin.show()


    def Borrorwed_Book_to_AMain(self):
        self.Borrorwed_Bookwin.close()
        self.AMainwin.show()


    def Send_Record_to_AMain(self):
        self.Send_Recordwin.close()
        self.AMainwin.show()

    def AMain_to_Send_Record(self):
        self.AMainwin.close()
        self.Send_Recordwin.init_ui({})# 进行刷新
        self.Send_Recordwin.show()

    def AMain_to_Borrow_Record(self):
        self.AMainwin.close()
        self.Borrorw_Recordwin.init_ui({})  # 进行刷新
        self.Borrorw_Recordwin.show()

    def Borrorw_Record_to_AMain(self):
        self.Borrorw_Recordwin.close()
        self.AMainwin.show()


    def AMain_to_del_book(self):
        self.AMainwin.close()
        self.Delete_Bookwin.show()

    def Delete_Book_to_AMain(self):
        self.Delete_Bookwin.close()
        self.AMainwin.show()

    def AMain_to_Add_user(self):
        self.AMainwin.close()
        self.Add_Userwin.show()


    def Add_User_to_AMain(self):
        self.Add_Userwin.close()
        self.AMainwin.show()


    def AMain_to_Add_book(self):
        self.AMainwin.close()
        self.Add_Bookwin.show()


    def Add_Book_to_AMain(self):
        self.Add_Bookwin.close()
        self.AMainwin.show()

    def login_to_AMain(self):
        # 进行页面跳转
        self.loginwin.close()
        self.AMainwin.show()

    def Borrow_to_Main(self):
        self.Borrowwin.close()
        self.Mainwin.show()

    def Main_to_Borrow(self):
        self.Borrowwin.init_user(self.user)
        self.Mainwin.close()
        self.Borrowwin.show()

    def login_to_Main(self):
        # 先将生成的user传入
        self.user = self.loginwin.get_User()
        self.Mainwin.init_user(self.user)

        # 进行页面跳转
        self.loginwin.close()
        self.Mainwin.show()

    def Main_to_Send(self):
        self.Sendwin.init_user(self.user)

        # 跳转
        self.Mainwin.close()
        self.Sendwin.show()

    # 跳转到主页面
    def Send_to_Main(self):
        self.Sendwin.close()
        self.Mainwin.show()

    # ========================================

    # 初始展示函数
    def show_login(self):
        self.loginwin.show()

# 管理员大厅
class AMain_win(QWidget):
    switch_add_book = QtCore.pyqtSignal()
    switch_del_book = QtCore.pyqtSignal()
    switch_add_user = QtCore.pyqtSignal()
    switch_select_book_borrowed = QtCore.pyqtSignal()
    switch_borrow_log = QtCore.pyqtSignal()
    switch_send_log = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.con_func()


    def init_ui(self):
        Amain_filepath = os.path.join(dir, "UI_window/AMain_win.ui")
        self.AMainWindow = uic.loadUi(Amain_filepath)
        self.add_book_btn =  self.AMainWindow.pushButton_4
        self.del_book_btn = self.AMainWindow.pushButton
        self.add_user_btn = self.AMainWindow.pushButton_6
        self.select_book_borrowed_btn = self.AMainWindow.pushButton_5
        self.borrow_log_btn = self.AMainWindow.pushButton_2
        self.send_log_btn = self.AMainWindow.pushButton_3



    def con_func(self):
        self.add_book_btn.clicked.connect(self.add_book)
        self.del_book_btn.clicked.connect(self.del_book)
        self.add_user_btn.clicked.connect(self.add_user)
        self.select_book_borrowed_btn.clicked.connect(self.select_book_borrowed)
        self.borrow_log_btn.clicked.connect(self.borrow_log)
        self.send_log_btn.clicked.connect(self.send_log)

    def show(self):
        self.AMainWindow.show()


    def add_book(self):
        self.switch_add_book.emit()


    def del_book(self):
        self.switch_del_book.emit()

    def add_user(self):
        self.switch_add_user.emit()

    def select_book_borrowed(self):
        self.switch_select_book_borrowed.emit()

    def borrow_log(self):
        self.switch_borrow_log.emit()

    def send_log(self):
        self.switch_send_log.emit()

    # 用户大厅
class Main_win(QWidget):
    switch_2 = QtCore.pyqtSignal()
    switch_3 = QtCore.pyqtSignal() # 跳转到send界面的信号

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.con_func()
        pass

    def init_user(self,user):
        self.user = user

    def init_ui(self):
        main_filepath = os.path.join(dir, "UI_window/Main_win.ui")
        self.MainWindow = uic.loadUi(main_filepath)
        self.borrow_btn = self.MainWindow.pushButton_2
        self.send_btn = self.MainWindow.pushButton_3

    def con_func(self):
        self.borrow_btn.clicked.connect(self.borror)
        self.send_btn.clicked.connect(self.send)

    def borror(self):
        self.switch_2.emit()

    def send(self):
        self.switch_3.emit()

    def close(self):
        self.MainWindow.close()

    def show(self):
        self.MainWindow.show()



class Borrorwed_Book_win(QMainWindow):
    switch_to_AMain = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.mouse_on_row = 10000
        self.setGeometry(800, 300, 550, 300)
        self.initUI()


    # 初始化绑定函数
    def con_func(self):
        self.button2.clicked.connect(self.quit)

    def on_cell_clicked(self, row):
        self.mouse_on_row = row

    def get_info(self):
        sql_order = "SELECT bb.BOOK_ID,BNAME,bb.STU_ID,SNAME FROM borrowed_book AS bb,users AS us,books AS bs WHERE bb.`BOOK_ID` =  bs.`BOOK_ID` AND bb.`STU_ID` = us.`STU_ID`"
        res = execute_select(sql_order)
        return res

    def initUI(self):
        self.book_info = self.get_info()

        # 创建 QTableWidget 控件
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(len(self.book_info))
        self.tableWidget.setColumnCount(4)

        for row in range(len(self.book_info)):
            for col in range(4):
                item = QTableWidgetItem(f"{self.book_info[row][col]}")
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.setHorizontalHeaderLabels(["BOOK_ID", "BNAME", "STU_ID", "STU_NAME"])
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

        # 创建 QPushButton 按钮
        self.button2 = QPushButton("退出")

        # 创建 QVBoxLayout 布局，并将表格和按钮添加进去
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.button2)

        # 创建一个 QWidget 来容纳整个布局，并将其设置为主窗口的中心部件
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("在借书籍查询")
        self.con_func()


    # 跳转到主页面
    def quit(self):
        self.switch_to_AMain.emit()

class Borrorw_Record_win(QMainWindow):
    switch_to_main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.mouse_on_row = 10000
        self.init_ui()

    def con_func(self):
        self.button1.clicked.connect(self.select_ui)
        self.button2.clicked.connect(self.delete)
        self.button3.clicked.connect(self.quit)

    def init_ui(self, condition={}):

        self.send_info = select_by_multipy_and_id(condition,table="borrow_record")

        self.setWindowTitle('借阅记录页面')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 创建水平布局
        self.layout = QHBoxLayout()

        # 创建左侧垂直布局
        self.left_layout = QVBoxLayout()

        # 创建输入框和标签
        self.label1 = QLabel('图书ID:')
        self.label1.setFixedWidth(160)
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(160)


        self.label2 = QLabel('借阅日期范围(小)')
        self.label2.setFixedWidth(160)
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(160)

        self.label3 = QLabel('借阅日期范围(大)')
        self.label3.setFixedWidth(160)
        self.input3 = QLineEdit()
        self.input3.setFixedWidth(160)

        self.label4 = QLabel('用户ID')
        self.label4.setFixedWidth(160)
        self.input4 = QLineEdit()
        self.input4.setFixedWidth(160)

        self.left_layout.addWidget(self.label1)
        self.left_layout.addWidget(self.input1)
        self.left_layout.addWidget(self.label2)
        self.left_layout.addWidget(self.input2)
        self.left_layout.addWidget(self.label3)
        self.left_layout.addWidget(self.input3)
        self.left_layout.addWidget(self.label4)
        self.left_layout.addWidget(self.input4)


        # 创建按钮
        self.button1 = QPushButton('查询')
        self.button1.setFixedWidth(100)
        self.button2 = QPushButton('删除')
        self.button2.setFixedWidth(100)
        self.button3 = QPushButton('退出')
        self.button3.setFixedWidth(100)

        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)

        # 创建右侧布局
        right_layout = QVBoxLayout()

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(self.send_info))
        self.table.setColumnCount(4)
        # 插入数据
        for row in range(len(self.send_info)):
            for col in range(4):
                item = QTableWidgetItem(f"{self.send_info[row][col]}")
                self.table.setItem(row, col, item)

        self.table.setHorizontalHeaderLabels(["index", "STU_ID", "BOOK_ID","BDATE"])

        # 设置表头自适应内容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        right_layout.addWidget(self.table)

        # 将左右布局添加到总体布局中
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(right_layout)
        self.table.cellClicked.connect(self.on_cell_clicked)

        centralWidget.setLayout(self.layout)

        # 绑定函数
        self.con_func()

    def select_ui(self):
        limit_con = self.get_limit_condition()  # 得到条件
        # 再次进行渲染
        self.init_ui(limit_con)

    # 得到限定条件
    def get_limit_condition(self):
        limit_con = {}
        BOOK_ID = self.input1.text().strip()
        PRO_DATE = self.input2.text().strip()
        LAS_DATE = self.input3.text().strip()
        STU_ID = self.input4.text().strip()


        con_list = [BOOK_ID, PRO_DATE, LAS_DATE, STU_ID]
        con_list_name = ["BOOK_ID", "PRO_DATE", "LAS_DATE", "STU_ID"]

        # 进行判断
        for idx, i in enumerate(con_list):
            # 防止值为空
            if len(i) > 0:
                if con_list_name[idx] in ["PRO_DATE", "LAS_DATE"]:
                    flag = judge_date(con_list[idx])

                    if not flag:
                        msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入日期!')
                        msg_box.exec_()
                        return {}

                limit_con[con_list_name[idx]] = i

        return limit_con

    def delete(self):
        if self.mouse_on_row >= len(self.send_info):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请选择要删的记录')
            msg_box.exec_()
            return

        # 得到对应的R_ID
        R_ID = self.send_info[self.mouse_on_row][0]
        # 删除对应的记录
        sql_order = "delete from borrow_record where R_ID = '%s';"%(R_ID)
        if execute_alert(sql_order,mul=False):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '删除成功')
            msg_box.exec_()

        self.init_ui()  # 进行刷新

    def quit(self):
        self.switch_to_main.emit()

    def on_cell_clicked(self, row):
        self.mouse_on_row = row


class Send_Record_win(QMainWindow):
    switch_to_main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.mouse_on_row = 10000
        self.init_ui()

    def con_func(self):
        self.button1.clicked.connect(self.select_ui)
        self.button2.clicked.connect(self.delete)
        self.button3.clicked.connect(self.quit)

    def init_ui(self, condition={}):

        self.send_info = select_by_multipy_and_id(condition,table="send_record")

        self.setWindowTitle('归还记录页面')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 创建水平布局
        self.layout = QHBoxLayout()

        # 创建左侧垂直布局
        self.left_layout = QVBoxLayout()

        # 创建输入框和标签
        self.label1 = QLabel('图书ID:')
        self.label1.setFixedWidth(160)
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(160)


        self.label2 = QLabel('归还日期范围(小)')
        self.label2.setFixedWidth(160)
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(160)

        self.label3 = QLabel('归还日期范围(大)')
        self.label3.setFixedWidth(160)
        self.input3 = QLineEdit()
        self.input3.setFixedWidth(160)

        self.label4 = QLabel('用户ID')
        self.label4.setFixedWidth(160)
        self.input4 = QLineEdit()
        self.input4.setFixedWidth(160)

        self.left_layout.addWidget(self.label1)
        self.left_layout.addWidget(self.input1)
        self.left_layout.addWidget(self.label2)
        self.left_layout.addWidget(self.input2)
        self.left_layout.addWidget(self.label3)
        self.left_layout.addWidget(self.input3)
        self.left_layout.addWidget(self.label4)
        self.left_layout.addWidget(self.input4)


        # 创建按钮
        self.button1 = QPushButton('查询')
        self.button1.setFixedWidth(100)
        self.button2 = QPushButton('删除')
        self.button2.setFixedWidth(100)
        self.button3 = QPushButton('退出')
        self.button3.setFixedWidth(100)

        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)

        # 创建右侧布局
        right_layout = QVBoxLayout()

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(self.send_info))
        self.table.setColumnCount(4)
        # 插入数据
        for row in range(len(self.send_info)):
            for col in range(4):
                item = QTableWidgetItem(f"{self.send_info[row][col]}")
                self.table.setItem(row, col, item)

        self.table.setHorizontalHeaderLabels(["index", "STU_ID", "BOOK_ID","BDARE"])

        # 设置表头自适应内容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        right_layout.addWidget(self.table)

        # 将左右布局添加到总体布局中
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(right_layout)
        self.table.cellClicked.connect(self.on_cell_clicked)

        centralWidget.setLayout(self.layout)

        # 绑定函数
        self.con_func()

    def select_ui(self):
        limit_con = self.get_limit_condition()  # 得到条件
        # 再次进行渲染
        self.init_ui(limit_con)

    # 得到限定条件
    def get_limit_condition(self):
        limit_con = {}
        BOOK_ID = self.input1.text().strip()
        PRO_DATE = self.input2.text().strip()
        LAS_DATE = self.input3.text().strip()
        STU_ID = self.input4.text().strip()


        con_list = [BOOK_ID, PRO_DATE, LAS_DATE, STU_ID]
        con_list_name = ["BOOK_ID", "PRO_DATE", "LAS_DATE", "STU_ID"]

        # 进行判断
        for idx, i in enumerate(con_list):
            # 防止值为空
            if len(i) > 0:
                if con_list_name[idx] in ["PRO_DATE", "LAS_DATE"]:
                    flag = judge_date(con_list[idx])

                    if not flag:
                        msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入日期!')
                        msg_box.exec_()
                        return {}

                limit_con[con_list_name[idx]] = i

        return limit_con

    def delete(self):
        if self.mouse_on_row >= len(self.send_info):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请选择要删的记录')
            msg_box.exec_()
            return

        # 得到对应的S_ID
        S_ID = self.send_info[self.mouse_on_row][0]
        # 删除对应的记录
        sql_order = "delete from send_record where S_ID = '%s';"%(S_ID)
        if execute_alert(sql_order, mul=False):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '删除成功')
            msg_box.exec_()

        self.init_ui()  # 进行刷新

    def quit(self):
        self.switch_to_main.emit()

    def on_cell_clicked(self, row):
        self.mouse_on_row = row

class Delete_Book_win(QMainWindow):
    switch_to_main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.mouse_on_row = 10000
        self.init_ui()

    def con_func(self):
        self.button1.clicked.connect(self.select_ui)
        self.button2.clicked.connect(self.delete)
        self.button3.clicked.connect(self.quit)

    def init_ui(self, condition={}):

        self.book_info = select_by_multipy_and_id(condition)

        self.setWindowTitle('删除页面')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 创建水平布局
        self.layout = QHBoxLayout()

        # 创建左侧垂直布局
        self.left_layout = QVBoxLayout()

        # 创建输入框和标签
        self.label1 = QLabel('书名:')
        self.label1.setFixedWidth(160)
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(160)

        self.label2 = QLabel('出版社:')
        self.label2.setFixedWidth(160)
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(160)

        self.label3 = QLabel('作者:')
        self.label3.setFixedWidth(160)
        self.input3 = QLineEdit()
        self.input3.setFixedWidth(160)

        self.label4 = QLabel('出版日期范围(小)')
        self.label4.setFixedWidth(160)
        self.input4 = QLineEdit()
        self.input4.setFixedWidth(160)

        self.label5 = QLabel('出版日期范围(大)')
        self.label5.setFixedWidth(160)
        self.input5 = QLineEdit()
        self.input5.setFixedWidth(160)

        self.label6 = QLabel('是否在馆(1/0):')
        self.label6.setFixedWidth(160)
        self.input6 = QLineEdit()
        self.input6.setFixedWidth(160)

        self.left_layout.addWidget(self.label1)
        self.left_layout.addWidget(self.input1)
        self.left_layout.addWidget(self.label2)
        self.left_layout.addWidget(self.input2)
        self.left_layout.addWidget(self.label3)
        self.left_layout.addWidget(self.input3)
        self.left_layout.addWidget(self.label4)
        self.left_layout.addWidget(self.input4)
        self.left_layout.addWidget(self.label5)
        self.left_layout.addWidget(self.input5)
        self.left_layout.addWidget(self.label6)
        self.left_layout.addWidget(self.input6)

        # 创建按钮
        self.button1 = QPushButton('查询')
        self.button1.setFixedWidth(100)
        self.button2 = QPushButton('删除')
        self.button2.setFixedWidth(100)
        self.button3 = QPushButton('退出')
        self.button3.setFixedWidth(100)

        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)

        # 创建右侧布局
        right_layout = QVBoxLayout()

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(self.book_info))
        self.table.setColumnCount(7)
        # 插入数据
        for row in range(len(self.book_info)):
            for col in range(7):
                item = QTableWidgetItem(f"{self.book_info[row][col]}")
                self.table.setItem(row, col, item)

        self.table.setHorizontalHeaderLabels(["BOOK_ID", "BNAME", "publisher", "AUTHOR", "CDATE", "CLASS", "FLAG"])

        # 设置表头自适应内容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        right_layout.addWidget(self.table)

        # 将左右布局添加到总体布局中
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(right_layout)
        self.table.cellClicked.connect(self.on_cell_clicked)

        centralWidget.setLayout(self.layout)

        # 绑定函数
        self.con_func()

    def select_ui(self):
        limit_con = self.get_limit_condition()  # 得到条件
        # 再次进行渲染
        self.init_ui(limit_con)

    # 得到限定条件
    def get_limit_condition(self):
        limit_con = {}
        BNAME = self.input1.text().strip()
        publisher = self.input2.text().strip()
        AUTHOR = self.input3.text().strip()
        PRO_DATE = self.input4.text().strip()
        LAS_DATE = self.input5.text().strip()
        FLAG = self.input6.text().strip()

        con_list = [BNAME, publisher, AUTHOR, PRO_DATE, LAS_DATE, FLAG]
        con_list_name = ["BNAME", "publisher", "AUTHOR", "PRO_DATE", "LAS_DATE", "FLAG"]

        # 进行判断
        for idx, i in enumerate(con_list):
            # 防止值为空
            if len(i) > 0:
                if con_list_name[idx] in ["PRO_DATE", "LAS_DATE"]:
                    flag = judge_date(con_list[idx])

                    if not flag:
                        msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入日期!')
                        msg_box.exec_()
                        return {}

                if con_list_name[idx] == "FLAG":
                    if con_list[idx] not in ["0", "1"]:
                        msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入馆藏信息!')
                        msg_box.exec_()
                        return {}
                    else:
                        con_list[idx] = int(con_list[idx])

                limit_con[con_list_name[idx]] = i

        return limit_con

    def delete(self):
        if self.mouse_on_row >= len(self.book_info):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请选择要借书籍')
            msg_box.exec_()
            return

        # 得到对应的书名
        BOOK_ID = self.book_info[self.mouse_on_row][0]
        if delete_book(BOOK_ID):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '删除成功')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '删除失败')
            msg_box.exec_()
        self.init_ui()  # 进行刷新

    def quit(self):
        self.switch_to_main.emit()

    def on_cell_clicked(self, row):
        self.mouse_on_row = row

class Add_User_win(QWidget):
    switch_to_AMain = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.con_fun()


    def init_ui(self):
        Add_User_filepath = os.path.join(dir, "UI_window/add_user_win.ui")
        self.add_user_Window = uic.loadUi(Add_User_filepath)
        self.STU_NAME_edit = self.add_user_Window.lineEdit
        self.STU_ID_edit = self.add_user_Window.lineEdit_2
        self.SEX_edit = self.add_user_Window.lineEdit_3
        self.birth_edit = self.add_user_Window.lineEdit_4
        self.submit_btn = self.add_user_Window.pushButton
        self.quit_btn =  self.add_user_Window.pushButton_2

    def con_fun(self):
        self.submit_btn.clicked.connect(self.submit)
        self.quit_btn.clicked.connect(self.quit)

    def quit(self):
        self.switch_to_AMain.emit()

    def show(self):
        self.add_user_Window.show()

    def close(self):
        self.add_user_Window.close()

    def submit(self):
        stu_name = self.STU_NAME_edit.text().strip()
        stu_id = self.STU_ID_edit.text().strip()
        sex = self.SEX_edit.text().strip()
        birth = self.birth_edit.text().strip()
        data_info = [stu_name,stu_id,sex,birth]

        sql_order = "SELECT STU_ID FROM users "
        res = execute_select(sql_order)
        stu_ids = [] # 学生id

        for i in res:
            stu_ids.append(i[0])

        # 进行规范性检查
        for i in data_info:
            if len(i) ==0:
                # 进行错误处理
                msg_box = QMessageBox(QMessageBox.Information, '提醒', '请填写所有信息')
                msg_box.exec_()
                return

        if stu_id in stu_ids:
            #  进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '错误', '用户ID已经存在')
            msg_box.exec_()
            return

        if not judge_date(birth):
            # 进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '错误', '请填写正确的日期')
            msg_box.exec_()
            return

        if sex not in ["男","女"]:
            # 进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '错误', '请填写正确性别')
            msg_box.exec_()
            return

        flag = insert_user(stu_name,stu_id,sex,birth)
        if flag:
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '成功提交')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '错误', '提交失败')
            msg_box.exec_()




class Add_Book_win(QWidget):
    switch_to_AMain = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.con_func()


    def con_func(self):
        self.submit_btn.clicked.connect(self.submit)
        self.quit_btn.clicked.connect(self.quit)

    def init_ui(self):
        Add_Book_filepath = os.path.join(dir, "UI_window/add_book_win.ui")
        self.add_book_Window = uic.loadUi(Add_Book_filepath)
        self.submit_btn = self.add_book_Window.pushButton_2
        self.quit_btn =  self.add_book_Window.pushButton_3
        self.BOOK_ID_edit = self.add_book_Window.lineEdit
        self.BNAME_edit = self.add_book_Window.lineEdit_2
        self.publisher_edit = self.add_book_Window.lineEdit_3
        self.AUTHOR_edit = self.add_book_Window.lineEdit_4
        self.CDATE_edit = self.add_book_Window.lineEdit_5
        self.CLASS_edit = self.add_book_Window.lineEdit_6

    def submit(self):
        book_id = self.BOOK_ID_edit.text().strip() # 防止主键重合
        book_name = self.BNAME_edit.text().strip()
        publisher = self.publisher_edit.text().strip()
        author = self.AUTHOR_edit.text().strip()
        cdate = self.CDATE_edit.text().strip()
        _class = self.CLASS_edit.text().strip()
        data_list = [book_id,book_name,publisher,author,cdate,_class]

        # 获取class列表
        sql_order1 = "SELECT  class_name FROM book_class;"
        sql_order2 = "SELECT  BOOK_ID FROM books;"
        res1 = execute_select(sql_order1)
        res2 = execute_select(sql_order2)
        class_list  = []
        bookId_list = []
        for i in res1:
            class_list.append(i[0])
        for i in res2:
            bookId_list.append(i[0])

        #  进行输入规范性检验
        # 不允许为空
        for i in data_list:
            if len(i) == 0:
                #  进行错误处理
                msg_box = QMessageBox(QMessageBox.Information, '提醒', '还存在信息空缺!')
                msg_box.exec_()
                return

        if _class not in class_list:
            # 进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '该类别不存在数据库中!')
            msg_box.exec_()
            return

        # 进行book_id判断
        if book_id in bookId_list:
            # 进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '该书籍ID已经存在，请重新填写!')
            msg_box.exec_()
            return

        if not judge_date(cdate):
            #  进行错误处理
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入日期!')
            msg_box.exec_()
            return

        flag = insert_book(book_id, book_name,publisher,author,cdate,_class)
        print(flag)
        if not flag:
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '添加失败!')
            msg_box.exec_()
        else:
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '添加成功!')
            msg_box.exec_()

    def quit(self):
        self.switch_to_AMain.emit()

    def close(self):
        self.add_book_Window.close()

    def show(self):
        self.add_book_Window.show()


class Borrow_win(QMainWindow):
    switch_to_main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400)
        self.mouse_on_row = 10000

    def con_func(self):
        self.button1.clicked.connect(self.select_ui)
        self.button2.clicked.connect(self.borrow)
        self.button3.clicked.connect(self.quit)

    # 传入user
    def init_user(self,user):
        self.user = user
        self.init_ui()

    def init_ui(self,condition = {}):
        self.book_info = select_by_multipy(condition)

        self.setWindowTitle('借书页面')

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        # 创建水平布局
        self.layout = QHBoxLayout()

        # 创建左侧垂直布局
        self.left_layout = QVBoxLayout()

        # 创建输入框和标签
        self.label1 = QLabel('书名:')
        self.label1.setFixedWidth(160)
        self.input1 = QLineEdit()
        self.input1.setFixedWidth(160)

        self.label2 = QLabel('出版社:')
        self.label2.setFixedWidth(160)
        self.input2 = QLineEdit()
        self.input2.setFixedWidth(160)

        self.label3 = QLabel('作者:')
        self.label3.setFixedWidth(160)
        self.input3 = QLineEdit()
        self.input3.setFixedWidth(160)

        self.label4 = QLabel('出版日期范围(小)')
        self.label4.setFixedWidth(160)
        self.input4 = QLineEdit()
        self.input4.setFixedWidth(160)

        self.label5 = QLabel('出版日期范围(大)')
        self.label5.setFixedWidth(160)
        self.input5 = QLineEdit()
        self.input5.setFixedWidth(160)

        self.left_layout.addWidget(self.label1)
        self.left_layout.addWidget(self.input1)
        self.left_layout.addWidget(self.label2)
        self.left_layout.addWidget(self.input2)
        self.left_layout.addWidget(self.label3)
        self.left_layout.addWidget(self.input3)
        self.left_layout.addWidget(self.label4)
        self.left_layout.addWidget(self.input4)
        self.left_layout.addWidget(self.label5)
        self.left_layout.addWidget(self.input5)

        # 创建按钮
        self.button1 = QPushButton('查询')
        self.button1.setFixedWidth(100)
        self.button2 = QPushButton('借阅')
        self.button2.setFixedWidth(100)
        self.button3 = QPushButton('退出')
        self.button3.setFixedWidth(100)

        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)

        # 创建右侧布局
        right_layout = QVBoxLayout()

        # 创建表格
        self.table = QTableWidget()
        self.table.setRowCount(len(self.book_info))
        self.table.setColumnCount(6)
        # 插入数据
        for row in range(len(self.book_info)):
            for col in range(6):
                item = QTableWidgetItem(f"{self.book_info[row][col]}")
                self.table.setItem(row, col, item)

        self.table.setHorizontalHeaderLabels(["BNAME", "publisher","AUTHOR","CDATE","CLASS" ,"counter"])

        # 设置表头自适应内容
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        right_layout.addWidget(self.table)

        # 将左右布局添加到总体布局中
        self.layout.addLayout(self.left_layout)
        self.layout.addLayout(right_layout)
        self.table.cellClicked.connect(self.on_cell_clicked)

        centralWidget.setLayout(self.layout)

        # 绑定函数
        self.con_func()

    def select_ui(self):
        limit_con = self.get_limit_condition() # 得到条件
        # 再次进行渲染
        self.init_ui(limit_con)

    # 得到限定条件
    def get_limit_condition(self):
        limit_con = {}
        BNAME = self.input1.text().strip()
        publisher = self.input2.text().strip()
        AUTHOR = self.input3.text().strip()
        PRO_DATE = self.input4.text().strip()
        LAS_DATE = self.input5.text().strip()
        con_list = [BNAME,publisher,AUTHOR,PRO_DATE,LAS_DATE]
        con_list_name = ["BNAME", "publisher", "AUTHOR", "PRO_DATE", "LAS_DATE"]

        # 进行判断
        for idx,i in enumerate(con_list):
            # 防止值为空
            if len(i) > 0 :
                if con_list_name[idx] in ["PRO_DATE", "LAS_DATE"]:
                    flag = judge_date(con_list[idx])

                    if not flag:
                        msg_box = QMessageBox(QMessageBox.Information, '提醒', '请正确输入日期!')
                        msg_box.exec_()
                        return {}

                limit_con[con_list_name[idx]] = i
        print(limit_con)
        return limit_con

    # 按照行借书
    def borrow(self):
        if  self.mouse_on_row >= len(self.book_info):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请选择要借书籍')
            msg_box.exec_()
            return

        # 得到对应的书名
        BNAME = self.book_info[self.mouse_on_row][0]
        self.user.borror_book(BNAME)
        self.init_ui() # 进行刷新


    def quit(self):
        self.switch_to_main.emit()

    def on_cell_clicked(self, row):
        self.mouse_on_row = row

class Send_win(QMainWindow):
    switch_to_Main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.mouse_on_row = 10000
        self.setGeometry(800, 300, 700, 300)

    # 必须得先传入user,才能进行展示
    def init_user(self,user):
        self.user = user
        self.initUI()

    # 初始化绑定函数
    def con_func(self):
        self.button1.clicked.connect(self.send_ui)
        self.button2.clicked.connect(self.quit)

    def on_cell_clicked(self, row):
        self.mouse_on_row = row

    def initUI(self):
        self.book_info = self.user.get_my_borrored_book()
        # 创建 QTableWidget 控件
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(len(self.book_info))
        self.tableWidget.setColumnCount(6)

        for row in range(len(self.book_info)):
            for col in range(6):
                item = QTableWidgetItem(f"{self.book_info[row][col]}")
                self.tableWidget.setItem(row, col, item)

        self.tableWidget.setHorizontalHeaderLabels(["BOOK_ID", "BNAME", "publisher", "AUTHOR", "CDATE", "CLASS"])
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)

        # 创建 QPushButton 按钮
        self.button1 = QPushButton("归还")
        self.button2 = QPushButton("退出")

        # 创建 QVBoxLayout 布局，并将表格和按钮添加进去
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # 创建一个 QWidget 来容纳整个布局，并将其设置为主窗口的中心部件
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setWindowTitle("借阅记录")
        self.con_func()

    def send_ui(self):
        if  self.mouse_on_row >= len(self.book_info):
            msg_box = QMessageBox(QMessageBox.Information, '提醒', '请选择要归还的书籍')
            msg_box.exec_()
            return
        # 得到目前鼠标获取的图书ID
        book_id = self.book_info[self.mouse_on_row][0]
        # 进行归还
        self.user.send_book(book_id)
        # 刷新UI界面
        self.initUI()

    # 跳转到主页面
    def quit(self):
        self.switch_to_Main.emit()


class Login_win(QWidget):
    switch_to_main = QtCore.pyqtSignal()
    switch_to_admin_main = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.con_func()

    def init_ui(self):
        login_filepath = os.path.join(dir, "UI_window/login.ui")
        self.loginWindow = uic.loadUi(login_filepath)
        self.radio_adm = self.loginWindow.radioButton
        self.radio_user = self.loginWindow.radioButton_2

        self.account_label = self.loginWindow.lineEdit
        self.passwd_label = self.loginWindow.lineEdit_2
        self.login_btn = self.loginWindow.pushButton
        self.exit_btn =self.loginWindow.pushButton_2

        # 设置基础样式
        self.account_label.setPlaceholderText("account")
        self.passwd_label.setPlaceholderText("passwd")
        self.passwd_label.setEchoMode(QLineEdit.Password)

    # 绑定槽函数
    def con_func(self):
        self.exit_btn.clicked.connect(self._exit)
        self.login_btn.clicked.connect(self._login)

    # 登录
    def _login(self):
        # 交叉一下。。。
        account = self.passwd_label.text().strip()
        pwd = self.account_label.text().strip()
        flag = "U"
        if self.radio_user.isChecked():
            self.user = Lib_User(pwd,account) # 创建用户对象
            flag = "U"
        elif self.radio_adm.isChecked():
            self.user = Lib_Manager(pwd, account)  # 创建管理员对象
            flag = "A"

        # 尝试登录
        self.user.login()
        time.sleep(1)

        if self.user.get_login_state():
            self.login_succ(True)
            if flag == "U":
                self.switch_to_main.emit()
            elif flag == "A":
                self.switch_to_admin_main.emit()
        else:
            self.login_succ(False)

    def get_User(self):
        try:
            return self.user
        except:
            pwd = self.passwd_label.text().strip()
            account = self.account_label.text().strip()
            self.user = Lib_User(pwd, account)  # 创建用户对象
            return self.user


    #  针对login的情况进行提示框
    def login_succ(self,flag):
        if flag == True:
            msg_box = QMessageBox(QMessageBox.Information, 'sign!', '登录成功')
            print("[log]login successfully!")
        else:
            msg_box = QMessageBox(QMessageBox.Information, 'sign!', '登录失败')
            print("[log]failed")
        msg_box.exec_()

    def close(self):
        self.loginWindow.close()

    def show(self):
        self.loginWindow.show()

    def _exit(self):
        QApplication.quit()



if __name__ == "__main__":
    pass