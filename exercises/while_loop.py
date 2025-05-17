"""
练习: while循环

描述：
在数字列表中查找第一个偶数。

请补全下面的函数，使用while循环在数字列表中查找并返回第一个偶数。
如果列表中没有偶数，则返回None。
"""


def find_first_even(numbers: list):
    """
    在数字列表中查找第一个偶数

    参数:
    - numbers: 整数列表

    返回:
    - 列表中的第一个偶数，如果没有偶数则返回None
    """
    # 请在下方编写代码
    while True:
        if len(numbers) == 0:
            return None

        a = numbers.pop(0)
        if a > 1 and a % 2 == 0:
            return a
