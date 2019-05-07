# Python 风格
def insert_sort_Pythonic(array):
    for i in range(1, len(array)):
        for j in range(i-1, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1


# Python风格变体
def insert_sort_x(array):
    for i in range(1, len(array)):
        while array[i] < array[i-1] and i-1 >= 0:
            temp = array[i-1]
            array[i-1] = array[i]
            array[i] = temp
            i -= 1


# 普通风格
def insert_sort(array):
    for i in range(1, len(array)):
        cur = array[i]
        while cur < array[i-1] and i-1 >= 0:
            array[i] = array[i-1]
            i -= 1
        array[i] = cur  # 因为下一个值不小,而这个值小于 cur,所以是array[i] =cur


if __name__ == '__main__':
    array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insert_sort(array)
    print(array)



