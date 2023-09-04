import library
import cczu_sql
import re
def handle(wechat_id,content):
    backupusername='2100160322'
    backuppassword='20030126Wxc'
    response=''
    hint='''常大助手使用方法：
    输入“预约 [校区][楼层][座位号][开始时间]-[结束时间]”，比如“预约 武进3楼24号18：00-20：00”
    输入“取消预约”，取消最近的预约
    输入“预约状态”，查看预约状态
    输入“快速预约”，按照上一次进行预约
    输入“绑定 [帐号] [密码] [校区]”，如“绑定 20440225 123456 西太湖”，绑定教务系统帐号
    输入“解绑”，解除绑定
    '''
    cczusql = cczu_sql.sql()
    try:
        username, password = cczusql.auto_login(wechat_id=wechat_id)
    except:
        username='none'
    if '解绑' in content:
        cczusql.del_by_wechatid(wechat_id=wechat_id)
        response='解绑成功！'
    elif '绑定' in content:
        username=content.split()[1]
        password=content.split()[2]
        campus=content.split()[3]
        if username=='superuser':
            response='管理员测试帐号'
            username=backupusername
            password=backuppassword
        cczusql.bind(wechat_id=wechat_id,username=username,password=password,campus=campus)
        response=response+'绑定成功！'
    else:
        if username=='none' and ('预约' in content or '取消' in content):
            response='您还没没有绑定教务系统，请绑定'
        elif '取消预约' in content:
            spider = library.libspider(username=username,password=password)
            response = spider.Cancel()
        elif '预约状态' in content:
            spider = library.libspider(username=username,password=password)
            response = spider.BookStatus()
        elif '快速预约' in content:
            # try:
                seat, floor, starttime, duration=cczusql.getpreference(wechat_id=wechat_id)
                spider = library.libspider(username=username,password=password)
                response = spider.book(date='tomorrow', starttime=float(starttime),
                                   duration=float(duration), seat=int(seat), test=False)
            # except:
            #     response = '快速预约失败！没有上一次预约的记录！'
        elif content=='预约':
            response=hint
        elif '预约' in content:
            # try:
                s = content
                # 提取校区信息
                campus_pattern = re.compile(r'预约\s+(.*?)\d+楼')
                campus_match = campus_pattern.search(s)
                campus = campus_match.group(1)
                # 提取楼层信息
                floor_pattern = re.compile(r'(\d+)楼')
                floor_match = floor_pattern.search(s)
                floor = str(floor_match.group(1))
                # 提取座位号信息
                seat_pattern = re.compile(r'(\d+)号')
                seat_match = seat_pattern.search(s)
                seat = seat_match.group(1)
                # 提取开始时间和结束时间信息
                time_pattern = re.compile(r'(\d+)：(\d+)-(\d+)：(\d+)')
                time_match = time_pattern.search(s)
                st = float(time_match.group(1)) + float(time_match.group(2)) / 60.0
                et = float(time_match.group(3)) + float(time_match.group(4)) / 60.0
                starttime=str(st)
                endtime=str(et)
                duration=float(et)-float(st)
                cczusql.setpreference(wechat_id=wechat_id, floor=floor, seat=str(seat), starttime=starttime, duration=str(duration))
                # s=campus+floor+seat+starttime+endtime
                spider = library.libspider(username=username,password=password)
                response=spider.book(date='tomorrow',starttime=st,duration=duration,seat=int(seat),test=False)
            # except:
            #     response='预约格式错误！'+bookhint
        else:
            response=hint
    return response

if __name__=="__main__":
    s="快速预约"
    print(handle('123456',s))