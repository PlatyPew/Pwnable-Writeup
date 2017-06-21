import socket
import sys
import re
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('pwnable.kr', 9007)
sock.connect(server_address)
sock.recv(2048)

for i in range(100):
	arr = re.findall("\d+", sock.recv(100))
	count = int(arr[-1])
	number = int(arr[-2])
	low = 0
	high = number
	while_count = 0

	while(low <= high):
		while_count += 1
		mid = (low+high)/2
		send_data = " ".join([str(i) for i in range(low, mid+1)])+"\n"
		sock.sendall(send_data)
		data = sock.recv(100)
		res = int(data[:-1]) % 10
		if int(data[:-1]) == 9: break;
		if res == 9:
			high = mid - 1
		elif res == 0:
			low = mid + 1

	for i in range(count - while_count + 1):
		if res == 0 and i == 0:
			send_data = str(int(send_data)+1) + "\n"
		sock.sendall(send_data)
		data = sock.recv(100)
		print data
data = sock.recv(100)
print data