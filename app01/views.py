from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.
from django.views import View
from day04 import settings
import os,sys
import zipfile

DOWN=os.path.join(settings.BASE_DIR,"down")
file_name=os.path.join(DOWN,"users.zip")





# 查看班级
def grade(request):
    # 取出所有班级对象
    class_obj=models.Grade.objects.all()
    #返回班级grade.HTML网页文件,并将班级对象传入给网页
    return render(request,"grade.html",{"grade_list":class_obj})

#添加班级
def add_grade(request):
    if request.method=="POST":
        # 取出post请求中的新班级名
        add_classname=request.POST.get("add_classname")
        #操作数据库表,向其中添加该数据
        models.Grade.objects.create(classname=add_classname)
        #返回一个查看班级的URl
        return redirect("/grade/")
    else:
        #返回一个添加班级的页面
        return render(request,"add_grade.html")


#删除班级
def del_grade(request):
    # 取出URL后拼接的id值
    class_id=request.GET.get("id")
    # 从数据库表中取出对应的对象
    class_obj=models.Grade.objects.get(id=class_id)
    # 删除该对象
    class_obj.delete()
    # 返回查询班级的URL
    return redirect("/grade/")

#修改班级
def change_grade(request):
    if request.method=="POST":
        #从拼接的URL中取出修改班级的id值
        class_id = request.GET.get("id")
        #从POST请求中取出新的班级名称
        new_classname=request.POST.get("new_classname")
        #从数据库中根据班级id取出班级对象
        class_obj = models.Grade.objects.get(id=class_id)
        # 修改班级对象的名称
        class_obj.classname=new_classname
        #保存班级对象
        class_obj.save()
        # 返回查询班级的URL
        return redirect("/grade/")
    else:
        #取出拼接URL中修改班级的id值
        class_id=request.GET.get("id")
        # 从数据库中取出修改的班级对象
        class_obj=models.Grade.objects.get(id=class_id)
        #返回一个修改页面文件,并将要修改的班级对象传如网页
        return render(request,"change_grade.html",{"class_list":class_obj})


 # 查看学生
def student(request):
    # 取出所有学生对象
    student_obj=models.Student.objects.all()

    #返回一个学生页面文件,并将所有学生对象传入该文件
    return render(request,"student.html",{"student_obj_list":student_obj})

# 添加学生
def add_student(request):
    if request.method=="POST":
        #取出post请求中的添加的学生姓名
        add_student_name=request.POST.get("add_student_name")
        # 取出post请求中添加学生的班级id
        class_id=request.POST.get("student_class")
        #操作数据库表创建该学生
        models.Student.objects.create(student_name=add_student_name,grade_id=class_id)
        #返回查询学生的URL
        return redirect("/student/")
    else:

        # 取出所有班级对象
        all_grade=models.Grade.objects.all()
        #返回一个添加学生的页面,并将多有班级对象传入该文件
        return render(request,"add_student.html",{"grade_list":all_grade})


# 删除学生
def del_student(request):
    #取得拼接URL中的要删除的学生id
    student_id=request.GET.get("id")
    #根据学生id在数据库中查出该学生对象
    student_obj=models.Student.objects.get(id=student_id)
    #删除该学生对象
    student_obj.delete()
    # 返回查询学生的URL
    return redirect("/student/")


# 修改学生
def change_student(request):
    if request.method=="POST":
        #取得拼接URL中要修改的学生id
        student_id=request.GET.get("id")
        #根据学生id查询出要修改的学生的对象
        student_obj=models.Student.objects.get(id=student_id)
        #取出POST请求中的新的学生姓名
        new_student_name=request.POST.get("new_student_name")
        #取出POST请求中新的班级id
        student_class_id=request.POST.get("student_class_id")
        #修改学生姓名
        student_obj.student_name=new_student_name
        #修改学生班级id
        student_obj.grade_id=student_class_id
        #保存修改
        student_obj.save()
        # 返回查询学生的URL
        return redirect("/student/")
    else:
        #取得拼接URL中要修改的学生id
        student_id=request.GET.get("id")
        #根据学生id查询出要修改的学生的对象
        sutdent_obj=models.Student.objects.get(id=student_id)
        #查询出所有班级对象
        grade_all=models.Grade.objects.all()
        #返回一个修改网页,将所有的班级对象和要修改的学生对象传入网页中
        return render(request,"change_student.html",{"sutdent":sutdent_obj,"grade_list":grade_all})


