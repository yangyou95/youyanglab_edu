# 优扬实验室网站项目

## 1. 工具/技术
### UI
* Bootstrap
* Animate.css
* Vue.js

### web框架
* Django

## 2. 项目时间节点 （2月15日前）

### 前端
- [x] 首页前端页面搭建
- [x] 课程概览前端页面搭建
- [ ] 课程具体内容页面搭建
- [ ] 用户个人中心界面搭建
- [ ] 注册及登录界面搭建
### 后端及数据库
- [ ] 用户注册与登陆逻辑程序
- [ ] 课程信息模型
- [ ] 课程章节信息模型
- [ ] 课程具体内容信息模型
- [ ] 用户与课程内容链接模型，存储学习进度
- [ ] 管理端平台

## 尤扬
  1. 负责后端相关逻辑程序搭建
  2. 参与前端设计工作
## 许人文
  1. 使用Bootstrap相关模板
  2. 用户注册登录界面设计
  3. 用户个人中心设计
## 张钊
  1. 准备视频教学素材
  2. 搭建数据库结构   


## 3. 项目进度
### 尤扬

* 完成了简单用户注册的逻辑程序

### 许人文

* 完成了个人中心页面设计

## 4. Django使用手册
### 前端Render文件的位置及索引
1. 前端html文件放在“根目录/webapp/templates/webapp"里, 在html文件中引入静态库tag **{% load static %}**
2. 前端文件的css，放在“根目录/webapp/static/webapp"里, 在html文件中以 **href="{% static "webapp/css文件名.css" %}"** 方式索引
3. 前端的图片文件，放在“根目录/webapp/static/webapp/images"里，同理索引图片
### Render的后端逻辑程序
1. 定义url，在“根目录/webapp/urls.py"里, 定义方式如 **path('userpage/',views.userpage, name = "user_url")**
2. 定义模型文件，在“根目录/webapp/views.py"里，简单方式用函数即可，return一个针对前端html页面的render。


### 本地端编译
1. Python3 环境
2. Python3 环境下 安装django，django_heroku
3. 在项目根目录下打开终端，输入python3 manange.py runserver，即可在本地端调试网站程序
4. 注意需要在本地PATH中添加SECRET_KEY的变量

### 相关BUG解决
1. 针对django_heroku库的无法安装
    - 解决办法，终端输入 sudo apt install libpq-dev

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