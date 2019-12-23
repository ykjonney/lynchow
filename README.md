一个以 Django 作为框架搭建的个人博客。

博客主页 http://www.lynchow.com/

## 使用步骤：

### 必须的支持项
- Python3.4 以上
- redis 服务启动了，因为2018-4-18增加了django-redis缓存，所以必须要有redis了
- MySQL
- 其他依赖看依赖文件即可

### 创建网站关键信息文件
由于涉及到网站的一些隐私信息，所以这个项目有一个文件没有上传到Github中，所以要在克隆项目之后自己创建这个文件。
在settings.py文件所在的文件夹下创建一个base_settings.py文件，然后在里面写入如下代码：
```
# -*- coding: utf-8 -*-
# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}
# 邮箱配置
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'your-email@163.com'
EMAIL_HOST_PASSWORD = 'your-password'  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = 465  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
DEFAULT_FROM_EMAIL = 'your-webname <your-email@163.com>'

# 网站默认设置和上下文信息
SITE_END_TITLE = '网站的名称，如TendCode'
SITE_DESCRIPTION = '网站描述'
SITE_KEYWORDS = '网站关键词，多个词用英文逗号隔开'
```

### 创建数据库

首先在自己的电脑上面创建一个数据库，根据配置信息里面填写的数据库信息去创建。比如数据库的名字为izone,那么我建议你使用下面这段MySQL的语句，注意，创建的数据库的编码格式是utf8mb4，原因是我的博客中支持emoji表情，所以必须使用这个格式才行：
```
CREATE DATABASE name DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```

### Exception

第三方登录模块还未做相关处理，找回密码功能不记得有没有修复bug。

