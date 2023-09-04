from flask import Flask, request
from wechatpy import parse_message, create_reply, WeChatClient
import xml.etree.ElementTree as ET
import hashlib
import wechat_reply
from wechatpy.fields import (
    BaseField,
    StringField,
    IntegerField,
    DateTimeField,
    FieldDescriptor
)
app = Flask(__name__)

TOKEN = 'your_token_here'  # 替换为您的微信公众号的Token

@app.route('/wechat', methods=['GET'])
def wechat_auth():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    echostr = request.args.get('echostr', '')

    # 检查签名
    if check_signature(signature, timestamp, nonce):
        return echostr
    else:
        return 'Failed to authenticate'

def check_signature(signature, timestamp, nonce):
    tmp_arr = [TOKEN, timestamp, nonce]
    tmp_arr.sort()
    tmp_str = ''.join(tmp_arr)
    tmp_str = hashlib.sha1(tmp_str.encode('utf-8')).hexdigest()

    return tmp_str == signature

@app.route('/wechat', methods=['POST'])
def post_handler():
    signature = request.args.get('signature', '')
    timestamp = request.args.get('timestamp', '')
    nonce = request.args.get('nonce', '')
    # client = WeChatClient(appid='APPID', secret='APPSECRET')
    if not check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        return 'fail'
    xml_str = request.stream.read()
    msg = parse_message(xml_str)
    if msg.type == 'text':
        wechat_id=str(msg.source)
        content=str(msg.content)
        reply = create_reply(wechat_reply.handle(wechat_id=wechat_id,content=content), msg)
    else:
        reply = create_reply('你好!欢迎来到常州大学小助手！', msg)
    return reply.render()
def ReplyText(toUser,fromUser,nowtime,MsgType,content):
    XmlForm = f"""
        <xml>
            <ToUserName><![CDATA[{toUser}]]></ToUserName>
            <FromUserName><![CDATA[{fromUser}]]></FromUserName>
            <CreateTime>{nowtime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{content}]]></Content>
        </xml>
        """

    return {
    "isBase64Encoded": False,
    "statusCode": 200,
    "headers": {"Content-Type": "application/xml"},
    "body": XmlForm
    }
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)