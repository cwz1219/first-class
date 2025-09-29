# 提示用户输入分数
score = input("请输入一个分数（0-100）：")

# 检查输入是否为数字
if score.isdigit():
    score = int(score)  # 将输入转换为整数

    # 判断分数范围并输出对应的等级
    if 90 <= score <= 100:
        print("优秀")
    elif 75 <= score < 90:
        print("良好")
    elif 60 <= score < 75:
        print("及格")
    elif 0 <= score < 60:
        print("不及格")
    else:
        print("分数超出范围，请输入0-100之间的分数。")
else:
    print("输入无效，请输入一个数字。")