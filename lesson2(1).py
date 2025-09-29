# 初始化任务清单
tasks = []

# 显示菜单
def show_menu():
    print("\n任务清单管理系统")
    print("1. 添加新任务")
    print("2. 显示所有任务")
    print("3. 标记任务为已完成")
    print("4. 退出程序")

# 添加新任务
def add_task():
    task = input("请输入新任务：")
    tasks.append({"任务": task, "状态": "未完成"})
    print(f"任务 '{task}' 已添加！")

# 显示所有任务
def show_tasks():
    if not tasks:
        print("当前没有任务！")
    else:
        print("\n任务清单：")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['任务']} - {task['状态']}")

# 标记任务为已完成
def complete_task():
    show_tasks()
    if tasks:
        try:
            task_number = int(input("请输入要标记为已完成的任务编号："))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["状态"] = "已完成"
                print(f"任务 '{tasks[task_number - 1]['任务']}' 已标记为已完成！")
            else:
                print("无效的任务编号！")
        except ValueError:
            print("请输入有效的数字！")

# 主程序循环
while True:
    show_menu()
    choice = input("请选择操作（1-4）：")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("程序已退出，再见！")
        break
    else:
        print("无效的选择，请重新输入！")