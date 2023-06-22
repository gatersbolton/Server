function login(username, password, successCallback) {
  wx.request({
    url: 'http://zhaokejian.life/miniprogram',
    success: function(res) {
      // 成功获取数据后的处理逻辑
      console.log("666");
    },
    fail: function(err) {
      // 处理请求失败的情况
      console.log("sbsb",err);
    }
  })
}

module.exports = {
  login: login
}