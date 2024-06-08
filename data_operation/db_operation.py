from .db_init import *
# 创建books
def insert_book(BNAME, BOOK_ID,publisher,AUTHOR,CDATE,CLASS):
    FLAG = True # 默认没有借出
    # 提交数据
    data = [(BNAME, BOOK_ID,publisher,AUTHOR,CDATE,CLASS,FLAG)]
    sql_order = f"INSERT INTO BOOKS(BOOK_ID,BNAME,publisher,AUTHOR,CDATE,CLASS,FLAG) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    return execute_alert(sql_order,data)

# 删除书籍
def delete_book(BOOK_ID):
    # 删除与BOOK_ID有关的send记录
    sql_order1 = "DELETE FROM send_record WHERE BOOK_ID = '%s'"%(BOOK_ID)
    if not execute_alert(sql_order1,mul=False):
        return False

    # 删除与BOOK_ID有关的borrow记录
    sql_order2 = "DELETE FROM borrow_record WHERE BOOK_ID = '%s'" % (BOOK_ID)
    if not execute_alert(sql_order2,mul=False):
        return False

    # 删除与BOOK_ID有关的借书目录
    sql_order3 = "DELETE FROM borrowed_book WHERE BOOK_ID = '%s'" % (BOOK_ID)
    if not execute_alert(sql_order3,mul=False):
        return False

    # 删除books中对应的数目
    sql_order4 = "DELETE FROM books WHERE BOOK_ID = '%s'" % (BOOK_ID)
    if not execute_alert(sql_order4,mul=False):
        return False

    return True


# 创建users
def insert_user(SNAME,STU_ID,sex,birth):
    # 创建游标
    # 提交数据
    data = [(SNAME,STU_ID,sex,birth)]
    sql_order = f"INSERT INTO USERS(SNAME,STU_ID,sex,birth) VALUES (%s,%s,%s,%s);"
    return execute_alert(sql_order, data)

# 借书 单元操作
def borrow_operation(BNAME,STU_ID,DATE = None):
    '''
    :param BNAME:
    :param STU_ID:STU_ID注意一定是已经创建的USER表中的ID
    :return:
    '''

    # 先查询对应的书是否全借出
    sql_order = f"select BOOK_ID,FLAG from books WHERE FLAG = 1 and BNAME = \"{BNAME}\";"
    res = execute_select(sql_order)
    if len(res) < 1:# 没查到在场馆中的书
        print("[log]未查到在场馆中的书/此书不存在")
        return False
    # 已经查到了对应的书
    borr_id = res[0][0] # 取第一个书进行借出操作

    # ==============更改对应书目的flag==============
    sql_order = f"UPDATE books set FLAG = 0 WHERE BOOK_ID='%s';"%(borr_id)
    flag1 = execute_alert(sql_order,mul=False)

    if DATE == None:
        DATE = current_time()
    # ==============添加借出记录==============
    sql_order = f"INSERT INTO BORROW_RECORD(STU_ID,BOOK_ID,BDATE) VALUES ('%s','%s','%s');"%(STU_ID,borr_id,DATE)
    flag2 = execute_alert(sql_order,mul=False)

    # ==============添加借出书籍==============
    sql_order = f"INSERT INTO BORROWED_BOOK(BOOK_ID,STU_ID) VALUES ('%s','%s');" % (borr_id,STU_ID )
    flag3 = execute_alert(sql_order,mul=False)
    if flag1 and flag2 and flag3:
        print("[log]借书成功!")
    else:
        print("[log]借书失败...")


# 归还操作
def send_operation(BOOK_ID,STU_ID,DATE = None):
    # ==============将对应B_ID的书的FLAG更改==============
    sql_order = "UPDATE books set FLAG = 1 WHERE BOOK_ID='%s';"%(BOOK_ID)
    flag = execute_alert(sql_order,mul=False)
    if not flag:
        print(f"[err]{STU_ID} FLAG 更改错误!")
        return flag

    if DATE == None:
        DATE = current_time()
    # ==============在归还表中添加==============
    sql_order = f"INSERT INTO SEND_RECORD(STU_ID,BOOK_ID,BDATE) VALUES ('%s','%s','%s');"%(STU_ID,BOOK_ID,DATE)
    flag = execute_alert(sql_order, mul=False)
    if not flag:
        print(f"[err]{STU_ID} 归还表添加错误!")
        return flag

    # ===========删除出借表中的书==============
    sql_order = "DELETE  FROM BORROWED_BOOK WHERE BOOK_ID='%s' AND STU_ID = '%s' ;"%(BOOK_ID,STU_ID)
    flag = execute_alert(sql_order, mul=False)
    if not flag:
        print(f"[err]删除记录错误!")
        return flag
    print("归还成功！")

    return True



if __name__ == "__main__":
    # test
    # insert_book("葬爱","1003","人民出版社","花心","2022-3-2","爱情")
    # insert_user("刘翔","2021110751","男","2003-7-18")
    # print(borrow_operation("葬爱","2021110751"))
    # print(send_operation("1001","2021110751"))




    # _init_
    # book_info = [
    #     ("活着", "1011", "清华出版社", "MIke", "2003-3-2", "现实"),
    #     ("活着", "1012", "清华出版社", "MIke", "2003-3-2", "现实"),
    #     ("活着", "1013", "清华出版社", "MIke", "2003-3-2", "现实"),
    #     ("百年孤独", "1021", "哈工大出版社", "laohuang", "2003-3-1", "悲剧"),
    #     ("百年孤独", "1022", "哈工大出版社", "laohuang", "2003-3-1", "悲剧"),
    #     ("百年孤独", "1023", "哈工大出版社", "laohuang", "2003-3-1", "悲剧"),
    #     ("平凡的世界", "1031", "哈工大出版社", "John", "2005-3-2", "烂漫"),
    #     ("平凡的世界", "1032", "哈工大出版社", "John", "2005-3-2", "烂漫"),
    #     ("平凡的世界", "1033", "哈工大出版社", "John", "2005-3-2", "烂漫")
    # ]
    # for i in book_info:
    #     if not insert_book(*i):
    #         print("err")
    #         break

    pass






# 构建图书管理系统
# 具有如下表
# ------------Table------------
# BOOKS(
# BNAME 书籍名称
# BOOK_ID 图书编号 primary key
# publisher 出版商
# AUTHOR 作者名称
# CDATE 出版年月日
# CLASS 所属类别
# FLAG 借出是否
# )

# BORROW_RECORD(
# R_ID primary key
# STU_ID 借书人学号
# BOOK_ID 图书编号
# BDATE 借走的日期

# foreign key(STU_ID) references USERS(STU_ID)
# foreign key(BOOK_ID) references BOOKS(BOOK_ID)
# )

# SEND_RECORD(
# S_ID primary key
# STU_ID 归还人学号
# BOOK_ID 图书编号
# BDATE 归还的日期

# foreign key(STU_ID) references USERS(STU_ID)
# foreign key(BOOK_ID) references BOOKS(BOOK_ID)
# )

# USERS(
# SNAME 姓名
# STU_ID 学号 primary key
# BORROW_BOOKS 在借书籍编号
# foreign key(BORROW_BOOKS) references BOOKS(BOOK_ID)
# )
