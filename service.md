# unbantu 16.04 LTS 作为服务器配置
1.  获取服务器ip地址：ifconfig
2.  服务器开启ssh：
  安装 open ssh:sudo apt-get install openssh-server
  修改root密码：sudo passwd root
  编辑文件 sudo vi /etc/ssh/sshd_config,找到：PermitRootLogin prohibit-password 禁用，添加：PermitRootLogin yes     ,sudo service ssh restart
  http://www.cnblogs.com/EasonJim/p/7189509.html
3.  ubuntu 16.04 启用root用户：http://blog.csdn.net/sunxiaoju/article/details/51993091
4.  安装Nginx 、python3、git、pip和virtualenv
