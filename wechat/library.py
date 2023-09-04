import base64
import datetime
import re
import time
import requests
import argparse
# usernames = ['20416323', '20440213', '20440216']
# passwords = ['Xf552200.', 'Chenxt1668zz', 'Pyw12345']

class libspider:
    session=requests.Session()
    seat_map_wj3 = [0, 12551,12552,12553,12554,12555,12556,13363,13364,12560,12561,12562,12563,12564,12565,13365,13366,12569,12570,12571,16751,12573,12574,13367,13368,13369,13370,12584,12623,12659,12695,12624,12660,12696,12627,12663,12699,13355,13356,13357,13358,13359,13360,12632,12668,12704,12635,12671,12707,12636,12672,12708,12639,16760,12711,12640,12676,16757,12643,12679,12715,12644,12680,12716,16756,12683,12719,12648,12684,12720,12615,12651,12687,12723,12759,12795,12616,12652,12688,12724,12760,12796,12848,12884,12849,12885,12852,12888,12853,12889,12856,12892,12857,12893,12860,12896,12861,12897,12990,13026,12991,13027,12994,13030,12995,13031,12998,13034,12999,13035,13002,13038,13003,13039,13006,13042,13007,13043,13393,13236,13394,13395,13396,13373,13397,13392,13398,13245,13399,13390,13400,13379,13401,13382,13402,13253,13403,13385,13404,13258,13405,13388,]
    seat_map_xth3= [0, 41191, 41217, 41192, 41218, 41193, 41219, 41194, 41220, 41195, 41221, 41196, 41222, 41243, 41269, 41244, 41270, 41245, 41271, 41246, 41272, 41247, 41273, 41248, 41274, 41295, 41321, 41296, 41322, 41297, 41323, 41298, 41324, 41299, 41325, 41300, 41326, 41347, 41373, 41348, 41374, 41349, 41375, 41350, 41376, 41351, 41377, 41352, 41378, 41399, 41425, 41400, 41426, 41401, 41427, 41402, 41428, 41403, 41429, 41404, 41430, 41451, 41477, 41452, 41478, 41453, 41479, 41454, 41480, 41455, 41481, 41456, 41482, 41503, 41529, 41504, 41530, 41505, 41531, 41506, 41532, 41507, 41533, 41508, 41534, 41555, 41581, 41556, 41582, 41557, 41583, 41558, 41584, 41559, 41585, 41560, 41586, 41607, 41633, 41608, 41634, 41609, 41635, 41610, 41636, 41611, 41637, 41612, 41638, 41659, 41685, 41660, 41686, 41661, 41687, 41662, 41688, 41663, 41689, 41664, 41690, 41711, 41737, 41712, 41738, 41713, 41739, 41714, 41740, 41715, 41741, 41716, 41742, 41763, 41789, 41764, 41790, 41765, 41791, 41766, 41792, 41767, 41793, 41768, 41794, 41815, 41841, 41816, 41842, 41817, 41843, 41818, 41844, 41819, 41845, 41820, 41846, 41867, 41893, 41868, 41894, 41869, 41895, 41870, 41896, 41871, 41897, 41872, 41898, 41919, 41945, 41920, 41946, 41921, 41947, 41922, 41948, 41923, 41949, 41924, 41950, 41355, 41381, 41356, 41382, 41357, 41383, 41358, 41384, 41407, 41433, 41408, 41434, 41409, 41435, 41410, 41436, 41459, 41485, 41460, 41486, 41461, 41487, 41462, 41488, 41511, 41537, 41512, 41538, 41513, 41539, 41514, 41540, 41563, 41589, 41564, 41590, 41565, 41591, 41566, 41592, 41615, 41641, 41616, 41642, 41617, 41643, 41618, 41644, 41667, 41693, 41668, 41694, 41669, 41695, 41670, 41696, 41719, 41745, 41720, 41746, 41721, 41747, 41722, 41748, 41771, 41797, 41772, 41798, 41773, 41799, 41774, 41800, 41823, 41849, 41824, 41850, 41825, 41851, 41826, 41852, 41875, 41901, 41876, 41902, 41877, 41903, 41878, 41904, 41927, 41953, 41928, 41954, 41929, 41955, 41930, 41956, 41413, 41439, 41414, 41440, 41465, 41491, 41466, 41492, 41517, 41543, 41518, 41544, 41569, 41595, 41570, 41596, 41621, 41647, 41622, 41648, 41673, 41699, 41674, 41700, 41725, 41751, 41726, 41752, 41777, 41803, 41778, 41804, 41829, 41855, 41830, 41856, 41881, 41907, 41882, 41908, 41933, 41959, 41934, 41960, 41209, 41235, 41210, 41236, 41211, 41237, 41212, 41238, 41213, 41239, 41214, 41240, 41261, 41287, 41262, 41288, 41263, 41289, 41264, 41290, 41265, 41291, 41266, 41292, 41313, 41339, 41314, 41340, 41315, 41341, 41316, 41342, 41317, 41343, 41318, 41344, 41365, 41391, 41366, 41392, 41367, 41393, 41368, 41394, 41369, 41395, 41370, 41396, 41417, 41443, 41418, 41444, 41419, 41445, 41420, 41446, 41421, 41447, 41422, 41448, 41469, 41495, 41470, 41496, 41471, 41497, 41472, 41498, 41473, 41499, 41474, 41500, 41521, 41547, 41522, 41548, 41523, 41549, 41524, 41550, 41525, 41551, 41526, 41552, 41573, 41599, 41574, 41600, 41575, 41601, 41576, 41602, 41577, 41603, 41578, 41604, 41625, 41651, 41626, 41652, 41627, 41653, 41628, 41654, 41629, 41655, 41630, 41656, 41677, 41703, 41678, 41704, 41679, 41705, 41680, 41706, 41681, 41707, 41682, 41708, 41729, 41755, 41730, 41756, 41731, 41757, 41732, 41758, 41733, 41759, 41734, 41760, 41303, 41329, 41304, 41330, 41305, 41331, 41306, 41332, 41309, 41335, 41310, 41336, 41361, 41387, 41362, 41388]

    usernames = ['20440225', '2100160322', '20440217']
    passwords = ['Amelia,520', '20030126Wxc', 'Scr1028scr']
    weekday_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    campus='xth'
    st=''
    def __init__(self,user=-1,username='',password='',test=False):
        libspider.session=requests.Session()
        if user >= 0 :
            username=libspider.usernames[user]
            password=libspider.passwords[user]
        i0 = libspider.session.get(
            url='http://zuowei.cczu.edu.cn/login',
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        i1 = libspider.session.get(
            url='http://sso.cczu.edu.cn/sso/login?service=http://zuowei.cczu.edu.cn/cas',
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        if test:
            pass
            # print(i1.text)
        i1txt = i1.text

        reg = re.compile(r'name="lt" value=".*"')
        match = reg.search(i1txt)
        start = match.start();
        end = match.end();
        lt = i1txt[start + 17:end]
        lt = lt.strip('>');
        lt = lt.strip('/');
        lt = lt.strip('"');
        reg = re.compile(r'name="execution" value=".*"')
        match = reg.search(i1txt)
        execution = match[0][24:-1]
        # 获取jlibspider.sessionid
        ijsid = libspider.session.post(url='https://webvpn.cczu.edu.cn/webvpn/getcookie?domain=sso.cczu.edu.cn')
        jsidtxt = ijsid.text
        reg = re.compile(r'"Jlibspider.sessionID":"[a-zA-Z0-9]*"')
        match = reg.findall(jsidtxt)
        # jlibspider.sessionid = match[0][14:-1]
        b64password = base64.b64encode(password.encode()).decode()
        i2 = libspider.session.post(
            url="http://sso.cczu.edu.cn/sso/login?service=http://zuowei.cczu.edu.cn/cas",
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
            data={
                'username': username,
                'password': b64password,
                'lt': lt,
                'execution': execution,
                '_eventId': 'submit'
            },
        )
        if test:
            pass
            print(username)
            print(b64password)
            print(lt)
            print(execution)
            print(i2.text)

        i3 = libspider.session.post(
            url="https://zmvpn.cczu.edu.cn/http/webvpn4578b329feda6a5f6cc5a9222350e3b0/sso/login?service=http://zuowei.cczu.edu.cn/cas",
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        if test:
            pass
            # print(i3.text)
        i4 = libspider.session.get(
            url="http://zuowei.cczu.edu.cn/",
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        if test:
            print(i4.text)
        tokentext = i4.text
        reg = re.compile(r'name="SYNCHRONIZER_TOKEN" value=".*?"')
        match = reg.search(tokentext)
        libspider.st = match[0][33:-1]
        # print(match[0])
        # print(libspider.st)

    def book(self,date='today',starttime=18.5,duration=4.0,seat=1,campus='xth',floor=3,test=False):
        self.campus=campus
        seatmap=1
        if campus == 'wj':
            seatmap = libspider.seat_map_wj3[seat]
        if campus == 'xth':
            if floor == 3:
                seatmap = libspider.seat_map_xth3[seat]
        seatmap=str(seatmap)
        print('booking',date,starttime,duration,seat)
        log='预约成功！'
        endtime=starttime+duration
        #判断周六
        today = datetime.date.today()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        if date == 'today': whichday = today
        if date == 'tomorrow': whichday = tomorrow
        weekday = whichday.today().weekday()
        if libspider.weekday_str[weekday] == 'Saturday' and endtime == 17.0:
            endtime = 16.5
            if not test:
                print(">>>>由于今天周六，下午四点半需要打扫，请注意哦！<<<<")
        i4=libspider.session.get('http://zuowei.cczu.edu.cn/map')
        tokentext = i4.text
        reg = re.compile(r'name="SYNCHRONIZER_TOKEN" value=".*?"')
        match = reg.search(tokentext)
        libspider.st = match[0][33:-1]
        i5 = libspider.session.post(
            url="http://zuowei.cczu.edu.cn/selfRes",
            data={
                'SYNCHRONIZER_TOKEN': libspider.st,
                'SYNCHRONIZER_URI': '/map',
                'date': str(whichday),
                'seat': seatmap,
                'start': str(int(starttime * 60)),
                'end': str(int(endtime * 60)),
                'authid': '-1'
            }
        )
        # print(i5.text)
        if test:
            print(i5.text)


        match = re.search(r"预约失败，请尽快选择其他时段或座位", i5.text)
        while match:
            seat=seat+1
            i4 = libspider.session.get('http://zuowei.cczu.edu.cn/map')
            tokentext = i4.text
            reg = re.compile(r'name="SYNCHRONIZER_TOKEN" value=".*?"')
            match = reg.search(tokentext)
            libspider.st = match[0][33:-1]
            i4 = libspider.session.get(
                url="http://zuowei.cczu.edu.cn/cas?ticket=" + libspider.st,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
            )
            # print(i4.text)
            if test:
                print(i4.text)

            i4txt = i4.text
            reg = re.compile(r'name="SYNCHRONIZER_TOKEN" value=".*?"')
            match = reg.search(i4txt)
            st = match[0][33:-1]
            # print(seat)
            i5 = libspider.session.post(
                url="http://zuowei.cczu.edu.cn/selfRes",
                data={
                    'SYNCHRONIZER_TOKEN': st,
                    'SYNCHRONIZER_URI': '/map',
                    'date': str(whichday),
                    'seat': seatmap,
                    'start': str(int(starttime * 60)),
                    'end': str(int(endtime * 60)),
                    'authid': '-1'
                }
            )
            if test:
                print(i5.text)
            match = re.search(r"预约失败，请尽快选择其他时段或座位", i5.text)
            if match is None:
                if not test:
                    log=log+'座位已被预约，自动修改为  ' + str(seat) + '  号位置。\n'
                break
        return log
    def ChangeSeat(self,user):
        log, date, starttime, duration, seat, cancelable = self.Cancel(True)
        newspider=libspider(user)
        newspider.book(date,starttime,duration,seat)
    def BookStatus(self):
        log, date, start_time, duration,seat,cancelable=self.Cancelornot(realcancel=False)
        if date==-1:
            return ''
        st=str(int(start_time))+':'+str(int((start_time-int(start_time))*60))
        start_time=start_time+duration
        et=str(int(start_time))+':'+str(int((start_time-int(start_time))*60))
        if date == 'today':date='今天'
        else: date='明天'
        if cancelable:
            log='当前预约：'+date+st+'-'+et+'座位号'+str(seat)
        else:
            log='当前没有预约。'
        return log
    def Cancel(self):
        log, date, start_time, duration,seat,cancelable=self.Cancelornot(realcancel=True)
        return log
    def Cancelornot(self,realcancel=True,test=False):
        log=""
        i6 = libspider.session.get(
            url="http://zuowei.cczu.edu.cn/history?type=SEAT",
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        tokentext = i6.text
        reg = re.compile(r'name="SYNCHRONIZER_TOKEN" value=".*?"')
        match = reg.search(tokentext)
        libspider.st = match[0][33:-1]
        if test:
            print(i6.text)
        if self.campus == 'xth':
            pattern = r"<a onclick=\"MyDoSubmit\('(\d+)'"
            result = re.findall(pattern, i6.text)
            pattern2 = r'style="font-weight: bold">(.*?)</dt>'
            result2 = re.findall(pattern2, i6.text)
            pattern3 = r'东南角三楼(\d+)'
            result3 = re.findall(pattern3, i6.text)
            if test:
                if result:print(result[-1])
                if result2:print(result2[-1])
                if result3:print(result3[-1])
            if not result:
                log=log+"没有预约，无法取消！\n"
            date="today"
            if "明" in result2[-1]: date="tomorrow"
            match = re.search(r"(\d+):(\d+)", result2[-1])
            if match:
                start_hour = int(match.group(1))
                start_min = int(match.group(2))
                start_time = start_hour + start_min / 60.0
            match = re.search(r"-- (\d+):(\d+)", result2[-1])
            if match:
                end_hour = int(match.group(1))
                end_min = int(match.group(2))
                duration = (end_hour + end_min / 60.0) - start_time
            seat=int(result3[-1])
            if result and realcancel:
                if test:
                    pass
                    # print(url)
                # "http://zuowei.cczu.edu.cn/reservation/cancel/1665014"
                i7 = libspider.session.post(
                    url='http://zuowei.cczu.edu.cn/reservation/cancel',
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                    },
                    data={
                        'SYNCHRONIZER_TOKEN': libspider.st,
                        'SYNCHRONIZER_URI': '/history',
                        'id': result[-1],
                    }
                )
                if test:
                    data = {
                        'SYNCHRONIZER_TOKEN': libspider.st,
                        'SYNCHRONIZER_URI': '/',
                        'id': result[-1],
                    }
                    print(data)
                    print(i7.text)
            cancelable=False
            if result and realcancel: log="取消成功！"
            if result and not realcancel: cancelable=True
        if self.campus == 'wj':
            pattern = r'/reservation/cancel/(\d+)'
            result = re.findall(pattern, i6.text)
            pattern2 = r'style="font-weight: bold">(.*?)</dt>'
            result2 = re.findall(pattern2, i6.text)
            pattern3 = r'区三楼阅读空间(\d+)'
            result3 = re.findall(pattern3, i6.text)
            if test:
                if result:print(result[-1])
                if result2:print(result2[-1])
                if result3:print(result3[-1])
            if not result:
                log=log+"没有预约，无法取消！\n"
            date="today"
            if "明" in result2[-1]: date="tomorrow"
            match = re.search(r"(\d+):(\d+)", result2[-1])
            if match:
                start_hour = int(match.group(1))
                start_min = int(match.group(2))
                start_time = start_hour + start_min / 60.0
            match = re.search(r"-- (\d+):(\d+)", result2[-1])
            if match:
                end_hour = int(match.group(1))
                end_min = int(match.group(2))
                duration = (end_hour + end_min / 60.0) - start_time
            seat=int(result3[-1])
            if result and realcancel:
                url = 'http://zuowei.cczu.edu.cn/reservation/cancel/' + str(result[-1])
                if test:
                    print(url)
                # "http://zuowei.cczu.edu.cn/reservation/cancel/1665014"
                i7 = libspider.session.post(
                    url='http://zuowei.cczu.edu.cn/reservation/cancel',
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                    },
                    data={
                        'SYNCHRONIZER_TOKEN': libspider.st,
                        'SYNCHRONIZER_URI': '/',
                        'id': result[-1],
                    }
                )
                if test:
                    print(i7.text)
            cancelable=False
            if result and realcancel: log="取消成功！"
            if result and not realcancel: cancelable=True
        return log, date, start_time, duration,seat,cancelable

# library.py -t 18.5 -d 0 -s 2 -a 0

if __name__ == "__main__":
    s=libspider(user=1)
    print(s.BookStatus())
    print(s.Cancel())
    print(s.book(date='tomorrow',starttime=13,duration=4.0,seat=123,campus='xth',floor=3))
    print(s.BookStatus())
    # s.ChangeSeat(user=1)
    # print(log,date,starttime,duration,seat)


    # parser = argparse.ArgumentParser(description='图书馆预约程序')
    # parser.add_argument('-t', '--time', help='预约开始时间，接受小数，24小时制', required=False)
    # parser.add_argument('-e', '--endtime', help='预约结束时间，接受小数，24小时制', required=False)
    # parser.add_argument('-d', '--date', help='日期，0今天，1明天', required=False)
    # parser.add_argument('-s', '--seat', help='座位号，只支持3楼', required=False)
    # parser.add_argument('-a', '--account', help='使用系统中的哪个帐号，123表示', required=False)
    # parser.add_argument('-c', '--cancel', help='取消预约', required=False)
    # parser.add_argument('-u', '--use', help='转移到大号使用', required=False)
    # args = vars(parser.parse_args())
    # arg_t = args['time']
    # arg_d = args['date']
    # arg_s = args['seat']
    # arg_a = args['account']
    # arg_c = args['cancel']
    # date = 'today';
    # i = int(arg_a)
    # if arg_c is None:
    #     if arg_d=='1': date='tomorrow'
    #     libspider(mode='book',date=date,starttime=float(arg_t),endtime=float(arg_t)+4,username=usernames[i],password=passwords[i],index=i,seat=seat_index.index(int(arg_s)))
    # else:
    #     libspider("cancel", username=usernames[i], password=passwords[i], index=i)


