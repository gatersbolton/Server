from Crypto.Cipher import AES
from bs4 import BeautifulSoup
import lxml
import re
import requests
import base64
import xlrd,xlwt
import json
import smtplib
from email.mime.text import MIMEText
import time
import library
class CCZUVPN(object):
    session = requests.Session()
    realcookie=''
    # xlrownumber=0
    mode=False
    username=''
    password=''
    def aes_encrypt(self,data,key,iv):
        BLOCK_SIZE = 16
        from base64 import b64encode
        AES_KEY =key.encode()
        AES_IV = iv.encode()
        cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)
        x = data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(data) % BLOCK_SIZE)
        x = x.encode()
        e = b64encode(cipher.encrypt(x))
        return str(e, encoding='utf8')
    def __init__(self):
        pass
    def Login(self,username,password,mode='none'):
        CCZUVPN.username=username
        CCZUVPN.password=password
        password0=password
        CCZUVPN.mode=mode
        if (CCZUVPN.mode == 'status'): print('\n'+username, end=':')
        CCZUVPN.session = requests.Session()

        if (CCZUVPN.mode == 'status'): print('4', end='')
        i1 = CCZUVPN.session.get(
            url='https://zmvpn.cczu.edu.cn/http/webvpn4578b329feda6a5f6cc5a9222350e3b0/sso/login',
            headers={
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
            },
        )
        soup1 = BeautifulSoup(i1.text, 'lxml')

        i1txt=i1.text
        soup1 = BeautifulSoup(i1txt, 'html.parser')
        reg=re.compile(r'name="lt" value=".*"')
        match=reg.search(i1txt)
        start=match.start();end=match.end();
        lt=i1txt[start+17:end]
        lt=lt.strip('>');lt=lt.strip('/');lt=lt.strip('"');
        reg=re.compile(r'name="execution" value=".*"')
        match=reg.search(i1txt)
        execution=match[0][24:-1]

        #获取jsessionid
        ijsid=CCZUVPN.session.post(url='https://webvpn.cczu.edu.cn/webvpn/getcookie?domain=sso.cczu.edu.cn')
        reg = re.compile(r'"JSESSIONID":"[a-zA-Z0-9]*"')
        b64password=base64.b64encode(password0.encode()).decode()

        #post第二个登录页面的用户名密码
        if (CCZUVPN.mode == 'status'):
            print('打开界面', end=' ')
        if (CCZUVPN.mode=='test'):
            print('打开界面')
            print(soup1)
        i2 = CCZUVPN.session.post(
            url="https://zmvpn.cczu.edu.cn/http/webvpn4578b329feda6a5f6cc5a9222350e3b0/sso/login?service=http%3A%2F%2Fywtb.cczu.edu.cn%2Fpc%2Findex.html",
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
        if(CCZUVPN.mode=='status'):
            print('点击登录按钮',end=' ')
        if(CCZUVPN.mode=='test'):
            print('点击登录按钮')
            print(username)
            print(password)
            print(lt)
            print(execution)
            soup2 = BeautifulSoup(i2.text, 'lxml')
            print(soup2)
        i2nxt=CCZUVPN.session.get(
            url='https://zmvpn.cczu.edu.cn/http/webvpnb4628df0d7b77a6d0f08dfc00aa8d59c2c964ac696c57b03b13c3b6f0ee2cb8c/pc/index.html',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },
        )
        if(CCZUVPN.mode=='test'):
            print(i2nxt.text)
        i2nxt2 = CCZUVPN.session.get(
            url='https://zmvpn.cczu.edu.cn/http/webvpnb4628df0d7b77a6d0f08dfc00aa8d59c2c964ac696c57b03b13c3b6f0ee2cb8c/pc/myHome.html',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            },
        )
        if (CCZUVPN.mode == 'test'):
            print(i2nxt2.text)
        return ('自定义工作台' in i2nxt2.text)

    #教务管理信息系统
    class Portal:
        row_number=0
        def __init__(self):
            #教务管理系统按钮的快速重定向
            i3pre=CCZUVPN.session.get(
                url='https://zmvpn.cczu.edu.cn/http/webvpnb4628df0d7b77a6d0f08dfc00aa8d59c2c964ac696c57b03b13c3b6f0ee2cb8c/ydmh/api/clickYy?yyid=9a3222874dbe467c87342f2586c8d345&enlink-vpn',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                },
            )
            if (CCZUVPN.mode == 'status'): print('教务系统重定向', end='')
            if (CCZUVPN.mode == 'test'):
                print('教务系统重定向')
                print(i3pre.text)
            i3loginpage=CCZUVPN.session.get(
                url='https://zmvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/loginN.aspx',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                }
            )
            i3txt=i3loginpage.text
            regvs = re.compile(r'STATE" value=".*?"')
            matchvs = regvs.search(i3txt)
            vs=matchvs[0][14:-1]
            regvsg = re.compile(r'RATOR" value=".*?"')
            matchvsg = regvsg.search(i3txt)
            vsg=matchvsg[0][14:-1]
            if(CCZUVPN.mode=='test'):
                print(vs)
                print(vsg)

            i3pre2 = CCZUVPN.session.post(
                url='https://zmvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/loginN.aspx',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                },
                data={
                    '__VIEWSTATE':vs,
                    '__VIEWSTATEGENERATOR':vsg,
                    'username': CCZUVPN.username,
                    'userpasd': CCZUVPN.password,
                    'btLogin': '登录',
                }
            )
            if (CCZUVPN.mode == 'status'): print('教务系统登录', end='')
            if (CCZUVPN.mode == 'test'):
                print('教务系统登录')
                print(i3pre2.text)
            i3 = CCZUVPN.session.get(
                url='https://zmvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/View/indexTablejw.aspx',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                },
            )
            if (CCZUVPN.mode=='test'):
                print('进入教务系统')
                soup3 = BeautifulSoup(i3.text, 'lxml')
                print(soup3)
            if (CCZUVPN.mode == 'status'): print('进入教务系统', end=' ')

        #查询成绩
        def GetScore(self):
            if (CCZUVPN.mode == 'status'): print('查分', end=' ')
            i4 = CCZUVPN.session.get(
                url='https://zmvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/web_cjgl/cx_cj_xh.aspx',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
               },
            )
            soup4 = BeautifulSoup(i4.text, 'lxml')
            data = soup4.find_all(class_='dg1-item')
            if (CCZUVPN.mode=='test1'):
                print('学生所学成绩')
                print(soup4)
                print(data)
            if (CCZUVPN.mode=='status'): print('学生所学成绩',end=' ')
            return self.ParseScore(data)

        def ParseRow(self,row0, f):
            sheet1 = f.get_sheet('sheet1')
            for i in range(0, len(row0)):
                sheet1.write(self.row_number, i, row0[i])
            self.row_number = self.row_number + 1
        def ParseGrade(self,s):
            s2 = s
            if s2[6] == '优秀':
                score = 95;
            elif s2[6] == '良好':
                score = 85;
            elif s2[6] == '中等':
                score = 75;
            elif s2[6] == '及格':
                score = 65;
            elif s2[6] == '不及格':
                score = 55;
            elif s2[6] == '合格':
                score = 85
            elif s2[6] == '不合格':
                score = 55
            else:
                score = s2[6];
            term = s2[2];
            name = s2[1]
            s2[4] = s2[4].strip()
            # print(s2)
            bixiu = ('实践环节', '学科基础必修', '通识教育必修', '专业必修')
            if s2[4] in bixiu:
                cred = s2[5]
            else:
                cred = 0
            return name, int(term), float(cred), float(score)
        def ParseScore(self,data):
            score_table=[]
            row0 = ('学号', '姓名', '学期', '课程', '类别', '学分', '分数', '考试性质', '绩点', '学科代码')
            terms = [[0 for i in range(10)] for j in range(10)]
            max_term = 0

            for i in data:
                data2 = i.find_all('td')
                item = []
                for j in data2:
                    item.append(j.text)
                try:
                    name, term, cred, score = self.ParseGrade(item)
                except:
                    continue
                if term > max_term: max_term = term;
                terms[term][0] = terms[term][0] + 1
                terms[term][1] = terms[term][1] + cred
                terms[term][2] = terms[term][2] + cred * score
                score_table.append(item)
            for i in range(1, max_term + 1, 1):
                if terms[i][1] > 0:
                    avg = terms[i][2] / terms[i][1];
                else:
                    avg = 0;
                t = ('第' + str(i) + '学期：', '总课程:' + str(terms[i][0]), ' 总学分:' + str(terms[i][1]),
                     ' 总绩点:' + str(terms[i][2]), ' 加权平均分:' + str(avg), ' 绩点' + str(avg/20))
                score_table.append(t)
                terms[max_term + 1][0] = terms[max_term + 1][0] + terms[i][0];
                terms[max_term + 1][1] = terms[max_term + 1][1] + terms[i][1];
                terms[max_term + 1][2] = terms[max_term + 1][2] + terms[i][2];

            i = max_term + 1
            if terms[i][1] > 0:
                avg = terms[i][2] / terms[i][1];
            else:
                avg = 0;
            t = ('所有学期：', '总课程:' + str(terms[i][0]), ' 总学分:' + str(terms[i][1]), ' 总绩点:' + str(terms[i][2]),
                 ' 加权平均分:' + str(avg),' 绩点:' + str(avg/20))
            score_table.append(t)
            return score_table
        def SaveScoreToXls(self,score_table,filename):
            filename=filename+'.xls'
            f = xlwt.Workbook()
            sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
            for i in score_table:
                self.ParseRow(i, f)
            f.save(filename)


        #查询个人资料
        def GetProfile(self):
            if (CCZUVPN.mode == 'status'): print('资料', end=' ')
            i9 = CCZUVPN.session.get(
                url='https://webvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/web_xjgl/xjgl_wh_tj_xsxx.aspx',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/View/indexTablejw.aspx',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'iframe',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
               },
            )
            soup9 = BeautifulSoup(i9.text, 'lxml')
            viewstate=str(soup9.body.div.find(id='__VIEWSTATE'))
            viewstate=viewstate.lstrip('<input id="__VIEWSTATE" name="__VIEWSTATE" type="hidden" value="')
            viewstate=viewstate.rstrip('"/>')
            viewstategenerator=str(soup9.body.find(id='__VIEWSTATEGENERATOR'))
            viewstategenerator=viewstategenerator.lstrip('<input id="__VIEWSTATEGENERATOR" name="__VIEWSTATEGENERATOR" type="hidden" value="')
            viewstategenerator=viewstategenerator.rstrip('"/>')
            self.__viewstate=viewstate
            self.__viewstategenerator=viewstategenerator
            # print(soup9)
            i9txt=i9.text
            if (CCZUVPN.mode=='test'):
                print(99999999)
                print(soup9)
                print(viewstate)
                print(viewstategenerator)
            return i9txt

        #获取照片
        def GetPhoto(self,studentNumber,path):
            if (CCZUVPN.mode == 'status'): print('照片', end=' ')
            jpg=studentNumber+'.jpg'
            i11 = CCZUVPN.session.get(
                url='https://zmvpn.cczu.edu.cn/http/webvpndc2d086cb5b297c15e661687e73c1549/images/xszp/'+jpg,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
                },
                # allow_redirects=False
            )
            path=path+'/'+jpg
            with open(path, 'wb') as f:
                f.write(i11.content)
    #校园卡管理系统
    class Card:
        def __init__(self,username):
            if (CCZUVPN.mode == 'status'): print('校园卡', end=' ')
            self.username=username
            url1='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/czdxbmportalHome.action?sno='+username
            i12 = CCZUVPN.session.get(
                url=url1,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Content-Length': '150',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Origin': 'https://webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn4578b329feda6a5f6cc5a9222350e3b0/sso/login?service=http%3A%2F%2Fs.cczu.edu.cn%2F',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
                data={
                   'sno':username
                },
            )
            if(CCZUVPN.mode=='test'):
                print(12121212)
                soup12 = BeautifulSoup(i12.text, 'lxml')
                # print(soup12)

        def GetProfile(self):
            if (CCZUVPN.mode == 'status'): print('资料', end=' ')
            i13 = CCZUVPN.session.get(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accountcardUser.action',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accleftframe.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
            )
            if(CCZUVPN.mode=='test'):
                print(13131313)
                soup13 = BeautifulSoup(i13.text, 'lxml')
                # print(soup13)
                name=soup13.body.table.tr.td.table#.tr['align']
                for i, child in enumerate(name.children):
                    # print(i)
                    # print('66666666666666')
                    # print(child)
                    if i == 3:
                        child = child.tr.th.table
                        for j, child2 in enumerate(child.children):
                            if j == 3:
                                for k, child3 in enumerate(child2.children):
                                    if k == 3:
                                        print(child3.div.text)
                                    elif k==7:
                                        print(child3.div.text)
                                        self.cardid=child3.div.text
                                    elif k == 9:
                                        txt = str(child3.find('img'))
                                        reg = re.compile(r'uno=............')
                                        match = reg.search(txt)
                                        start = match.start();
                                        end = match.end();
                                        photoid = txt[start + 4:end]
                                        print(photoid)
                                        self.photoid=photoid
                                        break
                            elif j == 11:
                                for k, child3 in enumerate(child2.children):
                                    if k == 7:
                                        print(child3.div.text);
                                        break;
                            elif j == 15:
                                for k, child3 in enumerate(child2.children):
                                    if k == 3:
                                        print(child3.div.text);
                                        break;
                            if j == 23:
                                for k, child3 in enumerate(child2.children):
                                    if (k == 3):
                                        print(child3.text);
                                        break;
                        break
                # print(name)

        def GetPhoto(self,path):
            if (CCZUVPN.mode == 'status'): print('照片', end=' ')
            i14 = CCZUVPN.session.get(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/getPhoto.action?uno='+self.photoid,
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accleftframe.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
            )
            path = path + '/' + self.username+'.jpg'
            with open(path, 'wb') as f:
                f.write(i14.content)

        def QueryFlow(startdate,enddate,self):
            if (CCZUVPN.mode == 'status'): print('消费5', end='')
            # startdate='20220227'
            # enddate='20220306'
            i15 = CCZUVPN.session.get(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn.action',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accleftframe.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
            )
            # soup15 = BeautifulSoup(i15.text, 'lxml')
            # print(soup15)
            if(CCZUVPN.mode=='test'): print(15151515)
            if (CCZUVPN.mode == 'status'): print('6', end='')
            i16 = CCZUVPN.session.post(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn1.action',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Connection': 'keep-alive',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accleftframe.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
                data={
                    'account': self.cardid,
                    'inputObject': 'all',
                    'Submit': '+%C8%B7+%B6%A8+'
                }
            )
            if (CCZUVPN.mode=='test'): print(16161616)
            # soup16 = BeautifulSoup(i16.text, 'lxml')
            # print(soup16)
            if (CCZUVPN.mode == 'status'): print('7', end='')
            i17 = CCZUVPN.session.post(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn2.action',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Content-Length': '45',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn1.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                },
                data={
                    'inputStartDate': startdate,
                    'inputEndDate': enddate
                }
            )
            if (CCZUVPN.mode=='test'): print(17171717)
            # soup17 = BeautifulSoup(i17.text, 'lxml')
            # print(soup17)
            # time.sleep(3)
            if (CCZUVPN.mode == 'status'): print('8', end='')
            i18 = CCZUVPN.session.post(
                url='https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn3.action',
                headers={
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Content-Lenght':'0',
                    # 'Cookie': CCZUVPN.realcookie,
                    'Host': 'webvpn.cczu.edu.cn',
                    'Origin': 'https://webvpn.cczu.edu.cn',
                    'Referer': 'https://webvpn.cczu.edu.cn/http/webvpn48ea4191986ecc27b223ea5e039e79cb8c19f40f8a9ef3f65599836b50e81265/accounthisTrjn2.action',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'Sec-Fetch-Dest': 'frame',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36',
                }
            )
            soup18 = BeautifulSoup(i18.text, 'lxml')
            # print(soup18)
            parse18=soup18.body.form.table.tr.td
            for i, child in enumerate(parse18.children):
                # print(i,child)
                if i == 3:
                    for j, child2 in enumerate(child.children):
                        if j == 3:
                            child2 = child2.th.table
                            lst=[]
                            dct={'消费时间','商户名称','交易额','现有余额','总交易次数','说明'}
                            for k, child3 in enumerate(child2.children):
                                info=dict.fromkeys(dct)
                                if (k <= 1): continue
                                try:
                                    for t, child4 in enumerate(child3.children):
                                        if t == 1:info['消费时间']=child4.text
                                        elif t == 9:info['商户名称'] = child4.text.strip()
                                        elif t == 13:info['交易额'] = child4.text
                                        elif t == 15:info['现有余额'] = child4.text
                                        elif t == 17:info['总交易次数'] = child4.text
                                        elif t == 21:
                                            info['说明'] = child4.text
                                            lst.append(info)
                                except:
                                    continue
                            return lst
            if(CCZUVPN.mode=='test'): print(18181818)

if __name__=="__main__":
    username = "20440225"
    password = "Amelia,520"
    spider = CCZUVPN()
    spider.Login(username, password, mode='status')
    portalspider=spider.Portal()
    data=portalspider.GetScore()
    print(data)
    # portalspider.SaveScoreToXls(data)

    # with open("stuinfo.json") as f_obj:
    # 	stuinfo = json.load(f_obj)  #读取文件
    # print(stuinfo)
    # for i in range(len(stuinfo)):
    #     username1 = stuinfo[i][0]
    #     password1 = stuinfo[i][1][-6:]
    #     spider=CCZUVPN(username1,password1,mode=True)
    #     portalspider=spider.Portal()
    #     data=portalspider.GetScore()

    # portalspider.GetProfile()
    # portalspider.ModifyProfile()
    # for i in range(1, 31, 1):
    #     s = ''
    #     if i < 10: s = '0'
    #     s = s + str(i);
    #     print(s)
    #     portalspider.GetPhoto('20411031'+s,'photo3')
    # cardspider=spider.Card('19440209')
    # cardspider.GetProfile()
    # print(cardspider.QueryFlow())