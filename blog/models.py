from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    Django 要求模型必须继承 models.Model类。
    Category 只需要一个简单的分类名name就可以了
    CharField 指定了分类名name的数据类型，CharField 是字符类型

    """
    name = models.CharField(max_length = 100)

class Tag(models.Model):
    """
    标签Tag也比较简单，和Category一样。

    """
    name = models.CharField(max_length = 100)

class Post(models.Model):
    """
    文章的数据库表稍微复杂点，主要是涉及字段多
    """

    #文章标题
    title = models.CharField(max_length=70)

    #文章正文，我们使用了TextField。
    #存储比较短的字符串可以使用CharField,但对于文章正文来说，可能是一段文本，因此使用TextField来存储大段文本
    body = models.TextField()

    #这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用DateTimeField类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    #文章摘要，可以没有文章摘要，但默认情况下CharField要求我们必须存入数据，否则就会报错
    #指定CharField的blank=True参数值后就可以允许空值了
    excerpt =models.CharField(max_length=200,blank=True)

    #这是分类与标签，分类与标签的模型我们已经定义在上面
    #我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同
    #我们规定一篇文章只能对应一个分类，但是一个分类下面可以有多篇文章，所以我们用的是ForeignKey，即一对多的关联关系
    #对于标签，一篇文章可以有多个标签，同一标签下也可以有多篇文章，所以我们使用ManyToManyField，表明这是多对多的关联关系
    #哦那个是我们规定文章可以没有标签，因此为标签tags制订了blank=True
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank = True)

    #文章作者，这里User是从django.contrib.auth.models导入的
    #django.contrib.auth是Django内置的应用，专门用于处理网站用户的注册、登录等流程，User是Django为我们已经写好的用户模型
    #这里我们通过ForeignKey把文章和User关联起来
    #因为我们规定一篇文章只能有一个作者，而一个作者可能会写很多文章，因此关联是一对多
    author = models.ForeignKey(User)
