from django.db import models

# Create your models here.


class Grade(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的主键
    classname = models.CharField(max_length=32)  #班级名


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=24)
    grade = models.ForeignKey(to=Grade)  # 外键关联Publisher这张表


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher_name = models.CharField(max_length=24)
    # ORM创建多对多字段，会自动在数据库中创建第三张表
    grades = models.ManyToManyField(to=Grade)



