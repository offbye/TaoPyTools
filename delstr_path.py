#!/usr/bin/python2.7
# -*- encoding: UTF-8 -*-
# Copyright 2014 offbye@gmail.com


"""Delete lines contains some string form all expected extension files in path
批量删除目录指定扩展名的文件中含指定字符串的行

可以指定目录和文件扩展名
临时写的一个工具脚本，与App生成系统无关

Usage: python delstr_path.py  -p YOUR_PATH  -e FILE_EXTENSION -s CONTAIN_STRING_WANT_TO_DELETE
"""

__author__ = ['"Zhang Xitao":<offbye@gmail.com>']

import sys
import os
import shutil
import getopt


def delstr_path(p, findstr, suffix='js'):
    # 传递路径及两个字符串作为参数
    workdir = p
    os.chdir(workdir)
    cwd = os.getcwd()
    dirs = os.listdir(cwd)
    for tmp in dirs:
        path = os.path.join(cwd, tmp)
        #print 'path=', path
        #如果是文件
        if os.path.isfile(path):
            #判断文件扩展名
            if os.path.splitext(tmp)[1][1:] == suffix:
                tmp_name = path + '.bak'
                tmp_file = open(tmp_name, "w")
                with open(path) as f:
                    lines = f.readlines()
                for line in lines:
                    # 如果包含字符串则跳过,否则写入临时文件
                    if line.find(findstr) > -1:
                        continue
                    tmp_file.write(line)
                tmp_file.close()
                # 使用新文件替换原文件
                shutil.move(tmp_name, path)



                    #如果是路径，递归
        elif os.path.isdir(path):
            print("Enter dir: " + path)
            delstr_path(path, findstr)


if __name__ == "__main__":
    print("delele contains str in path")
    opts, args = getopt.getopt(sys.argv[1:], "hp:e:s:")
    path = ''
    find_str = ''
    extension = ''
    for op, value in opts:
        if op == "-p":  # 获取路径
            path = value
        elif op == "-e":  # 获取路径
            extension = value
        elif op == "-s":
            find_str = value
            print("Delete lines contains {0} form all {1} files in path  {2}  ".format(find_str, extension, path))
            delstr_path(path, find_str, extension)
            sys.exit()
        elif op == "-h":
            print("Usage: python delstr_path.py  -p YOUR_PATH  -e FILE_EXTENSION -s CONTAIN_STRING_WANT_TO_DELETE")
            sys.exit()

