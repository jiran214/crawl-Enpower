import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('My Window')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x650')  # 这里的乘是小x
# label
l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack()  # Label内容content区域放置位置，自动调节尺寸# 放置lable的方法有：1）l.pack(); 2)l.place();
# text
e1= tk.Entry(window, show='*', font=('Arial',14))  # 显示成密文形式
e2= tk.Entry(window, show=None, font=('Arial',14)) # 显示成明文形式
e1.pack()
e2.pack()
#listbox
var2= tk.StringVar()
var2.set((1,2,3,4))# 为变量var2设置值
# 创建Listbox
lb= tk.Listbox(window, listvariable=var2) #将var2的值赋给Listbox
# 创建一个list并将值循环添加到Listbox控件中
list_items= [11,22,33,44]
for item in list_items:
    lb.insert('end', item) # 从最后一个位置开始加入值
lb.insert(1,'first')      # 在第一个位置加入'first'字符
lb.insert(2,'second')     # 在第二个位置加入'second'字符
lb.delete(2)               # 删除第二个位置的字符
lb.pack()
#在图形界面上创建一个标签label用以显示并放置
var= tk.StringVar()   # 定义一个var用来将radiobutton的值和Label的值联系在一起.
l= tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()
# 第定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + var.get())
#option
r1= tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2= tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3= tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()
#check button
var1= tk.IntVar() # 定义var1和var2整型变量用来存放选择行为返回值
var2= tk.IntVar()
c1= tk.Checkbutton(window, text='Python',variable=var1, onvalue=1, offvalue=0, command=print_selection)   # 传值原理类似于radiobutton部件
c1.pack()
c2= tk.Checkbutton(window, text='C++',variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()
#scale
def print_selection(v):
    l.config(text='you have selected ' + v)
s= tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.pack()
# # 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
# canvas= tk.Canvas(window, bg='green', height=500, width=500)
# # 说明图片位置，并导入图片到画布上
# image_file= tk.PhotoImage(file='C:/Users/ccc/Desktop/Snipaste_2021-07-23_14-33-11.png') # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
# image= canvas.create_image(300,-140, anchor='n',image=image_file)       # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# canvas.pack()


# 第5步，定义触发函数功能
def hit_me():
    # tkinter.messagebox.showinfo(title='Hi', message='你好！')  # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')       # 提出警告对话窗
    tkinter.messagebox.showerror(title='Hi', message='出错了！')         # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='Hi', message='你好！'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='Hi', message='你好！'))     # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='Hi', message='你好！'))  # return 'True', 'False'


# 第4步，在图形界面上创建一个标签用以显示内容并放置
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()
# 第6步，主窗口循环显示
window.mainloop()