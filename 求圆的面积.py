# 导入数学模块
import math
# 定义计算圆面积的函数
def calculate_circle_area(radius):
    """
    计算圆的面积
    参数: radius - 圆的半径
    返回: 圆的面积
    """
    area = math.pi * radius ** 2
    return area
# 主函数
def main():
    # 获取用户输入
    radius = float(input("请输入圆的半径: "))
    # 检查输入是否有效
    if radius <= 0:
        print("半径必须大于0!")
    else:
        # 计算并输出结果
        area = calculate_circle_area(radius)
        print(f"半径为 {radius} 的圆的面积是: {area:.5f}")
# 程序入口点
if __name__ == "__main__":
    main()