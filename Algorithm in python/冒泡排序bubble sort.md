```python
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):                # 第n次对序列一一比较,找出最大数
        for j in range(0, n-1-i):      # 每次都从索引为0的元素开始,两两比较(list[j] compare list[j+1] 到 len(list)-1-n
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list
                
     
```
