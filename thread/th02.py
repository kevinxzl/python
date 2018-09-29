#-*- coding: utf-8 -*-
import threading
import time

def task1():
	print("1: This is a Thread, number is %s" %threading.current_thread())
	print("1. active threading count:%d" %threading.active_count())
	print("1. threading enumerate:%s" %threading.enumerate())
	print("1. current thread: %s" %threading.current_thread())

	time.sleep(2)   


def main():
	print("Create a thread")
	thread1 = threading.Thread(target=task1())
	thread1.start()
	print("This is main thread")

if __name__ == '__main__':
	main()

