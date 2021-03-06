# 优扬实验室网站项目

## 1. 工具/技术
### UI
* Bootstrap
* Animate.css
* Vue.js

### web框架
* Django

## 2. 项目细分

### 前端
- [x] 首页前端页面搭建
- [x] 课程概览前端页面搭建
- [ ] 课程具体内容页面搭建
- [x] 用户个人中心界面搭建
- [x] 注册及登录界面搭建
### 后端及数据库
- [x] 用户注册与登陆逻辑程序
- [x] 课程信息模型
- [x] 课程章节信息模型
- [x] 课程具体内容信息模型
- [ ] 用户与课程内容链接模型，存储学习进度
- [x] 管理端平台




## 3. 当前问题
### 尤扬

* 忘记找回密码机制

### 许人文 

* 登陆页面用户名或密码错误提醒
* 

## 4. Django使用手册
### 前端Render文件的位置及索引
1. 前端html文件放在“根目录/webapp/templates/webapp"里, 在html文件中引入静态库tag **{% load static %}**
2. 前端文件的css，放在“根目录/webapp/static/webapp"里, 在html文件中以 **href="{% static "webapp/css文件名.css" %}"** 方式索引
3. 前端的图片文件，放在“根目录/webapp/static/webapp/images"里，同理索引图片
### Render的后端逻辑程序
1. 定义url，在“根目录/webapp/urls.py"里, 定义方式如 **path('userpage/',views.userpage, name = "user_url")**
2. 定义模型文件，在“根目录/webapp/views.py"里，简单方式用函数即可，return一个针对前端html页面的render。

### 后端与数据库操作
1. 数据模型定义在models.py
2. 前端从数据库中调取数据包括参数传递逻辑在views.py (需要import对应的模型)
3. 需要在admins.py中import对应模型并register


### 本地端编译
1. Python3 环境
2. Python3 环境下 安装django，django_heroku
3. 在项目根目录下打开终端，输入python3 manange.py runserver，即可在本地端调试网站程序
4. 注意需要在本地PATH中添加SECRET_KEY的变量, 设置HOST邮箱帐号及密码

### 相关BUG及问题
1. 目前用户点击注册后，在等待完成发送邮件跳转到新页面前，等待时间比较长，需要做
    * 有一个加载效果让用户知道目前请求正在处理
    * 需要保证在提交过后，加载过程中，submit按钮出于不可激活状态，防止用户以为卡住重复点击
    

### 可参考的资料，想法
1. 用户注册认证逻辑
  - https://www.jianshu.com/p/502c66aca85d
2. 类似优秀网站
  - brilliant
  - https://zzax.io/course/
3. 管理端需要一个编写文章（课程小节）的网页，其功能包括
  - 提供按顺序添加标题，文章内容，选择题，图片等选项
  - 完成后选择加入的课程->章节->小节里
  - 参考一些教学网站的markown风格样式，pagedown。
  - 参考https://pandao.github.io/editor.md/
