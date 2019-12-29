#!/usr/bin/python
# coding=utf-8
import time

class TimeToDate():

    def time_date1(self,time_sj):  # 时间转为时间戳，时间为str
        self.time_sj = time_sj
        date_sj = time.strptime(self.time_sj, "%Y-%m-%d")  # 定义格式
        time_int = int(time.mktime(date_sj))
        return time_int  # 返回传入时间的时间戳，类型为int

    def time_date2(self,time_sj):  # 时间戳转换年月日时间格式,时间戳为int
        self.time_sj = time_sj
        date_sj = time.localtime(self.time_sj)
        time_str = time.strftime("%Y%m%d", date_sj)  # 时间戳转换正常时间
        return time_str
'''
if __name__ == "__main__":
    a = TimeToDate().time_data1("2019-08-01")
    print(a)
    b = TimeToDate().time_data2(1564588800)
    print(b)
'''