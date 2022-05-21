import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 7
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)


def click_about():
    messagebox.showinfo('만든이 : 이준혁', '피지컬컴퓨팅 v0.1')


def click_fire():
    print('Starting Measurement...')

    GPIO.output(TRIG, 1)
    time.sleep(0.001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        pass
    start = time.time()

    while GPIO.input(ECHO) == 1:
        pass
    stop = time.time()

    print((stop - start) * 17000)
    messagebox.showinfo('물체와의 거리는 {}cm 입니다.'.format(round((stop-start) * 17000)))

    GPIO.cleanup()

    # 물체와의 거리는 ??cm 입니다. 팝업창 출력

root = tk.Tk()
root.title('메뉴 : 초음파센서')
root.geometry('300x200')

m_menubar = tk.Menu(root)
m_file = tk.Menu(m_menubar, tearoff=0)
m_menubar.add_cascade(label='File', menu=m_file)
m_file.add_command(label='Fire', command=click_fire)
m_file.add_command(label='Exit', command=exit)

m_help = tk.Menu(m_menubar, tearoff=0)
m_menubar.add_cascade(label='Help', menu=m_help)
m_help.add_command(label='About', command=click_about)

root.config(menu=m_menubar)
root.mainloop()