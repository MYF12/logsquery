from logsquery.queryapp.get_now_time import GetNowTime
nowtime = GetNowTime()
aa = nowtime.getNowTime()
print(aa)


str1='hello;   china!'
str2 = " [WARNING]: No hosts matched, nothing to do" \
       "hosts (0):"
print(len(str2))
for i in [";",'"']:
    if i in str1:
        print('yes')
    else:
        print('no')


test = "1,2,3,4,5,6,8"
testlist = test.split(',')
count = len(testlist)
print(testlist,"\n",count,testlist[count-1])




# 导入time模块
import time
# # 打印时间戳
print(str(int(time.time())))
# d1 = int(time.time())
print(time.strftime('%y%m%d%H%M%S',time.localtime(time.time())))

