"""
作者：冯永信
时间：2020.2.15
开发版本：Python 3.7.5
"""

'''
该版本使用dict字典类型存储用户注册登录等数据
修复了上个版本的一些不知名BUG
'''

#导入os模块与time模块
import os,time

#全局变量name用于获得昵称，users字典用于存储注册用户信息,fyx属于内测用户
name=''
users={
    'fyx':{'username':'fyx','password':'123','nickname':'信哥哥'}
}

#第一层循环，加载首页界面
while True:
    os.system('cls')
    print('\n      这是一个网上商城')
    print('---------------------------')
    print('      1.会员登录')
    print('      2.用户注册')
    print('      3.退出系统')
    print('---------------------------')

    x=input('请输入您的选项：')

    #第二层循环，开始进入选择结构
    while True:
        if x=='1':
            os.system('cls')
            username=input('\n请输入账号：')
            password=input('请输入密码：')
            
            #先查询账号是否存在
            if username in users:

                #获取users字典下对应username的value——u
                u=users.get(username)
                #判断密码是否一致
                if u.get('password')==password:
                    print('\n登陆成功！！！2秒后进入游戏商城！！！')
                    time.sleep(2)

                    #name值将用于进入商城界面
                    name=u.get('nickname')
                    break

                else:
                    print('\n密码出错了。。。')
                    print('   1.重试输入')
                    print('   2.注册账号')
                    s=input('您选择：')

                    if s=='1':
                        #continue语句将重新加载第二层while循环
                        continue
                    elif s=='2':
                        #break语句将会使程序跳出第二层while循环，继续向下运行第一层while循环
                        break
            
            #账号不存在或未找到
            else:
                print('\n账号输入有误。。。')
                print('   1.重试输入')
                print('   2.注册账号')
                s=input('您选择：')

                if s=='1':
                    #continue语句将重新加载第二层while循环
                    continue
                elif s=='2':
                    #break语句将会使程序跳出第二层while循环，继续向下运行第一层while循环
                    break
                            
        elif x=='2':
            os.system('cls')
            print('\n这里是注册界面：')

            #创建一个空字典user用于向users中添加
            user=dict()
            uname=input('请输入账号：')
            user.setdefault('username',uname)

            #查看users中是否存在uname这个key，有则退出
            if uname in users:
                print('该账号已被注册！！！2秒后返回主页！！！')
                time.sleep(2)
                break
            
            #添加数据到users中
            else:
                pwd=input('请输入密码：')
                user.setdefault('password',pwd)
                nickname=input('请输入昵称：')
                user.setdefault('nickname',nickname)
            
                #将user添加到users中
                users.setdefault(uname,user)
                print('注册成功,2秒后将进入登录界面：')

                #清空name，防止混淆（修复了上个版本混淆登录的BUG）
                name=''

                time.sleep(2)
                #break语句将会使程序跳出第二层while循环，继续向下运行第一层while循环
                break

        else:
            print('您离开了。。。')
            exit()

    #if语句判断name是否为空值，不为空则代表着登录成功，进入网上商城
    if name!='' and name!=None:
        os.system('cls')
        print('\n      欢迎%s进入网上商城' % name)
        print('---------------------------')
        print('      1.英雄皮肤商城')
        print('      2.英雄装备商城')
        print('      3.返回登录菜单')
        print('      4.退出系统')
        print('---------------------------')
        
        n=input('请输入您的选项：')

        #该循环在第二层while循环结束后运行
        while True:

            if n=='1':
                os.system('cls')
                print('\n您进入了英雄皮肤商城！！！')
                print('因为作者太懒了，后面没写。。。')
                print('您离开了。。。')
                exit()

            elif n=='2':
                os.system('cls')
                print('\n您进入了英雄装备商城！！！')
                print('因为作者太懒了，后面没写。。。')
                print('您离开了。。。')
                exit()

            elif n=='3':
                os.system('cls')
                print('\n您选择回头！2秒后回到登录菜单界面！')
                time.sleep(2)
                #跳出自身循环后将重新进入到第一次循环
                break

            else:
                print('您离开了。。。')
                exit()

    else:
        continue
    