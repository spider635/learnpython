'''
# 创建一个基于TCP连接的Socket
# 导入socket库:
import socket

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET指定使用IPv4协议; SOCK_STREAM指定使用面向流的TCP协议
# 建立连接:
s.connect(('www.sina.com.cn', 80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1) # 仅分割一次
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
'''

# 一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去
# 导入socket库:
import socket
import threading
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口:
s.bind(('127.0.0.1', 9999))

s.listen(5) # 开始监听端口，传入的参数指定等待连接的最大数量
print('Waiting for connection...')

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
