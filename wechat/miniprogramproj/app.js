// app.js
App({
  onLaunch() {
    // 展示本地存储能力
    const logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)
    const token = wx.getStorageSync('token')
    if (token) {
      // 如果 token 存在，跳转到菜单页面
      wx.navigateTo({
        url: '/pages/menu/menu'
      })
    } else {
      // 如果 token 不存在，跳转到登录页面
      wx.navigateTo({
        url: '/pages/login/login'
      })
    }
    
  },
  globalData: {
    userInfo: null
  }
})
