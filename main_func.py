import linecache
import os
import random

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'result'))
## 来点白丝
def give_me_some_bais(num):
    txt = open(file_path+'/bais.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()

    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/bais.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set


## 来点黑丝
def give_me_some_heis(num):
    txt = open(file_path+'/heis.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()

    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/heis.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点足控
def give_me_some_zuk(num):
    txt = open(file_path+'/zuk.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()
    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/zuk.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set


## 来点jk
def give_me_some_jk(num):
    txt = open(file_path+'/jk.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()
    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/jk.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点巨乳
def give_me_some_jur(num):
    txt = open(file_path+'/jur.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()
    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/jur.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点网红
def give_me_some_mcn(num):
    txt = open(file_path+'/mcn.txt',mode='rb')
    data = txt.read().decode('utf-8')  # python3一定要加上这句不然会编码报错！
    txt.close()
    # 获取txt的总行数！
    n = data.count('\n')
    print("总行数", n)
    heis_set = []
    # 选取随机的数
    for index in range(0,num) :
        i = random.randint(1, (n + 1))
        print("本次使用的行数", i)
        ## 得到对应的i行的数据
        line=linecache.getline(file_path+'/mcn.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set