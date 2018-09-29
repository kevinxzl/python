import threading
from multiprocessing import cpu_count

def main():
	print("1. active threading count:%d" %threading.active_count())
	print("2. threading enumerate:%s" %threading.enumerate())
	print("3. current thread: %s" %threading.current_thread())
	
	print("4. cpu count:%d "%cpu_count())
 


if __name__ == '__main__':
	main()
