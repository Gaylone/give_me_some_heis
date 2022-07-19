import linecache
import random

## 来点白丝

def give_me_some_bais(num):
    txt = open('./result/bais.txt',mode='rb')
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
        line=linecache.getline(r'./result/bais.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set


## 来点黑丝
def give_me_some_heis(num):
    txt = open('./result/heis.txt',mode='rb')
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
        line=linecache.getline(r'./result/heis.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点足控
def give_me_some_zuk(num):
    txt = open('./result/zuk.txt',mode='rb')
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
        line=linecache.getline(r'./result/zuk.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set


## 来点jk
def give_me_some_jk(num):
    txt = open('./result/jk.txt',mode='rb')
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
        line=linecache.getline(r'./result/jk.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点巨乳
def give_me_some_jur(num):
    txt = open('./result/jur.txt',mode='rb')
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
        line=linecache.getline(r'./result/jur.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set

## 来点网红
def give_me_some_mcn(num):
    txt = open('./result/mcn.txt',mode='rb')
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
        line=linecache.getline(r'./result/mcn.txt', i).replace("\n",'')
        heis_set.append(line)
    print(heis_set)
    linecache.clearcache()
    return heis_set