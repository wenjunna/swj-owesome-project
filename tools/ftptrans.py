# -*- coding: utf-8 -*-
"""
@Time ： 2023/10/11 14:53
@Auth ： sunwenjun
@File ：ftptrans.py
@IDE ：PyCharm
@Brief：ftp传输数据。把本地数据上传到指定地址的ftp
"""
import ftplib
import socket
import os.path


class FTPTrans(object):
    def __init__(self, ftpconfig):
        self.host = ftpconfig['ip']
        self.port = ftpconfig['port']
        self.username = ftpconfig['user']
        self.password = ftpconfig['passwd']
        self.ftp = self.ftpconnect(self.host, self.port, self.username, self.password)

    def ftpconnect(self, host, port, username, password):
        '''
        创建ftp链接
        :return:
        '''
        ftp = ftplib.FTP()
        # ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
        ftp.encoding = 'utf-8'  # 解决中文编码问题，默认是latin-1
        try:
            ftp.connect(host, port)  # 连接
            ftp.login(username, password)  # 登录，如果匿名登录则用空串代替即可
            print(ftp.getwelcome())  # 打印欢迎信息
        except(socket.error, socket.gaierror):  # ftp 连接错误
            print("ERROR: cannot connect [{}:{}]".format(host, port))
            return None
        except ftplib.error_perm:  # 用户登录认证错误
            print("ERROR: user Authentication failed ")
            return None
        return ftp

    def is_file_exists(self, path, filename):
        '''
        判断远程目标文件是否存在
        :param path: 文件夹
        :param filename: 文件名
        :return: 存在返回True, 不存在返回false
        '''
        file_path_list = self.ftp.nlst(path)
        file_path = path + "/" + filename
        if file_path in file_path_list:
            return True
        return False

    def ftp_makedirs_cwd(self, path):
        '''
        创建目标目录（文件夹）
        :param path:
        :return:
        '''
        path_list = path.split("/")
        path0 = path_list[0]

        # 循环一层一层创建目录，否则易出错
        for p in path_list[1:]:
            path1 = path0 + "/" + p
            try:
                self.ftp.cwd(path1)
                # print('进入目录，路径 %s' % path1)
            except ftplib.error_perm:
                try:
                    # print('远程路径不存在 %s ,需要创建' % path1)
                    self.ftp.mkd(path1)
                    self.ftp.cwd(path1)
                except ftplib.error_perm:
                    print('没有权限创建 %s', path1)
            path0 = path1

        return

    def upload(self, localpath, despath, filename):
        '''
        数据传输
        :param localpath: 本地文件夹
        :param despath: 目标文件夹
        :param despath: 文件名
        :return:
        '''
        bufsize = 8192

        # 判断本地文件是否存在
        localfile = localpath + "/" + filename
        if not os.path.exists(localfile):
            return

        # 判断目标文件是否存在
        if self.is_file_exists(despath, filename):
            return

        # 创建目标文件夹
        self.ftp_makedirs_cwd(despath)

        # 文件传输
        try:

            file_handler = open(localfile, "rb")
            self.ftp.storbinary("STOR {}".format(filename), file_handler, bufsize)
        except ftplib.error_perm as e:
            print(u"请检查上传路径是否正确，是否连接FTP，---错误代码%s" % e)
        return

    def quit(self):
        self.ftp.quit()
        return


if __name__ == '__main__':
    ftpconfig = {
        'ip': '124.16.***.***',
        'port': 1024,
        'user': 'sunwenjun',
        'passwd': '123456'
    }

    ftptrans = FTPTrans(ftpconfig)
    localpath = "/localpath"  # 本地文件目录
    despath = "/despath"  # 目标文件目录
    filename = "test.txt"  # 要上传的文件
    ftptrans.upload(localpath, despath, filename)
