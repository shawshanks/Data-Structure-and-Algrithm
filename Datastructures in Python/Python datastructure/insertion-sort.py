def insertionSort(array):
    for index in range(1, len(array)):
        index_value = array[index]
        # 在index之前的数组中,寻找index_value 现在合适的位置
        for bigger in range(index):
            if index < array[bigger]:
                # bigger处就是要和现在的值要互换的位置

                # 从index处开始,把之前的元素后移一位,直到bigger处
                for k in range(index, bigger, -1):
                    array[k] = array[k-1]

                # 然后把array[temp] 插入合适的位置
                array[bigger] = index_value
                break   # 结束循环
    return array


def insertionSort_2(array):
    for index in range(1, len(array)):
        index_value = array[index]
        j = index
        # 从index开始,step= -1, 将 value(index) 和 前一个位置的值进行比较:
        #    if value(index) < 前一个位置的值: 将一个位置的值后移
        # 直到 和第一个数进行比较,即 j = 1, j-1 =0
        while array[j-1] > index_value and j >= 1:
            array[j] = array[j-1]
            j -= 1

        # 最后插入index_value. 此时, 注意上面的while循环, 在最后一次满足条件的
        # 交换之后, j的值又减小了1, 这样j就是那个最终要被插入的位置.
        array[j] = index_value


array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def insertionSort_3(array):
    for i in range(1, len(array)):
        insert = array[i]

        j = i
        while insert < array[j-1] and j >= 1:
            array[j] = array[j-1]
            j -= 1
        array[j] = insert


insertionSort_3(array)
print(array)



