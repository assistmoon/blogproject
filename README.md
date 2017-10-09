# MY DJANGO TEST
这是一个Django练习项目，使用的是Django 1.10 和 Python 3.5
1.  查看python版本：命令行输入：python -V
2.  搭建虚拟环境Virtualenv：pip install virtualenv;
将新的虚拟环境安装到指定目录下：virtualenv C:\Users\pc\envs\blogproject_env
激活虚拟环境：C:\Users\pc\envs\blogproject_env\Scripts\activate
3.  安装Django：在虚拟目录下：pip install django==1.10.6
4.  建立Django工程：进入指定目录：cd C:\Users\pc\workspace
5.  运行命令创建工程blogproject：django-admin startproject blogproject
6.  运行:在manage.py所在目录：python manage.py runserver 开启web服务器
浏览器输入：http://127.0.0.1:8000，验证Django启动
7.  将界面换成中文：在settings.py中，修改语言和时区，找到LANGUAGE_CODE = 'zh-hans' TIME_ZONE = 'Asia/Shanghai'
8.  建立博客应用：激活虚拟环境；进入manage.py目录;运行创建blog命令：
python manage.py startapp blog
9.  注册blog应用：在settings.py中，INSTALLED_APPS加入:'blog',
10. 编写博客模型models.py代码
