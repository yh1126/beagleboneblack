#!/usr/bin/python
# -*- coding: utf-8 -*-

#メソッドにしたとき引数に時間、日付などをもってくることでpathdでのファイル指定などうまくいくはず、あと、このメソッドをコールした時もとファイルを消すはずなので消すようプログラムする必要あり。
#file名をどうするかはみんなと話し合い
import pysftp

HOST = '172.21.42.151' #ホスト名（グローバルIPでもOK）
PORT = 22 #SSHポート番号
USER = 'iwalab' #接続先のユーザ名
PASS_WORD = 'iwalab2016' #秘密鍵のパスフレーズ
fPath = '/Users/yamashitahideshi/study/python/bbb/beagleboneblack/img/akg.jpeg'
#uploadPath = '/var/www/html/'
uploadPath = '/home/iwalab'
sftp = pysftp.Connection(HOST, username=USER, port=PORT, password=PASS_WORD)

sftp.listdir() #接続先のファイル/ディレクトリのリストを返す
sftp.chdir(uploadPath) #接続先の作業ディレクトリを変更
sftp.getcwd() #現在の作業ディレクトリを返す
sftp.put(fPath) #転送するファイルを指定

for item in sftp.execute('ls -l /home/iwalab'): #接続先でlsコマンドを実行（必要ではないです）
  print item,     #結果を表示

sftp.close()

#PRIVATE_KEY_FILE = '/xxxx/xxxxx/.ssh/id_rsa' #接続元の秘密鍵ファイル
#SERVER_ASSETS_DIR = '/home/xxxxx/xxxx.xxx/public_html/';

#pysftpを使用せず、直でparamikoを使用する
#rsa_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_FILE, password=PASS_WORD)
#transport = paramiko.Transport((HOST,PORT))
#transport.connect(username=USER, pkey=rsa_key)
#sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.chdir( SERVER_ASSETS_DIR )    #接続先の作業ディレクトリを変更
#print sftp.listdir() #接続先のファイル/ディレクトリのリストを返す
#print sftp.getcwd()  #現在の作業ディレクトリを返す
#sftp.put(
#  '/xxxx/result.html', #転送元のローカルファイルを指定
#  SERVER_ASSETS_DIR +'/result.html'     #転送先のファイルを指定
#)
#sftp.close()
