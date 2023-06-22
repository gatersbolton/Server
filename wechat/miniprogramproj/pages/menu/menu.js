Page({
  data: {
    campus: 'wujin',
    floors: [ '2楼', '3楼', '4楼', '5楼', '6楼'],
    startTimes: [
      '6:00', '6:30', '7:00', '7:30', '8:00', '8:30', '9:00', '9:30',
      '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30',
      '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30',
      '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00', '21:30',
      '22:00', '22:30', '23:00', '23:30'
    ],
    durations: ['0.5小时', '1小时', '1.5小时', '2小时', '2.5小时', '3小时', '3.5小时', '4小时'],
    floorIndex: 0,
    seat: '',
    startTimeIndex: 0,
    durationIndex: 7, // 默认选择4小时
  },

  onCampusChange: function (e) {
    const value = e.detail.value;
    if (value !== this.data.campus) {
      this.setData({
        campus: value
      });
    }
  },

  onFloorChange: function (e) {
    const value = e.detail.value;
    if (value !== this.data.floorIndex) {
      this.setData({
        floorIndex: value
      });
    }
  },

  onSeatInput: function (e) {
    const value = e.detail.value;
    if (value !== this.data.seat) {
      this.setData({
        seat: value
      });
    }
  },

  onSubmit: function () {
    // TODO: 处理预约逻辑
  },

  onCancel: function () {
    // TODO: 处理取消逻辑
  },

  onStartTimeChange: function (e) {
    const value = e.detail.value;
    if (value !== this.data.startTimeIndex) {
      this.setData({
        startTimeIndex: value
      });
    }
  },
  onDurationChange: function (e) {
    const value = e.detail.value;
    if (value !== this.data.startTimeIndex) {
      this.setData({
        durationIndex: value
      });
    }
  }


})