#查看老师
def teacher(request):
    #查询所有老师对象
    teacher_obj=models.Teacher.objects.all()
    #返回一个页面,并将所有老师对象传入该文件
    return render(request,"teacher.html",{"teacher_list":teacher_obj})

#添加老师
def add_teacher(request):
    if request.method=="POST":
        # 取得POST请求中的添加的老师名
        add_teacher_name=request.POST.get("add_teacher_name")
        # 操作数据库表添加该老师
        models.Teacher.objects.create(teacher_name=add_teacher_name)
        #返回一条查询老师信息的URL
        return redirect("/teacher/")
    else:
        #查询出所有班级对象,传入添加老师的页面
        all_grade=models.Grade.objects.all()
        return render(request,"add_teacher.html",{"grade_list":all_grade})


#删除老师
def del_teacher(request):
    #接受拼接URL中的要删除的老师id
    teacher_id=request.GET.get("id")
    #根据id从数据库中取出该老师对象
    teacher_obj=models.Teacher.objects.get(id=teacher_id)
    #删除该对象
    teacher_obj.delete()
    #返回一个老师查询URL
    return redirect("/teacher/")

#修改老师
def change_teacher(request):
    if request.method=="POST":
        ##接受拼接URL中的要修改的老师id
        teacher_id = request.GET.get("id")
        # 根据id从数据库中取出该老师对象
        teacher_obj = models.Teacher.objects.get(id=teacher_id)
        #取出POST请求中老师选择教授的班级id
        grades_list=request.POST.getlist("teacher_class_id")
        #取出POST请求中新的老师名
        teacher_new_name=request.POST.get("new_teacher_name")
        #修改数据库中老师的名称
        teacher_obj.teacher_name=teacher_new_name
        #保存修改
        teacher_obj.save()
        #修改老师教授的班级
        teacher_obj.grades.set(grades_list)
        return redirect("/teacher/")
    else:
        ##接受拼接URL中的要修改的老师id
        teacher_id=request.GET.get("id")
        # 根据id从数据库中取出该老师对象
        teacher_obj = models.Teacher.objects.get(id=teacher_id)
        #查询出所有的班级对象
        grade_all=models.Grade.objects.all()
        #返回一个修改老师的页面文件,将所有班级对象和要修改的老师对象传入该页面
        return render(request,"change_teacher.html",{"teacher":teacher_obj,"grade_list":grade_all})


def index(request):
    return render(request,"index.html")






#传入一个目录,拿出目录下所有文件的路径
def allfile(dirs,li=[]):
    file_list=os.listdir(dirs)
    for i in file_list:
        neic=os.path.join(dirs,i)
        if os.path.isdir(neic):
            allfile(neic)
        else:
            li.append(neic)
    return li

#传入一个文件路径列表,返回所有文件的代码行数
def num_all(li):
    num = 0
    size=0
    for i in li:
        with open(i, "r", encoding="utf8") as f:
            for line in f:
                if line.strip() == "":
                    pass
                elif line.strip().startswith("#"):
                    pass
                else:
                    num += 1
        size+=os.path.getsize(i)
    return num,size


#响应url的函数
def Addfile(request):
    if request.method=="GET":
        return render(request,"addfile.html")
    else:
        file_obj=request.FILES.get("filename")
        file_name=os.path.join(DOWN,file_obj.name)
        file_dir=os.path.join(file_name.split(".")[0])
        with open(file_name,"wb") as f:
            for i in file_obj:
                f.write(i)

        file_size=os.path.getsize(file_name)
        #解压文件
        z = zipfile.ZipFile(file_name)
        z.extractall(path=file_dir)
        z.close()


        #获取加压目录中的文件和子文件
        b=allfile(file_dir,[])
        print(b)
        num=num_all(b)
        file={
            "name":file_obj.name,
            "num":num[0],
            "size":num[1],
            "ysq":file_size,
        }
        return render(request,"file.html",{"file_a":file})





