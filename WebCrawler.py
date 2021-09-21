# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:45:30 2021

@author: jerry
lotto 爬蟲
"""
from threading import Thread
import tkinter as tk
from tkinter import ttk

import BingoBingo as BB
from BingoBingo import BingoBingo, data_extract

def closing():
    msb = tk.messagebox.askquestion('Quit','結束程式?')
    if msb == 'yes':
        win.destroy()
        
def clearWin():
    Text2_1.delete('1.0','end') #清除字首到字尾

def getdata_thread():
    do = Thread(target=getdata)
    do.start()

def getdata():
    
    global data_dict
    website = "https://www.taiwanlottery.com.tw/lotto/bingobingo/drawing.aspx"
    
    bingo = BingoBingo(website)
    # 抓取某天網頁資料
    soup = bingo.web_data(int(Entry1_1.get()), int(Entry1_2.get()))
    # 得到賓果每期主要資訊
    data = data_extract(soup)
    # 將資料經處理後輸出成字典
    data_dict = data.data_dict()
    Text2_1.insert('end',
                   "已載入{0}月{1}號資料...\n".format(int(Entry1_1.get()), int(Entry1_2.get())))
    Button3_1.config(state="normal")

def main_thread():
    main = Thread(target=main_work)   
    main.start()     
        
def main_work():
    
    # 存取使用者獎號
    entry = [Entry3_1.get(), Entry3_2.get(), Entry3_3.get(), Entry3_4.get(), Entry3_5.get(), 
             Entry3_6.get(), Entry3_7.get(), Entry3_8.get(), Entry3_9.get(), Entry3_10.get()]
    user_num = []
    for i in entry:
        if i == '' or int(i) == 0:
            pass
        else:
            user_num.append(int(i))
    # 期數
    terms = list(range(int(Entry2_1.get()), int(Entry2_2.get())+1))
    
    for i in terms:
        win = 0
        for j in range(len(user_num)):
            if user_num[j] in data_dict[i]:
                win+=1
        Text2_1.insert('end', "第{0}期: 中{1}個\n".format(i, win))
        Text2_1.see('end')

#　========= GUI ==========
# 建立視窗物件
def main_GUI():
    global win, Entry1_1, Entry1_2, Entry2_1, Entry2_2, Entry3_1, Entry3_2, Entry3_3, Entry3_4
    global Entry3_5, Entry3_6, Entry3_7, Entry3_8, Entry3_9, Entry3_10, Text2_1, Button3_1
    win = tk.Tk() 
    path_ = tk.StringVar()
    win.tk.call('tk', 'scaling', 2.0)
    win.title('BingoBingo對獎') # 賦予標題名稱
    win.geometry('400x400+500+150') # 設定視窗大小 
    win.resizable(0,0) # X, Y方向調整視窗
    win.iconbitmap("bingo.ico")#圖標
    win.config(bg="#b7b7a4") # 背景顏色
    win.protocol("WM_DELETE_WINDOW", closing) #視窗關閉提示
    
    # ======== window content =============
    win_top = tk.Label(win,                                  
                       text="歡迎使用賓果對獎",
                       font=('Microsoft JhengHei UI', 12, 'bold'), bg="#b7b7a4")
    win_top.place(x=100, y=0)#標籤位置
    
    # ------frame 1--------
    Frame1 = tk.Frame(win, bg="#b7b7a4",
                      width=400, height=160) # 建立frame區塊
    Frame1.place(x=0, y=35) #frame區塊位置
    #　輸入日期
    Label1_1 = tk.Label(Frame1, text='請輸入對獎日期 :', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label1_1.place(x=0, y=0)
    
    Entry1_1 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=3)
    Entry1_1.place(x=145, y=0)
    
    Label1_2 = tk.Label(Frame1, text='月 ', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label1_2.place(x=180, y=0)
    
    Entry1_2 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=3)
    Entry1_2.place(x=220, y=0)
    
    Label1_3 = tk.Label(Frame1, text='日', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label1_3.place(x=250, y=0)
    Button1_1 = tk.Button(Frame1, text='確認',
                          font=('Microsoft JhengHei UI', 8),
                          command=getdata_thread)
    Button1_1.place(x=330, y=0)
    
    #　輸入對獎期數
    Label2_1 = tk.Label(Frame1, text='請輸入對獎期數 :', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label2_1.place(x=0, y=40)
    
    Entry2_1 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=10)
    Entry2_1.place(x=145, y=40)
    
    Label2_2 = tk.Label(Frame1, text='~', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label2_2.place(x=235, y=40)
    
    Entry2_2 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                         width=10)
    Entry2_2.place(x=260, y=40)
    
    # 輸入獎號
    Label3_1 = tk.Label(Frame1, text='請輸入獎號 :', 
                          bg='#b7b7a4', fg="#2a2f25",
                          font=('Microsoft JhengHei UI', 9,'bold'))
    Label3_1.place(x=0, y=80)
    
    Entry3_1 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_1.place(x=110, y=80)
    
    Entry3_2 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_2.place(x=150, y=80)
    
    Entry3_3 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_3.place(x=190, y=80)
    
    Entry3_4 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_4.place(x=230, y=80)
    
    Entry3_5 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_5.place(x=270, y=80)
    
    Entry3_6 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_6.place(x=110, y=110)

    Entry3_7 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_7.place(x=150, y=110)
    
    Entry3_8 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_8.place(x=190, y=110)
    
    Entry3_9 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_9.place(x=230, y=110)
    
    Entry3_10 = tk.Entry(Frame1, font=('Microsoft JhengHei UI', 7),
                          width=4)
    Entry3_10.place(x=270, y=110)
    
    # 執行鈕
    Button3_1 = tk.Button(Frame1, text='兌獎',
                          font=('Microsoft JhengHei UI', 8),
                          command=main_thread)
    Button3_1.place(x=330, y=90)
    Button3_1.config(state="disable")
    
    # ----- frame2 -------
    Frame2 = tk.Frame(win, bg="#b7b7a4",
                      width=400, height=205) # 建立frame區塊
    Frame2.place(x=0, y=196) #frame區塊位置
    
    Text2_1 = tk.Text(Frame2, height=10, width=36,
                      font=('Microsoft JhengHei UI', 8),
                      fg='white', bg='#8B8682')
    Text2_1.place(x=70, y=0)
    
    Button2_1 = tk.Button(Frame2, text='清除',
                          font=('Microsoft JhengHei UI', 8),
                          command=clearWin)
    Button2_1.place(x=10, y=10)
    
    
    win.mainloop() # 視窗更新迴圈(必要存在)

main_GUI()

