import re #实现正则匹配
import os,sys #os实现对文件目录的操作，通过sys获取程序参数
from collections import Counter #用来跟踪值出现的次数
def jisuanTotal(word):
    user_counters=Counter(word)
    total=0
    for user_counter in user_counters:
        total+=1
    print("total "+str(total)+" words\n")
    lsts=user_counters.most_common(10)
#most_common()用来实现Top 10的功能，返回一个列表，列表元组提供频率前10的元素和次数
    for lst in lsts:
        print("%s  %d"%(lst[0],lst[1]))
        #将元素和计数显示出来
def word_list(filename): #实现功能一
    with open(filename,encoding='utf-8') as f: #打开文件
        content=f.read() #用方法read()读取文件的全部内容
        words=re.findall(r'[\w^-]+',content)
#findall()方法能够以列表的形式返回能匹配的子串,w匹配从小写a到z,大写A到Z，数字0到9
        jisuanTotal(words)
def file_name(path): #功能二实现，输入不带后缀的文件名
    path=path+'.txt'
    try:
        with open(path,encoding='utf-8') as f: 
            content=f.read()
    except FileNotFoundError: #异常处理,找不到文件，输出文件不存在
        msg="The file"+path+"does not exist."
        print(msg)
    else:
        words=re.findall(r'[\w^-]+',content)
        jisuanTotal(words)
def file_floder(path): #功能三实现输入存储有英文作品文件的目录名
    dirs = os.listdir(path) 
    for file in dirs:
        if os.path.isfile(file): #判断是否是文件
           print(os.path.splitext(file)[0])
#os.path.splitext(“文件路径”)用于分离文件名与扩展名；默认返回(fname,fextension)元组
           with open(file,encoding='utf-8') as f:
               words=re.findall(r'[\w^-]+',f.read())
               jisuanTotal(words)
               print('----')
def main(argv):
    if sys.argv[1]=='-s': #功能一
        word_list(sys.argv[2])
    elif os.path.isdir(sys.argv[1]): #判断是否是目录，功能三
        file_floder(sys.argv[1])
    else:                 #功能二
        file_name(sys.argv[1])
if __name__=="__main__":
    main(sys.argv[1:])
    
        
            
        
    
