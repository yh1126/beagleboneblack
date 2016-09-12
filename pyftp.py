#!/usr/bin/python
# -*- coding: utf-8 -*-

#メソッドにしたとき引数に時間、日付などをもってくることでpathdでのファイル指定などうまくいくはず、あと、このメソッドをコールした時もとファイルを消すはずなので消すようプログラムする必要あり。
#file名をどうするかはみんなと話し合い
import pysftp

###nomal?
#HOST = '172.21.42.151' #ホスト名（グローバルIPでもOK）
#PORT = 22 #SSHポート番号
#USER = 'iwalab' #接続先のユーザ名
#PASS_WORD = 'iwalab2016' #秘密鍵のパスフレーズ
fPath = '/Users/yamashitahideshi/study/python/bbb/beagleboneblack/img/akg.jpeg'
#uploadPath = '/var/www/html/'
uploadPath = '/home/iwalab/.ssh'

#sftp = pysftp.Connection(HOST, username=USER, port=PORT, password=PASS_WORD)

#sftp.listdir() #接続先のファイル/ディレクトリのリストを返す
#sftp.chdir(uploadPath) #接続先の作業ディレクトリを変更
#sftp.getcwd() #現在の作業ディレクトリを返す
#sftp.put(fPath) #転送するファイルを指定
#for item in sftp.execute('ls -l /home/iwalab'): #接続先でlsコマンドを実行（必要ではないです）
#  print item,     #結果を表示
#
#sftp.close()

###RSA
HOST = '172.21.42.151'
PORT = 22
USER = 'iwalab'
PASS_WORD = ''
PRIVATE_KEY_FILE = '/Users/yamashitahideshi/.ssh/id_rsa' #接続元の秘密鍵ファイル

sftp = pysftp.Connection(HOST, username=USER, port=PORT, private_key=PRIVATE_KEY_FILE)
sftp.listdir() #接続先のファイル/ディレクトリのリストを返す
sftp.chdir(uploadPath) #接続先の作業ディレクトリを変更
sftp.getcwd() #現在の作業ディレクトリを返す
sftp.put(fPath) #転送するファイルを指定

for item in sftp.execute('ls -l /home/iwalab'): #接続先でlsコマンドを実行（必要ではないです）
  print item,     #結果を表示

sftp.close()
