import tkinter as tk




window = tk.Tk()
window.title('天津市科普嘉年华 定向验证系统')
window.geometry('500x500')






var = tk.StringVar()    # 这时文字变量储存器
l = tk.Label(window, 
    textvariable=var,   # 使用 textvariable 替换 text, 因为这个可以变化
    bg='green', font=('Arial', 12), width=15, height=2)
l.pack() 





on_hit = False  # 默认初始状态为 False
def hit_me():
    global on_hit
    
    t.delete(0,11)
    print("send signal")
    
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空
        number = 999
# 这里是窗口的内容


number = tk.StringVar()

number.set("begin")

b = tk.Button(window, 
    text='hit me',      # 显示在按钮上的文字
    width=15, height=2, 
    command=hit_me)     # 点击按钮式执行的命令
b.pack()    # 按钮位置

def test():
    return False

def test2(content):
    #alter("111")
    #print("aaa");
    print("content is  ", content)
    length = len(content)

    print("input length is " , length)
    
    # if input is ok, then send signal and reset
    if length == 20:
        print("Send signal")
        print("tes for kkk ")
        return True
    else:
        return True
test_cmd = window.register(test2)  # 需要将函数包装一下，必要的

#t = tk.Entry(window,textvariable=number,validate="key", validatecommand=(test_cmd,"%P"))

def listen(event):
    print("you enter the key for -- ", event.char)
    
    current_key = event.char

    if current_key.isalnum():


        content = t.get()+event.char
        #t.delete(0,11)
        print("The content is ", content)
        if(len(content) ==10):
            
            print("Send sigal")
            t.delete(0,11)
            return "break"
        
    else:
        print("input not number or alphbit")
        pass

    #print(t.get()+event.char)
    
    #content = t.get()+event.char


    #if len(content)==10:
    #    print('------  it is limit  -----')
    #    #hit_me()
    #    t.delete(0,11)
    #    return "break"
t=tk.Entry(window)
t.bind('<Key>', listen)

t.pack()


window.mainloop()
