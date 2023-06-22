// index.js
// 获取应用实例
const app = getApp()
var login = require('../../utils/login.js');
Page({
  data: {
    passwordInputHidden: true,
    username: '20416323',
    password: 'Xf552200.'
  },
  togglePasswordInput: function() {
    this.setData({
      passwordInputHidden: !this.data.passwordInputHidden
    })
  },

  login: function() {
    // console.log(this.data.username),
    // console.log(this.data.password)
    var that = this;
    login.login(that.data.username, that.data.password, function(res) {
        // console.log(res);
    });
},




  bindUsernameInput: function(e) {
    this.setData({
      username: e.detail.value
    })
  },
  bindPasswordInput: function(e) {
    this.setData({
      password: e.detail.value
    })
  },
})
