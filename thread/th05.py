import threading
from queue import Queue

def task(l, q):
	for i in range(len(l)):
		l[i] = l[i] ** 5
	q.put(l)


def main():
	q = Queue()
	threads = []
	data = [[1,2,3],[4,5,6,7],[8,9,10,11,12],[13,14,15,16,17,18]]
	for i in range(4):
		t = threading.Thread(target=task, args=(data[i],q))
		t.start()
		threads.append(t)

	for t in threads:
		t.join()

	results = []
	for _ in range(4):
		results.append(	q.get())
	
	print(results)

if __name__ == '__main__':
	main()

