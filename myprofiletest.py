# -*- coding: utf-8 -*-
import time

def sleep():
    time.sleep(1)

def main():
    i=0
    sleep()
    while i<10000:
        i+=1

if __name__ == '__main__':
    main()
