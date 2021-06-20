import socket
from tkinter.constants import COMMAND
import os
import tkinter as tk



def click_yes():
     data = '1'
     conn.send(data.encode())
     str = 'x11vnc'
     os.system(str)    
     sock.close()


def click_no():
    data = '0'
    conn.send(data.encode())
    sock.close()

def menu():
    window = tk.Tk()
    window.geometry('250x180')
    lb1 = tk.Label(window, text="Разрешить подключение?", font=("Arial Bold", 15))
    lb1.grid(column=0, row=0)

    btn = tk.Button(window, text="Да", height=3, width=5,command=click_yes)
    btn.grid(column=0, row=1)

    btn2 = tk.Button(window, text="Нет", height=3, width=5,command=click_no)
    btn2.grid(column=0, row=2)

    window.mainloop()
def connect():
    menu()
    


sock = socket.socket()
sock.bind(('0.0.0.0', 9095))
sock.listen(1)
conn, addr = sock.accept()
connect()





