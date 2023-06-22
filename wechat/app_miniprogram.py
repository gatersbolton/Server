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

@app.route('/miniprogram', methods=['GET'])
def wechat_auth():
    return 'wechat:goodjob!'

if __name__ == '__main__':
    app.run(port='5001')