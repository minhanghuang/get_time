
# 发布PyPI(简单)


## #0 GitHub

```
https://github.com/Coxhuang/get_time
```

## #1 环境

```
Python3.6
twine==1.13.0 # 需要pip下载 
```

## #2 准备

### #2.1 注册PyPI账号

```
https://pypi.org/
```

### #2.2 安装环境

```
pip3 install twine
```

## #3 开始

### #3.1 新建文件夹

```
.
├── get_time # 文件夹
│   └── __init__.py # 把需要发布的代码放到里面
└── setup.py # 配置文件 
```

> __init__.py


```
import datetime, time
import calendar

now = datetime.datetime.now()


def get_time(year=now.year,
             month=now.month,
             day=now.day,
             hour=now.hour,
             minute=now.minute,
             second=now.second,
             week=-1,
             last_day_of_month=False,
             type="time",
             detail=True):
    """

    :param year: 年 (默认今年)
    :param month: 月 (默认当月)
    :param day: 天 (默认今天)
    :param hour: 时 (默认当前时间)
    :param minute: 分 (默认当前时间)
    :param second: 秒 (默认当前时间)
    :param week: 星期x (默认-1,如果不等于-1,则day参数无效)
    :param last_day_of_month: 每个月的最后一天 (默认False)
    :param type: 输出类型 (time / str)
    :param detail: 是否输出时分秒? (默认输出时分秒)
    :return: 时间 
    """

    if week != -1:
        weekday = datetime.datetime(year, month, day, hour, minute, second)

        one_day = datetime.timedelta(days=1)
        while weekday.weekday() != 0:
            weekday -= one_day

        ret = weekday + datetime.timedelta(days=week - 1)

    else:

        if last_day_of_month:  # 每个月的最后一天
            day = calendar.monthrange(year, month)[1]

        if not detail:
            date = datetime.date(year, month, day)
        else:
            date = datetime.datetime(year, month, day, hour, minute, second)

        ret = date if type == "time" else str(date)

    return ret


def get_timestamp(detail=True):
    """
    获取当前时间戳 
    :param detail: True输出完整的时间戳/ False输出前10位(小数点之前)
    :return: 时间戳 
    """
    if detail:
        ret = time.time()
    else:
        ret = int(time.time())
    return ret


def timestamp_to_str(timestamp, strformat):
    """
    时间戳转字符串
    :param timestamp: 时间戳 
    :param strformat: 转换格式 (%Y-%m-%d %H:%M:%S)
    :return: 时间字符串 
    """
    ret = time.strftime(strformat, time.localtime(timestamp)) 

    return ret


def str_to_timestamp(timestr, strformat):
    """
    字符串转时间戳 
    :param timestr: 时间字符串 
    :param strformat: 转换格式 (%Y-%m-%d %H:%M:%S) 
    :return: 时间戳 (前10位)
    """
    ret = int(time.mktime(time.strptime(timestr, strformat)))

    return ret
```

> setup.py


```
#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='get-time', # 项目的名称,pip3 install get-time
    version='0.0.4', # 项目版本 
    author='黄民航', # 项目作者 
    author_email='gmhesat@gmail.com', # 作者email 
    url='https://github.com/Coxhuang/get_time', # 项目代码仓库
    description='获取任意时间/获取当前的时间戳/时间转时间戳/时间戳转时间', # 项目描述 
    packages=['get_time'], # 包名 
    install_requires=[],
    entry_points={
        'console_scripts': [
            'get_time=get_time:get_time', # 使用者使用get_time时,就睡到get_time项目下的__init__.py下执行get_time函数
            'get_timestamp=get_time:get_timestamp',
            'timestamp_to_str=get_time:timestamp_to_str',
            'str_to_timestamp=get_time:str_to_timestamp',
        ]
    } # 重点
)

```

### #3.2 上传

> 打包

在项目的目录下(和刚刚新建setup.py同级目录)
```
python3 setup.py sdist build
```

![20190401170244-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190401170244-image.png)

> 上传

```
twine upload dist/*
```

![20190401170134-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190401170134-image.png)


![20190401170532-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190401170532-image.png)


### #3.3 测试

```
pip3 insatll get-time==0.0.4
pip3 list # 查看安装过的包
```
![20190401170741-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190401170741-image.png)

![20190401170904-image.png](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20190401170904-image.png)











