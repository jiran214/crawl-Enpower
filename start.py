import random
from tkinter import *
import tkinter as tk
import tkinter.messagebox as msg
from spider import weibo_spider
from spider import bili_spider
import paint
import easyDL
def root1():
    def ini():
        Lstbox1.delete(0, END)
        list_bv = [
            'BV1No4y1S7TT', 'BV1J54y1J7kD', 'BV1JU4y1n7AJ',
            'BV1Yo4y1Q71P', 'BV1Jy4y1j79i', 'BV1tb4y1r7Wv',
            'BV1bv411n7yN', 'BV1764y167Lp', 'BV1qg411M7ND',
            'BV1CU4y137FJ', 'BV1VB4y1K7eL', 'BV15L411p7M8',
            'BV1L64y1t7ks', 'BV1Wv411n7FK',
            'BV1iM4y1K7DH', 'BV1Xb4y1k714', 'BV1KL411p7PA'
        ]
        for i in range(3):
            a=random.randint(1, 17)
            Lstbox1.insert(END, list_bv[a])

    def clear():
        Lstbox1.delete(0, END)

    def ins():
        if entry.get() != '':
            if Lstbox1.curselection() == ():
                Lstbox1.insert(Lstbox1.size(), entry.get())
            else:
                Lstbox1.insert(Lstbox1.curselection(), entry.get())
            global bv_list
            bv_list = list(Lstbox1.get(0, Lstbox1.size()))
            global community
            community = var_community.get()


    def delt():
        if Lstbox1.curselection() != ():
            Lstbox1.delete(Lstbox1.curselection())

    root = Tk()
    root.title('爬虫')
    sw = root.winfo_screenwidth()
    # 得到屏幕宽度
    sh = root.winfo_screenheight()
    # 得到屏幕高度
    ww = 950
    wh = 540
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    root.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    label = Label(root, text="基于 EasyDL 文本的网络环境维护系统", font=('heiti', 20), fg='red', bg='pink')
    label.place(x=225, y=75)
    label = Label(root, text="作者：Jiran               QQ:593848579", font=('heiti', 10), fg='red', bg='pink')
    label.place(x=595, y=427)

    #输入
    frame1 = Frame(root,relief=RAISED)
    frame1.place(relx=0.25,rely=0.25)
    frame2 = Frame(root,relief=GROOVE)
    frame2.place(relx=0.08,rely=0.25)
    Lstbox1 = Listbox(frame1,width=30,height=15 )
    Lstbox1.pack()


    l= tk.Label(frame2, bg='yellow', width=20, text='请选择社区')
    l.pack()
    # 第定义选项触发函数功能

    entry = Entry(frame2,width=20)
    entry.pack()
    #option
    var_community = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
    r1= tk.Radiobutton(frame2, text='Bilibili', variable=var_community, value='Bilibili')
    r1.pack()
    r2= tk.Radiobutton(frame2, text='微博', variable=var_community, value='微博')
    r2.pack()


    btn1 = Button(frame2,text='随机',command=ini)
    btn1.pack(fill=X)

    btn2 = Button(frame2,text='添加',command=ins)
    btn2.pack(fill=X)

    btn5 = Button(frame2,text='删除',command=delt)
    btn5.pack(fill=X)

    btn6 = Button(frame2,text='清空',command=clear)
    btn6.pack(fill=X)

    def parse():
        print('11111')
        global bv_list
        bv_list=list(Lstbox1.get(0, Lstbox1.size()))
        global community
        community= var_community.get()
        try:
            if community =='Bilibili':
                b=bili_spider.Bili_commentspider(bv_list)
                b.comment_parse()
            else:
                w=weibo_spider.WeiboCommentCrawer(bv_list)
                w.crawl_comment()
        except Exception as e:
            msg.showerror(title='error_parse', message=e)  # 提示信息对话窗
            return
            # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
            # tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
        msg.showinfo(title='Hi', message='爬取结束，数据已录入数据库')  # 提示信息对话窗

        #增加提示成功爬取功能
    btn4 = Button(frame2,text='爬取数据',command=parse)
    btn4.pack(fill=X)

    #显示框和功能选择框
    Lstbox2 = tk.Listbox(root, width=30,height=15)
    Lstbox2.grid(row=2, column=3,padx=650,pady=135)
    frame3= Frame(root,relief=GROOVE)
    frame3.place(relx=0.515,rely=0.25)
    list_var=[]
    v1=IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()
    v5 = IntVar()
    v6 = IntVar()
    l1= tk.Label(frame3, bg='yellow', width=20, text='请选EasyDL工具：')
    l1.pack(fill=X)
    c1= tk.Checkbutton(frame3, text='情感倾向度分析',variable=v1)   # 传值原理类似于radiobutton部件
    c1.pack(fill=X)
    c2= tk.Checkbutton(frame3, text='相似谣言搜寻',variable=v2)
    c2.pack(fill=X)
    entry1 = Entry(frame3, width=20)
    entry1.pack()
    c3= tk.Checkbutton(frame3, text='隐私判断分析',variable=v3)   # 传值原理类似于radiobutton部件
    c3.pack(fill=X)
    c4= tk.Checkbutton(frame3, text='谣言判断分析',variable=v4)
    c4.pack(fill=X)
    c5= tk.Checkbutton(frame3, text='广告判断分析',variable=v5)   # 传值原理类似于radiobutton部件
    c5.pack(fill=X)
    c6= tk.Checkbutton(frame3, text='敏感言论分析',variable=v6)
    c6.pack(fill=X)

    def data_analysis():
        e=easyDL.Easydl(community=community)
        try:
            if v1.get()==1:
                Lstbox2.insert(Lstbox1.size(), '情感倾向度分析中。。。\n')
                e.emo_request()
                Lstbox2.insert(Lstbox1.size(), '情感倾向度分析over\n')
            if v2.get()==1:
                if entry1.get()!='':
                    Lstbox2.insert(Lstbox1.size(), '相似谣言搜寻中。。。\n')
                    text=entry1.get()
                    e.similar_request(text)
                    Lstbox2.insert(Lstbox1.size(), '相似谣言搜寻over\n')
                else:
                    msg.showerror(title='analy_error', message="请输入相似文本")
            if v3.get()==1:
                Lstbox2.insert(Lstbox1.size(), '隐私判断分析中。。。\n')
                e.secrecy_request()
                Lstbox2.insert(Lstbox1.size(), '隐私判断分析over\n')
            if v4.get()==1:
                Lstbox2.insert(Lstbox1.size(), '谣言判断分析中。。。\n')
                e.rumor_request()
                Lstbox2.insert(Lstbox1.size(), '谣言判断分析over\n')
            if v5.get()==1:
                Lstbox2.insert(Lstbox1.size(), '广告判断分析中。。。\n')
                e.advertise_request()
                Lstbox2.insert(Lstbox1.size(), '广告判断分析over\n')
            if v6.get()==1:
                Lstbox2.insert(Lstbox1.size(), '敏感言论分析中。。。\n')
                e.sense_request(0.5)
                Lstbox2.insert(Lstbox1.size(), '敏感言论分析over\n')
            msg.showinfo(title='analy_info',message='数据分析完毕，请进入可视化页面')
        except Exception as e:
            msg.showwarning(title='analy_warn', message=str(e))  # 提示信息对话窗
            return
    btn6 = Button(frame3,text='开始',command=data_analysis)
    btn6.pack(fill=X)
    btn7 = Button(frame3, text='数据可视化页面', command=lambda:[root.destroy(),root2()])
    btn7.pack(fill=X)
    root.mainloop()



