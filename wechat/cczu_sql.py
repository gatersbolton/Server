import os
import sqlite3

class sql:
    sqlfile = 'cczu.db'  # 数据库的名字
    def __init__(self):
        self.initsql()
        pass
    # 参数全是字符串
    # 几个数据表：
    # users(wechat_id,username,password)
    # preference(wechat_id,floor,seat,starttime,duration)
    def initsql(self):
        # 不是__init__这个生成函数
        # 初始化，建数据库，建表y之类的，总共只要用一次
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        # 连接到数据库，如果不存在则会自动创建
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        # 创建用户表
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        wechat_id TEXT PRIMARY KEY NOT NULL,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL,
                        campus TEXT NOT NULL,
                        seat TEXT,
                        floor TEXT,
                        starttime TEXT,
                        duration TEXT
                    )''')
        conn.commit()
        conn.close()
    def auto_login(self, wechat_id):
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        # 查询 users 表
        c.execute("SELECT username,password FROM users WHERE wechat_id=?", (wechat_id,))
        result = c.fetchone()
        conn.close()
        # 处理结果
        if result is not None:
            username, password = result
        else:
            username = 'none';
            password = 'none';
        return username, password

    def bind(self, wechat_id, username, password, campus):
        """添加 (wechat_id, username, password) 到 users 表，并添加对应的偏好表项，初值全是字符串的 'none'"""
        # 连接到数据库
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        # 添加用户信息到 users 表
        c.execute("INSERT INTO users (wechat_id, username, password,campus, seat, floor, starttime, duration) VALUES (?, ?, ?, ?, ?, ?, ? ,?)", (wechat_id, username, password,campus, 'none', 'none', 'none', 'none'))
        conn.commit()
        conn.close()
    def getcampus(self,wechat_id):
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()

        # 查询 preference 表
        c.execute("SELECT campus FROM users WHERE wechat_id=?", (wechat_id,))
        result = c.fetchone()
        conn.close()
        campus=type(result)
        return campus
    def getpreference(self, wechat_id):
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()

        # 查询 preference 表
        c.execute("SELECT floor, seat, starttime, duration FROM users WHERE wechat_id=?", (wechat_id,))
        result = c.fetchone()
        conn.close()
        # 处理结果
        if result is not None:
            floor, seat, starttime, duration = result
        else:
            seat = '1'
            floor = 'none';
            starttime = '18.0';
            duration = '4.0';

        return seat, floor, starttime, duration

    # 查wechat_id对应的preference表，返回
        # return wechat_id,floor,seat,starttime,duration

    def setpreference(self, wechat_id, floor='none', seat='none', starttime='none', duration='none'):
        # 参数可缺省，默认为字符串的"none"
        # 连接到数据库
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()

        # 修改 preference 表
        c.execute("UPDATE users SET floor=?, seat=?, starttime=?, duration=? WHERE wechat_id=?",
                  (floor, seat, starttime, duration, wechat_id))
        conn.commit()
        conn.close()
        # 修改preference表里的对应项
    def select_all(self):
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        # 查询 users 表
        c.execute("SELECT * FROM users")
        result = c.fetchall()
        conn.close()
        return result

    def del_by_wechatid(self,wechat_id):
        # 建立数据库连接并获取游标对象
        conn = sqlite3.connect(self.sqlfile)
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE wechat_id=?", (wechat_id,))
        # 提交更改并关闭连接
        conn.commit()
        conn.close()


if __name__ == '__main__':
    cczusql = sql()
    cczusql.initsql()
    print(cczusql.getpreference('123456'))
    # cczusql.select_all()
    wechat_id='123456'
    # cczusql.bind(wechat_id=wechat_id,username='123123',password='abcabc',campus='xth')
    # cczusql.setpreference(wechat_id=wechat_id,seat='18',starttime='18.5',duration='3')
    print(cczusql.getcampus('123456'))
    # username, password = cczusql.auto_login(wechat_id=wechat_id)

    # cczusql.del_by_wechatid(wechat_id=wechat_id)
    # if (username == 'none'):
    #     username = '12345678'
    #     password = '123456'
    #     cczusql.bind(wechat_id=wechat_id, username=username, password=password)

    # os.remove(cczusql.sqlfile)
    # print(username, password)
    print(cczusql.select_all())