from .db_init import *

# 根据book_dict生成WHERE sql语句
def gen_condition_sql(book_dict,date_name = "CDATE"):
    sql_order_next = "WHERE "
    # 先遍历所有值,确定日期范围(日期范围用[PRO_DATE,LAS_DATE]进行表示)
    DATE_list = []  # 存储日期
    for i in book_dict.keys():
        if i in ["PRO_DATE", "LAS_DATE"]:
            DATE_list.append(i)
    if len(DATE_list) == 0:
        pass
    elif len(DATE_list) == 1:
        if DATE_list[0] == "PRO_DATE":
            sql_order_next += f"'%s' <= {date_name} AND " % (book_dict[DATE_list[0]])
        else:
            sql_order_next += f" {date_name} <= '%s'  AND " % (book_dict[DATE_list[0]])
    elif len(DATE_list) == 2:
        sql_order_next += f" {date_name} BETWEEN '%s' AND '%s' AND" % (book_dict["PRO_DATE"], book_dict["LAS_DATE"])

    #  判断是否还有限制条件
    if len(book_dict.keys()) - len(DATE_list) > 0:
        for idx, key in enumerate(book_dict.keys()):
            if key not in ["PRO_DATE", "LAS_DATE"]:
                sql_order_next += f"{key} =\'{book_dict[key]}\' AND "
        # 删除AND
    sql_order_next = sql_order_next[:-4]
    return sql_order_next

def select_by_multipy_and_id(book_dict,table = "books"):
    '''
        :param book_dict: 字典类型数据
        :return:
        '''

    sql_order_front = f"SELECT * FROM {table} "
    sql_order_next = "WHERE "
    if len(book_dict.keys()) == 0:
        return execute_select(sql_order_front )

    if table ==  "books":
        sql_order_next = gen_condition_sql(book_dict)
    else:
        sql_order_next = gen_condition_sql(book_dict,date_name="BDATE")

    sql_order = sql_order_front + sql_order_next
    return execute_select(sql_order)


# 书籍复合查询操作
def select_by_multipy(book_dict):
    '''
    :param book_dict: 字典类型数据
    :return:
    '''

    sql_order_front = "SELECT a.BNAME, publisher,AUTHOR,CDATE,CLASS ,counter FROM (SELECT DISTINCT BNAME, publisher,AUTHOR,CDATE,CLASS FROM  books "
    sql_order_next = "GROUP BY BOOK_ID) AS a,(SELECT BNAME,COUNT(BOOK_ID) AS counter FROM books WHERE FLAG = 1  GROUP BY BNAME) AS b WHERE a.BNAME = b.BNAME"
    if len(book_dict.keys()) == 0:
        return execute_select(sql_order_front + sql_order_next)

    sql_order = gen_condition_sql(book_dict)

    sql_order = sql_order_front + sql_order + sql_order_next
    return execute_select(sql_order)

# # 查询不重复元素操作(用于后续UI菜单)
# def select_distinct_element(element,table):
#     sql_order  = f"SELECT DISTINCT {element} FROM {table}"
#     return execute_select(sql_order)

if __name__ == "__main__":
    # print(select_by_multipy({"PRO_DATE":"2000-1-1"}))
    # print(select_by_multipy_and_id({"PRO_DATE":"2000-1-1","BNAME":"葬爱"}))
    print(select_by_multipy({"PRO_DATE":"2000-1-1"}))