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


def getLabel(text):

	result=list()

	re_label='<a href="//www.bilibili.com/v/(.*?)/">'
	re_uptime='<time>(.*?)</time>'
	re_uploader_no='#whisper/mid(.*?)" target="_blank"'
	re_video_name='&quot;title&quot;:&quot;(.*?)&quot;,&quot;images&quot;:'


	label=re.compile(re_label).findall(text)
	result.append("".join(label[-1]))

	uptime=re.compile(re_uptime).findall(text)
	result.append("".join(uptime))

	uploader_no=re.compile(re_uploader_no).findall(text)
	result.append("".join(uploader_no))

	video_name=re.compile(re_video_name).findall(text)
	result.append("".join(video_name))

	result[3]=result[3].replace("'", "`")

	#print(i,label[-1])
	#print(i,uptime)
	#print(i,uploader_no)
	#print(i,result)
	return result




def insert(label_message,dbno):

	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="bili", port=3306,charset='utf8')
	cursor = db.cursor()


	
	label_message[2]=int(label_message[2])

	sql = "INSERT INTO videolabel(dbno,uploaderno,label,videoname,uploadtime) \
		VALUES ('%d',  '%d', '%s', '%s', str_to_date(\'%s\','%%Y-%%m-%%d %%H:%%i:%%s'))" % \
		(dbno, label_message[2], label_message[0], label_message[3], label_message[1])
	
	try:
		cursor.execute(sql)
		db.commit()
		#print('videolabel提交成功')
	except Exception as e:  
		db.rollback()

		#写日志，记录有插入错误的视频信息
		log(dbno)

		print('catch异常')
	finally:
		db.close()
		#print('连接关闭')




def get_aid(i):

	db = pymysql.connect(host="localhost",user="root", password="123456ls",db="bili", port=3306,charset='utf8')
	cursor = db.cursor()

	sql = " SELECT aid FROM videomes \
		WHERE dbno = '%d'" % (i)

	try:
		cursor.execute(sql)
		# 获取所有记录列表
		#results = cursor.fetchall()
		result = cursor.fetchone()
		return result[0]
	except Exception as e:
		print ("videomes查询出现错误")

	# 关闭数据库连接
	db.close()


def log(dbno):
	#获得问题文件aid
	aid=get_aid(dbno)

	#拼接出应该写入的日志文件名
	log_name='D:\codes/bilibili\log\label-log-'+time.strftime("%Y-%m-%d", time.localtime())+'.txt'
	#打开文件，写入错误视频的dbno和aid以及此时时间，之后将文件关闭
	f = open(log_name, 'a')
	f.write(str(dbno)+' '+str(aid)+' '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n')
	f.close()



def all():

	while True:
		low = input("请输起始的dbno号码：")
		high = input("请输入终止dbno号码：")
	
		low = int(low)
		high = int(high)

		print('再检查一下输入起始和终止号码的范围\n')
		check = input('确认无误输入1，否则输入0: ')
		print('')

		check = int(check)

		if check == 0:
			continue
		
		start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		for i in range(low,high):
			try:
				avno = get_aid(i)
				url = "https://www.bilibili.com/video/av"+str(avno)
				insert(getLabel(getHTMLText(url)),i)
				print(str(low)+' '+str(i)+"/"+str(high-1)+'  目前进度:'+str(round(((int(i)-int(low)+1)/(int(high)-int(low)))*100,2))+'%')
				#print(getLabel(getHTMLText(url)),i)
			except:
				continue

		end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

		bili_script.getlabel_log(start_time,end_time,low,high)

		print("刚刚执行的起始和终止aid号码是"+str(low),str(high))

		print('开始时间:'+start_time)
		print('结束时间:'+end_time+'\n')

		print('先冷静一下\n')
		print('下一次输入的起始号码应该是上一次运行的终止号码\n')
		print('比如上一次运行的起始和终止是1和10')
		print('那么这一次的起始号码就应该是10')
		print('\n\n')
		print("刚刚执行的起始和终止aid号码是"+str(low),str(high))
		print('\n\n')
		flag = input('继续运行输入1，终止输入0： ')



		flag = int(flag)

		if flag == 0:
			break


		pass

	
	



'''
if __name__=="__main__":
	
	#avno = 186581
	#url = "https://www.bilibili.com/video/av"+str(avno)
	#insert(print(getLabel(getHTMLText(url)),8999))


	for i in range(8,9):
		try:
			avno = get_aid(i)
			url = "https://www.bilibili.com/video/av"+str(avno)
			insert(getLabel(getHTMLText(url)),i)
			#print(getLabel(getHTMLText(url)),i)
		except:
			continue
#for i in range(1,4758):
#for i in range(4759,6405):
'''