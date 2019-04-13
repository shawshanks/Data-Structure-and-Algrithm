<img src = "https://github.com/shawshanks/Data-Structure-and-Algrithm/blob/master/image/mid.png" width = '30%'>

由上面的分析可知:  
```
因为 mid = (low+high)//2,  low <= high  
所以       low <= mid <= high
```

```
if b = a+1, (a+b)//2 = (a+a+1)//2 = (2a+1)//2 = a   即当 b=a+1时, mid=a
   b = a+2, (a+b)//2 = (a+a+2)//2 = (2a+2)//2 = a+1 = b-1  当b = a+2时, mid在a,b中间
```

### 递归版本
```python
def binary_search(list,target,low,high):    # low初始值默认为0,high初始值默认为list最后一位元素索引,即len(list)-1
    if low > high:  # low <= high都是正常情况
        return "no match" # 序列中没有和target匹配的值
    mid = (low + high)//2   # 如果 high = low +1 则 mid = low
    if target == list[mid]:
        return mid      # target和list[mid]处的值匹配
    elif target < list[mid]:
        return binary_search(list,target,low,mid-1) # 如果 mid = low, 那么 下次递归时, low > mid -1 = high,说明没有匹配
    elif target > list[mid]:
        return binary_search(list,target,mid+1,high)    # 如果 mid=low,那么下次递归时, low = mid+1 = high
        
```

### while-loop非递归版本
```python
def binary_search(list,target,low,high):  
    while not(low > high):
        mid = (low + high) // 2
        if target == list[mid]:
            return mid
        elif target > list[mid]:
            low = mid + 1 
        elif target < list[mid]:
            high = mid - 1
    return "no match"
         
```
