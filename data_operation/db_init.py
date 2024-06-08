import pymysql
import time

# 连接数据库
db=pymysql.connect(
        #本机使用localhost，服务器使用ip地址
        host='localhost',
        #用户名，如变动请按变动后修改
        user='root',
        #密码，如变动请按变动后修改
        password='1234',
        #数据库名，如变动请按变动后修改
        database='library')

# 进行日期格式检查
def judge_date(date):
    date_info = date.split("-")
    # 如果日期不是三个部分，则错误
    if len(date_info) != 3:
        return False

    for idx,info in enumerate(date_info):
        try:
            d = int(info)
            if d > 0:
                if idx == 1:# 月份
                    if d <=0 or d >=13:
                        return False

                if idx == 2:# 日
                    if d <=0 or d >=32:
                        return False
            else:
                return  False

        except:
            return False

    return True


def current_time():
    # 获取当前时间的时间戳
    timestamp = time.time()
    # 将时间戳转换为 struct_time 对象
    local_time = time.localtime(timestamp)
    # 格式化输出年月日
    formatted_date = time.strftime("%Y-%m-%d", local_time)
    return formatted_date

# 插入操作执行单元
def execute_alert(sql,data = None,mul = True,debug = False):
    cursor = db.cursor()
    if not debug:
        try:
            if mul:
                cursor.executemany(sql, data)
                db.commit()
                return True

            elif (not mul) and data==None:
                cursor.execute(sql)
                db.commit()
                return True
        except:
            db.rollback()
            return False
    else:
        if mul:
            cursor.executemany(sql, data)
            db.commit()
            return True

        elif (not mul) and data == None:
            cursor.execute(sql)
            db.commit()
            return True

# 查询操作单元
def execute_select(sql):
    cursor = db.cursor()
    cursor.execute(sql)
    rest = cursor.fetchall()
    return rest

if __name__ == "__main__":
    print(judge_date("2022-44-112"))