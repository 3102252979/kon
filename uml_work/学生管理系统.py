class Student:
    def __init__(self, name, age, grade):
        self.name = name  # 初始化学生姓名
        self.age = age  # 初始化学生年龄
        self.grade = grade  # 初始化学生年级

    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}, 年级: {self.grade}"  # 重写字符串表示形式，用于打印学生信息

class StudentManager:
    def __init__(self):
        self.students = []  # 初始化学生列表

    def add_student(self, student):
        self.students.append(student)  # 将学生对象添加到学生列表
        print("学生信息添加成功！")  # 打印成功添加学生信息的消息

    def view_students(self):
        if not self.students:
            print("学生列表为空！")  # 如果学生列表为空，则打印提示消息
        else:
            print("学生列表：")
            for student in self.students:
                print(student)  # 遍历学生列表并打印每个学生信息

    def search_student(self, name):
        found = False
        for student in self.students:
            if student.name == name:  # 如果找到与输入姓名匹配的学生对象
                print("找到学生信息：", student)  # 打印找到学生信息的消息
                found = True
                break
        if not found:
            print("未找到该学生信息！")  # 如果未找到匹配的学生姓名，则打印未找到学生信息的消息

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:  # 如果找到与输入姓名匹配的学生对象
                self.students.remove(student)  # 从学生列表中删除该学生对象
                print("学生信息删除成功！")  # 打印成功删除学生信息的消息
                break
        else:
            print("未找到该学生信息，无法删除！")  # 如果未找到匹配的学生姓名，则打印未找到学生信息的消息

def display_menu():
    print("欢迎使用学生管理系统！")
    print("1. 添加学生信息")
    print("2. 查看学生列表")
    print("3. 搜索学生信息")
    print("4. 删除学生信息")
    print("5. 退出")

def get_choice():
    while True:
        try:
            choice = int(input("请输入选项编号："))  # 获取用户输入的选项编号
            if 1 <= choice <= 5:  # 如果选项编号在有效范围内
                return choice  # 返回用户选择的选项编号
            else:
                print("无效的选项编号！")  # 如果选项编号无效，则打印提示消息
        except ValueError:
            print("请输入一个有效的数字选项！")  # 如果输入不是整数，则打印提示消息

def main():
    student_manager = StudentManager()  # 创建学生管理器对象

    while True:
        display_menu()  # 显示菜单
        choice = get_choice()  # 获取用户选择的选项编号

        if choice == 1:
            name = input("请输入学生姓名：")  # 获取用户输入的学生姓名
            age = int(input("请输入学生年龄："))  # 获取用户输入的学生年龄
            grade = input("请输入学生年级：")  # 获取用户输入的学生年级
            student = Student(name, age, grade)  # 创建学生对象
            student_manager.add_student(student)  # 将学生对象添加到学生管理器中
        elif choice == 2:
            student_manager.view_students()  # 查看学生列表
        elif choice == 3:
            name = input("请输入要搜索的学生姓名：")  # 获取要搜索的学生姓名
            student_manager.search_student(name)  # 搜索学生信息
        elif choice == 4:
            name = input("请输入要删除的学生姓名：")  # 获取要删除的学生姓名
            student_manager.remove_student(name)  # 删除学生信息
        else:
            print("谢谢使用！再见！")  # 打印退出消息
            break

if __name__ == "__main__":
    main()  # 调用主函数
