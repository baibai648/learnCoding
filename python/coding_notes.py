#A notebook for python coding rules
#consider use markdown to format this file

DOCSTRING RULES
    - 第一行用于简洁描述该函数或类的功能
    - 第二行空白
    - 第三行开始详细描述函数参数及返回值

内置函数
    - all, any, filter, map, zip, *zip

PYTHON IO
    - input()
    - 格式化打印(pyton3 中用于替代%)
        - f'the url of {site} is :{url}'
            - site & url here are parameters or functions
        - f'{name:10}:{age:5}'
            - use fixed length to make print looks tidy
        - ''.format() used to replace %
            - print('{name} is {age}'.format(name='Tom',age=23))
            - persons = {'Tom':23,'Jack':29}
              print ('Tom:{0[Tom]:d},Jack:{0[JACK]}'.format(persons))
        - 'abc'.rjust(6)/'abc'.center()/.ljust()
            - '{:*^30}'.fromat('centered')   #use '*' as a fill char and center aligned
            - '{:>30}'     #right aligned
            - '{:<30}'     #legt aligned

#below is a code cell block
print('what now')
import numpy as np
for i in np.arange(3):
    print (i)



# another cell below
文件修改
    - open()
        - 始终用如下格式打开文件，好处是具体结束后文件正确关闭
            - with open('myfile') as f:
                  data = f.read()
    - 一些常用函数
        - f.read(size)     size不确定的话读取所有行
        - f.readline()     读一行
        - f.readlines()    读所有行并返回列表
        - f.seak(cookie,whence)  设置当前文件位置，比如0回到开头
            - cookie 位置偏移量，不确定实际意义
            - whence 相对位置 0 开头；1当前位置；2文件末尾
        - f.tell()         查看当前位置

MATPLOTLIB
    - .plot(data,'ko--',drawstyle='step-post')
