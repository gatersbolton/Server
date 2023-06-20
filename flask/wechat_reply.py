import library
import re
def handle(content):
    backupusername='2100160322'
    backuppassword='20030126Wxc'
    response=''
    bookhint='预约格式：输入“预约 [校区][楼层][座位号][开始时间]-[结束时间]”，比如“预约 武进3楼24号18：00-20：00”'
    if '取消预约' in content:
        spider = library.libspider(user=1)
        response = spider.Cancel()
    elif '预约状态' in content:
        spider = library.libspider(user=1)
        response = spider.BookStatus()
    elif content=='预约':
        response=bookhint
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
            floor = floor_match.group(1)
            # 提取座位号信息
            seat_pattern = re.compile(r'(\d+)号')
            seat_match = seat_pattern.search(s)
            seat = seat_match.group(1)
            # 提取开始时间和结束时间信息
            time_pattern = re.compile(r'(\d+)：(\d+)-(\d+)：(\d+)')
            time_match = time_pattern.search(s)
            starttime = float(time_match.group(1)) + float(time_match.group(2)) / 60.0
            endtime = float(time_match.group(3)) + float(time_match.group(4)) / 60.0
            print(campus, floor, seat, starttime, endtime)
            s=campus+floor+seat+str(starttime)+str(endtime)
            spider = library.libspider(user=1)
            response=spider.book(date='tomorrow',starttime=float(starttime),duration=float(endtime)-float(starttime),seat=int(seat),test=False)
        # except:
        #     response='预约格式错误！'+bookhint
    else:
        response=content
    return response

if __name__=="__main__":
    s="预约状态"
    print(handle(s))