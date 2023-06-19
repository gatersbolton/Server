import sqlite3

#用sqlite3进行一些数据库操作
class sql:
    sqlfile='cczu.db'#数据库的名字
    # 参数全是字符串
    # 几个数据表：
    # users(wechat_id,username,password)
    # preference(wechat_id,floor,seat,starttime,duration)
    def init(self):
        #不是__init__这个生成函数
        # 初始化，建数据库，建表之类的，总共只要用一次
        pass
    def auto_login(self,wechat_id):
        pass
        #查users表是否有wechat_id=wechat_id的条目
        if True:
            username='20410000';password='123456';#这里设置成表里查到的
            return username,password
        else:
            username = 'none';password = 'none';
            return username,password

    def bind(self,wechat_id, username,password):
        pass
        #添加users(wechat_id, username,password)到表里，并添加preference(wechat_id,floor,seat,starttime,duration)，初值全是字符串的'none'

    def getpreference(self,wechat_id):
        pass
        #查wechat_id对应的preference表，返回
        #return wechat_id,floor,seat,starttime,duration

    def setpreference(self,wechat_id,floor,seat,starttime,duration):
        #参数可缺省，默认为字符串的"none"
        pass
        #修改preference表里的对应项

if __name__=='__main__':
    # 示例：
    cczusql=sql
    cczusql.init()
    username,password=cczusql.auto_login(wechat_id='1234567890abcdefg')
    if(username=='none'):
        username='12345678'
        password='123456'
        cczusql.bind(wechat_id='1234567890abcdefg',username=username,password=password)
    # preference也类似
