from urllib import request
import requests
import re
import time
import json
import pymysql
import bili_script



def getHTMLText(url):
	try:
		r = requests.get(url,timeout=30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"



def inserter(x):


	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="bili", port=3306,charset='utf8')
	cursor = db.cursor()
	x = list(map(int, x))


	sql = "INSERT INTO videomes(aid,view,danmaku,reply,favorite,coin,\
	share,now_rank,his_rank,no_reprint,copyright,insert_time) \
		VALUES ('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d',\
		str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))" % \
		(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10],\
		 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	
	try:
		cursor.execute(sql)
		db.commit()
		#print('videomes成功提交')
	except Exception as e:  
		db.rollback()
		print('catch异常')
	finally:
		db.close()
		#print('连接关闭')


def insert_dis(x):


	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="bili", port=3306,charset='utf8')
	cursor = db.cursor()

	x[0]=int(x[0])
	x[2]=int(x[2])
	x[3]=int(x[3])
	x[4]=int(x[4])
	x[5]=int(x[5])
	x[6]=int(x[6])
	x[7]=int(x[7])
	x[8]=int(x[8])
	x[9]=int(x[9])
	x[10]=int(x[10])

	sql = "INSERT INTO disappear(aid,danmaku,reply,favorite,coin,\
	share,now_rank,his_rank,no_reprint,copyright,insert_time) \
		VALUES ('%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d',\
		str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))" % \
		(x[0], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9], x[10],\
		 time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	
	try:
		cursor.execute(sql)
		db.commit()
		#print('disappear成功提交')
	except Exception as e:  
		db.rollback()
		print('catch异常')
	finally:
		db.close()
		#print('连接关闭')


def getMassage(url):
	try:
		result = list()

		#匹配字符集
		html=request.urlopen(url).read()
	
		list1 = ['aid', 'view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 
		'now_rank', 'his_rank', 'no_reprint' ];

		flag = 1

		for i in list1:
			#利用列表进行字符串数组的拼接,然后进行匹配
			temp_result = re.compile(i+'":(.*?),').findall(str(html))
			#print(temp_result)
			if temp_result == []:
				flag = 0
				break

			result.append("".join(temp_result))

		#再匹配一次把版权信息的提取出来，就不用再调整字符串了
		temp_result = re.compile('copyright":(.*?)}}').findall(str(html))
		result.append("".join(temp_result))
		#此时的result全是数据不含其它字符
		#根据标记元素flag判断是否输出列表
		if(flag):
			#print(result)
			if(result[1] != '"--"' ):
				inserter(result)
			else:
				insert_dis(result)
	except:
		log(result[0])




def log(massage):

	#拼接出应该写入的日志文件名
	log_name='D:\codes\python\log\pctesta-log-'+time.strftime("%Y-%m-%d", time.localtime())+'.txt'
	#打开文件，写入错误视频的dbno和aid以及此时时间，之后将文件关闭
	f = open(log_name, 'a')
	f.write(str(massage)+' '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
	f.close()
	pass


def all():
	while True:
		low = input("请输起始的aid号码: ")
		high = input("请输入终止aid号码: ")

		print('再检查一下输入起始和终止号码的范围')
		check = input('确认无误输入1，否则输入0： ')

		check = int(check)

		if check == 0:
			continue


		low = int(low)
		high = int(high)

		start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		for i in range(low,high):
			url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(i)
			getMassage(url)
			print(str(low)+' '+str(i)+"/"+str(high-1)+'  目前进度:'+str(round(((int(i)-int(low)+1)/(int(high)-int(low)))*100,4))+'%')
			#延时的语句改在这里了
			time.sleep(0.8)

		end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		bili_script.videomes_log(start_time,end_time,low,high)

		print("刚刚执行的起始和终止aid号码是"+str(low),str(high))
		print('开始时间:'+start_time)
		print('结束时间:'+end_time+'\n')
		print('先冷静一下')
		print('下一次输入的起始号码应该是上一次运行的终止号码')
		print('比如上一次运行的起始和终止是1和10')
		print('那么这一次的起始号码就应该是10')
		print('\n\n')
		print("刚刚执行的起始和终止aid号码是 "+str(low)+' 和 '+str(high))
		print('\n\n')
		flag = input('继续运行输入1，终止输入0： ')


		flag = int(flag)

		if flag == 0:
			break
	pass


'''
if __name__=="__main__":

	for i in range(187111,190000):
		url = "https://api.bilibili.com/x/web-interface/archive/stat?aid="+str(i)
		getMassage(url)

'''
#17700000