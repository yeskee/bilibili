import time
#库函数文件


def TTS(x):
	#name of the function means Time to Stamp
	#return a int
	timeArray = time.strptime(x, '%Y-%m-%d %H:%M:%S')
	timeStamp = time.mktime(timeArray)
	return timeStamp


def videomes_log(start,end,low,high):
	#本次执行开始时间，结束时间，区间起始和终止位置.
	#文件名这样写也能成功读取
	log_name = 'D:\codes/bilibili\log/videomes-log-'+time.strftime("%Y-%m-%d", time.localtime())+'.txt'
	f = open(log_name, 'a')
	f.write('===============================\n')
	f.write('=========本次查询api信息===========\n')
	f.write('\n本次运行开始时间：'+str(start)+'\n')
	f.write('本次运行结束时间：'+str(end)+'\n')

	f.write('执行起始号码位置：'+str(low)+'\n')
	f.write('执行终止号码位置：'+str(high)+'\n')
	f.write('实际终止号码位置：'+str(high-1)+'\n')

	average = round((TTS(end)-TTS(start))/(int(high)-int(low)),2)
	f.write('平均每条读取用时：'+str(average)+'s\n')
	f.write('\n===============================\n\n')
	f.close()
	pass

def getlabel_log(start,end,low,high):
	#本次执行开始时间，结束时间，区间起始和终止位置.
	#文件名这样写也能成功读取
	log_name = 'D:\codes/bilibili\log\getlabel-log-'+time.strftime("%Y-%m-%d", time.localtime())+'.txt'
	f = open(log_name, 'a')
	f.write('===============================\n')
	f.write('=========本次查询标签信息===========\n')
	f.write('\n本次运行开始时间：'+str(start)+'\n')
	f.write('本次运行结束时间：'+str(end)+'\n')

	f.write('执行起始号码位置：'+str(low)+'\n')
	f.write('执行终止号码位置：'+str(high)+'\n')
	f.write('实际终止号码位置：'+str(high-1)+'\n')

	average = round((TTS(end)-TTS(start))/(int(high)-int(low)),2)
	f.write('平均每条读取用时：'+str(average)+'s\n')
	f.write('\n===============================\n\n')
	f.close()
	pass
