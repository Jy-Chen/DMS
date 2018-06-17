"""day04 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #查看班级
    url(r'^grade/', views.grade),

    # 添加班级
    url(r'^add_grade/', views.add_grade),

    # 删除班级
    url(r'^del_grade/', views.del_grade),

    # 修改班级
    url(r'^change_grade/', views.change_grade),

    # 查看学生
    url(r'^student/', views.student),

    # 添加学生
    url(r'^add_student/', views.add_student),

    # 删除学生
    url(r'^del_student/', views.del_student),

    # 修改学生
    url(r'^change_student/', views.change_student),


    #查看老师
    url(r'^teacher/', views.teacher),

    #添加老师
    url(r'^add_teacher/', views.add_teacher),

    #删除老师
    url(r'^del_teacher/', views.del_teacher),

    #修改老师
    url(r'^change_teacher/', views.change_teacher),

    url(r'^addfile/', views.Addfile),

    # 默认页面
    url(r'^$', views.index),
]
