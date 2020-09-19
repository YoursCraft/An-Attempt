import time,os
while True:
        key=input('请输入密码')
        realkey='kuaile'
        if key==realkey:
                scale = 20
                print("------时空机器开始运转------")
                for i in range(scale+1):
                    a, b = '**' * i,'..' * (scale - i)
                    c = (i/scale)*100
                    print("\r{:^3.0f}％[{}->{}]" .format (c, a, b),end='')
                    time.sleep(0.1)
                print("\n------执行结束------\n")
                print('欢迎进入快乐星球')
                time.sleep(3)
                #os.system('xingqiu.jpg')
                break
        else:
                print('密码错误\n')
