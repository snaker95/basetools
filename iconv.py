#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/12 14:14
# @Author  : Snaker95
# @Desc    : 循环遍历目录下文件, 并且重新编码
# @File    : iconv.py
# @Software: PyCharm

import os
import codecs


# 获取目录下所有文件
def getfiles(path):
    filelist = []
    # 判断是否存在该文件夹
    if (os.path.exists(path)):
        filelist = os.listdir(path)


    return filelist

# 通过命令进行文件编码
def to_iconv(file,newfile, oldcode = 'UTF-8', newcode = 'GB18030'):
    if os.path.isfile(file):
        command = "iconv -f %s -t %s %s > %s"%(oldcode,newcode,file,newfile)
        print "执行的命令: %s" % command
        os.system(command)

# 读取文件内容,然后另存时进行编码
def to_other_save(file,newfile, oldcode = 'UTF-8', newcode = 'GB18030'):
    file_size = os.path.getsize(file) # byte
    if file_size < 100*1024*1024: # 100M
        f = codecs.open(file, "r", oldcode)
        lines = f.readlines()
        f.close()
        n_f = codecs.open(newfile,'a+',newcode)
        for line in lines:
            n_f.write(line)
        n_f.close()

# 启动程序
def run():
    path = raw_input("请输入转码的目录(/tmp/):") or '/tmp/'
    oldcode = raw_input("请输入原始编码(UTF-8):") or 'UTF-8'
    newcode = raw_input("请输入新的编码(GB18030):") or 'GB18030'

    print '路径:%s'%path
    print '原始编码:%s'%oldcode
    print '新编码:%s'%newcode

    # 获取 所有文件
    files = getfiles(path)
    for file in files:
        print "当前文件: %s" % file
        y = raw_input("文件%s是否要进行转码(N):"%file)
        if y.lower() == 'y' or y.lower() == 'yes':
            oldfull = '%s%s'%(path,file)
            newfile = '%s-%s'%(newcode,file)
            newfull = '%s%s'%(path,newfile)

            # 通过mac下命令进行转码
            # to_iconv(oldfull, newfull)

            # 读取文件,另存时编码
            to_other_save(oldfull, newfull)

if __name__ == '__main__':
    run()