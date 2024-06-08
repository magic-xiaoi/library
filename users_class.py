from data_operation.db_init import  *
from data_operation.db_operation import borrow_operation,send_operation


def if_login(func):
    def wrapper(self, *args, **kwargs):
        if self.get_login_state():
            resp = func(self, *args, **kwargs)
            return resp
        else:
            print("[log]请先登录...")
    return wrapper

class Lib_Manager(object):
    def __init__(self,ADM_ID,ADM_NAME):
        self.ADM_ID = ADM_ID
        self.ADM_NAME = ADM_NAME
        self.__login_state = False

    def login(self):
        sql_order = "SELECT  ADM_NAME FROM  admin WHERE ADM_ID = '%s' " % (self.ADM_ID)
        res = execute_select(sql_order)
        if len(res) < 1:
            self.__login_state = False
            print("[log]登录失败...请重新登录")
            return

        elif res[0][0] == self.ADM_NAME:
            self.__login_state = True
            print("[log]登录成功!")
            return

        self.__login_state = False
        print("[log]登录失败...密码错误")
        return


    def get_login_state(self):
        return self.__login_state

class Lib_User(object):
    def __init__(self,STU_ID,SNAME):
        self.STU_ID = STU_ID
        self.SNAME = SNAME
        self.__login_state = False

    def login(self):
        sql_order = "SELECT  SNAME FROM  USERS WHERE STU_ID = '%s' "%(self.STU_ID)
        res = execute_select(sql_order)
        if len(res) < 1:
            self.__login_state = False
            print("[log]登录失败...请重新登录")
            return

        elif res[0][0] == self.SNAME:
            self.__login_state = True
            print("[log]登录成功!")
            return

        self.__login_state = False
        print("[log]登录失败...密码错误")
        return

    def get_login_state(self):
        return self.__login_state

    # 查看自己借阅的书，但是没有归还的书
    @if_login
    def get_my_borrored_book(self):
        sql_order = "SELECT BOOK_ID FROM borrowed_book WHERE STU_ID = '%s'"%(self.STU_ID)
        book_ids  = execute_select(sql_order)
        info = []
        for i in book_ids:
            sql_order = "SELECT BOOK_ID,BNAME,publisher,AUTHOR,CDATE,CLASS FROM books WHERE BOOK_ID = '%s'"%(i[0])
            res = execute_select(sql_order)
            info.append(res[0])
        return info

    # 还书
    @if_login
    def send_book(self,BOOK_ID):
        return send_operation(BOOK_ID,self.STU_ID)

    # 借书
    @if_login
    def borror_book(self,BNAME):
        return borrow_operation(BNAME,self.STU_ID)

    #

if __name__ == "__main__":
    # user = Lib_User("2021110751","刘翔")
    # user.login()
    # user.borror_book("葬爱")
    admin = Lib_Manager("admin","admin")
    admin.login()

# 基本功能实现
#1.实现用户登录(管理员登录、普通用户登录)

# 1.1 管理员功能
# 添加书籍 、 删除书籍 、添加用户、删除用户,查询所有记录

# 1.2 用户功能
# 借阅书籍、归还书籍 、 查阅图书馆书籍、查看目前还在借阅的书籍、
