### 递归版本
```python
def binary_search(list,target,low,high):    # low初始值默认为0,high初始值默认为list最后一位元素索引,即len(list)-1
    if low > high:
        return "no math" # 序列中没有和target匹配的值
    mid = (low + high)//2
    if target == list[mid]:
        return mid      # target和list[mid]处的值匹配
    elif target < list[mid]:
        return binary_search(list,target,low,mid-1)
    elif target > list[mid]:
        return binary_search(list,target,mid+1,high)
        
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
