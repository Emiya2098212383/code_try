# -*- coding: UTF-8 -*-

# Filename : 01-string.py
# author by : Emiya

msg = '啊'
byte_msg = msg.encode()
print('--default:[%s]' % byte_msg)
new_msg = byte_msg.decode()
print('--default:[%s]' % new_msg)

byte_msg = msg.encode()
print('--utf-8:[%s]' % byte_msg)
new_msg = byte_msg.decode()
print('--utf-8:[%s]' % new_msg)

byte_msg = msg.encode()
print('--gbk:[%s]' % byte_msg)
new_msg = byte_msg.decode()
print('--gbk:[%s]' % new_msg)

byte_msg = msg.encode()
print('--gb2312:[%s]' % byte_msg)
new_msg = byte_msg.decode()
print('--gb2312:[%s]' % new_msg)
