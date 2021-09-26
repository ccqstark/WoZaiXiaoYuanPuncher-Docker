import datetime
from utils.sqlliteUtil import EasySqlite

username = input("请输入username:")

connection = EasySqlite("database.sqlite")
# 判断用户是否存在
result = connection.execute("select * from jwsession where username=?", [username])
if len(result) == 0:
    print("用户不存在！")
    choice = input("是否创建此用户(y/n):")
    if choice == 'y':
        jwsession = input("请输入jwsession:")
        connection.execute("insert into jwsession values (?,?,?,?)",
                           [username, jwsession,
                            datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d-%H-%M'), 1])
        print("创建用户成功！")
    else:
        print("操作取消")
else:
    # 用户如果存在则跟新jwsession
    jwsession = input("请输入jwsession:")
    connection.execute("update jwsession set jwsession=? where username=?", [jwsession, username])
    print("jwsession更新成功！")