def root2():
    root2 = Tk()
    root2.title('数据分析处理')
    sw = root2.winfo_screenwidth()
    # 得到屏幕宽度
    sh = root2.winfo_screenheight()
    # 得到屏幕高度
    ww = 950
    wh = 540
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    root2.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
    #1
    frame1 = Frame(root2, relief=GROOVE)
    frame1.place(relx=0.1, rely=0.29)
    l = tk.Label(frame1, bg='yellow', width=20, text='【可视化】')
    l.pack()
    l1 = tk.Label(frame1, bg='yellow', width=20, text='请选择图表：')
    l1.pack()
    v=IntVar()
    r1 = tk.Radiobutton(frame1, text='情感倾向', variable=v,value=1)
    r1.pack()
    r2 = tk.Radiobutton(frame1, text='相似谣言', variable=v,value=2)
    r2.pack()
    r3 = tk.Radiobutton(frame1, text='隐私判断', variable=v,value=3)
    r3.pack()
    r4 = tk.Radiobutton(frame1, text='谣言判断', variable=v,value=4)
    r4.pack()
    r5 = tk.Radiobutton(frame1, text='广告判断', variable=v,value=5)
    r5.pack()
    r6 = tk.Radiobutton(frame1, text='敏感言论判断', variable=v,value=6)
    r6.pack()
    r7 = tk.Radiobutton(frame1, text='综合分析', variable=v,value=7)
    r7.pack()
    def root3():
        root3 = Tk()
        root3.title('图表生成器')
        sw = root3.winfo_screenwidth()
        # 得到屏幕宽度
        sh = root3.winfo_screenheight()
        # 得到屏幕高度
        ww = 230
        wh = 185
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        root3.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

        Label(root3, text='请填写图标信息：').grid(row=0, column=0, columnspan=2)
        Label(root3, text='title：').grid(row=1, column=0, sticky=E)
        title = Entry(root3)
        title.grid(row=1, column=1)
        Label(root3, text='ylim：').grid(row=2, column=0, sticky=E)
        ylim = Entry(root3)
        ylim .grid(row=2, column=1)
        Label(root3, text='xlabel：').grid(row=3, column=0)
        xlabel = Entry(root3)
        xlabel.grid(row=3, column=1)
        Label(root3, text='label1：').grid(row=4, column=0, sticky=E)
        label1 = Entry(root3)
        label1.grid(row=4, column=1)
        Label(root3, text='label2：').grid(row=5, column=0)
        label2 = Entry(root3)
        label2.grid(row=5, column=1)
        # label1, label2, xlabel,ylim, title=0
        btn1 = Button(root3, text='生成数据分析图', command=lambda: [paint.tx_paint( bv_list=bv_list,scorenum=v.get(), label1=label1.get(),
                                                                              label2=label2.get(), xlabel=xlabel.get(),title=title.get()
                                                            , ylim=ylim.get(), community=community),root3.destroy])
        btn1.grid(row=6, column=0, columnspan=2)

    btn1 = Button(frame1, text='生成数据分析图', command=root3)
    btn1.pack(fill=X)
    btn2 = Button(frame1, text='返回上一级', command=lambda:[root2.destroy(),root1()] )
    btn2.pack(fill=X)
    btn3 = Button(frame1, text='退出', command=root2.destroy)
    btn3.pack(fill=X)

    #4
    frame4 = Frame(root2, relief=RAISED)
    frame4.place(relx=0.3, rely=0.15)

    v1=StringVar()
    s = tk.Scale(frame4, label='请选择违规阈值（越👉范围越大）', from_=0, to=1, orient=tk.HORIZONTAL, length=300, showvalue=0, tickinterval=0.2,
                 resolution=0.01,variable=v1)
    s.pack()
    l = tk.Label(frame4, bg='green', fg='white', width=20, text='违规用户显示框')
    l.pack()
    Lstbox3 = Listbox(frame4, width=80, height=12)
    Lstbox3.pack()
    def search():
        try:
            Lstbox3.delete(0, END)
            list_user=easyDL.Easydl(community).search(float(v1.get()))
            print(list_user)
            for x in list_user:
                print(x)
                Lstbox3.insert(Lstbox3.size(), x)
        except Exception as e:
            msg.showwarning(title='search_warn', message=str(e))  # 提示信息对话窗
            return

    btn1 = Button(frame4, text='查找违规用户', command=search,width=20)
    btn1.pack()
    def info():
        msg.showinfo(title='sorry',message="功能开发中...")
    btn2 = Button(frame4, text='自动举报', command=info,width=20)
    btn2.pack()
    btn2 = Button(frame4, text='提交平台', command=info,width=20)
    btn2.pack()
    root2.mainloop()

if __name__ == '__main__':
    root1()
