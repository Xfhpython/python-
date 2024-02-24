# 学生类
from os import system


class Student:
    def __init__(self, name, id, age, sex, province, gaoshu_score, yuwen_score, yingyu_score):
        self.name = name
        self.id = id
        self.age = age
        self.sex = sex
        self.province = province
        self.gaoshu_score = gaoshu_score
        self.yuwen_score = yuwen_score
        self.yingyu_score = yingyu_score

    def __str__(self):
        return f"姓名：{self.name}, 学号：{self.id}, 年龄：{self.age}, 性别：{self.sex}, 籍贯：{self.province}, 数学成绩：{self.gaoshu_score}，" \
               f"语文成绩：{self.yuwen_score}, 英语成绩：{self.yingyu_score}"


# 添加学生功能
def add_student():
    name = input("请输入学生的名字：")
    id = input("请输入学生的学号：")
    age = int(input("请输入学生的年龄："))
    sex = input("请输入学生的性别：")
    province = input("请输入籍贯：")
    gaoshu_score = int(input("请输入数学成绩："))
    yuwen_score = int(input("请输入语文成绩："))
    yingyu_score = int(input("请输入英语成绩："))
    student = Student(name, id, age, sex, province, gaoshu_score, yuwen_score, yingyu_score)
    f = open("student.txt", "a+")
    f.write(str(student))
    f.write('\n')
    print("添加成功")
    f.close()
    


# 显示所有学生功能
def show_student():
    f = open("student.txt", "r")
    for line in f.readlines():
        line = line.strip()
        print(line)
    f.close()


# 删除学生功能
def del_student():
    print("只有名字和学号两者都符合，才能进行删除:")
    id = input("请输入学号：")
    name = input("请输入姓名：")
    with open("student.txt", "r+") as f:
        lines = f.readlines()
    with open("student.txt", "w+") as f:
        for line in lines:
            if id in line and name in line:
                print("删除成功")
            else:
                f.write(line)



# 菜单功能
def print_menu():
    print("-----------------")
    print("--学生信息管理系统--")
    print("1:添加学生")
    print("2:删除学生")
    print("3:修改学生")
    print("4:查询学生")
    print("5:显示所有学生")
    print("6:退出系统")
    print("-----------------")


# 修改学生功能
def revise_student():
    print("只有名字和学号符合才能进行修改：")
    name = input("请输入修改学生的姓名;")
    id = input("请输入修改学生的学号：")
    with open("student.txt", "r+") as f:
        lines = f.readlines()
    with open("student.txt", "w+") as f:
        for line in lines:
            if name in line and id in line:
                name = input("请输入修改后学生的名字：")
                id = input("请输入修改后学生的学号：")
                age = int(input("请输入修改后学生的年龄："))
                sex = input("请输入修改后学生的性别：")
                province = input("请输入修改后籍贯：")
                gaoshu_score = int(input("请输入修改后数学成绩："))
                yuwen_score = int(input("请输入修改后语文成绩："))
                yingyu_score = int(input("请输入修改后英语成绩："))
                student = Student(name, id, age, sex, province, gaoshu_score, yuwen_score, yingyu_score)
                f.write(str(student))
            else:
                f.write(line)


# 查询学生功能
def inquiry_student():
    print("请根据学生的姓名和学号进行查询")
    name = input("请输入要查询学生的姓名：")
    id = input("请输入要查询学生的学号：")
    with open("student.txt", "r+") as f:
        lines = f.readlines()
    for line in lines:
        if id in line and name in line:
            print(line)
   



# 退出功能
def exit_student():
    exit()


def main():
    while True:
        print_menu()
        choose = int(input("请输入你选择的功能："))
        if choose == 1:
            add_student()
        elif choose == 2:
            del_student()
        elif choose == 3:
            revise_student()
        elif choose == 4:
            inquiry_student()
        elif choose == 5:
            show_student()
        elif choose == 6:
            exit_student()


if __name__ == '__main__':
    main()