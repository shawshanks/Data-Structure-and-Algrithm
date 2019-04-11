# 斐波那契数列
## 1.数学定义
斐波那契数列: [维基百科](https://en.wikipedia.org/wiki/Fibonacci_number)
<img src = "https://github.com/shawshanks/Data-Structure-and-Algrithm/blob/master/image/%E8%8F%B2%E6%B3%A2%E9%82%A3%E5%88%87%E6%95%B0%E5%88%97%E5%AE%9A%E4%B9%89.PNG" width = '100%'>

即
```python
Fib(n) = n    ,  if n = 0,1
       = Fib(n-1) + Fib(n-2) , if n >2 
```

# 递归完成
## 1.Python的第一种完成 (效率比较差的递归)
根据定义写
```python
def Fib(n):
    if n <= 1:
        return n
    else:   
        return Fib(n-1) + Fib(n-2)
```
Fib() 每次调用时, 都会再调用两次Fib(). 所以这种写法的复杂度是 `O(2^n)`, 指数函数.不可接受.

## 2. 递归的优化写法

### 思路
尝试 Fib()中每次只调用一次自身.那么我们需要在函数完成其中一个调用函数(`fib(n-1)`或`fib(n-2)`的过程.  
这个递归函数`fib(n)`返回一个连续的斐波那契数列数列中的两个数`(f(n), f(n-1))`.  
每次调用`fib(n)`时想要达到的效果如下:  

```python
    f(0)    f(1)    f(2)    f(3)    f(4)    f(5)    f(6)    f(7)    f(8)    ...     f(n)
    (0,1)   (1,1)   (1,2)   (2,3)   (3,5)   (5,8)   (8,13)  (13,21) (21,34) (...)  (an, an+1
    /   \    / \     / \
   a0   a1  a1  a2 a2   a3  ................................................
   注: a0表示斐波那契数列第0项,a1 表示第1项,依次类推, an表示第n项,an+1表示第 n+1项
```

### 实现
```python
def fib(n):
    if n <= 1:
        return (n, 1)   # 这里不返回(0,1),因为f(n)返回的是左边的元素.
    else:               # f(0)[0]返回0, f(1)[0]返回的还是1
        (a, b) = fib(n-1)
        return (b, a+b)
```
### 调用fib(n)过程图示
<img src= 'https://www.pornhub.com/view_video.php?viewkey=ph5c3152e0577f9' width= '50%'>

### 包装调用,F(n)返回第n项的值
如果我们想要返回一个相应的值,只需再调用`fib()`的结果就行了.可以写成以下两种形式:

```python
def fib(n):
    if n <= 1:
        return (n, 1)   # 这里不返回(0,1),因为f(n)返回的是左边的元素.
    else:               # f(0)[0]返回0, f(1)[0]返回的还是1
        (a, b) = fib(n-1)
        return (b, a+b)

def F(n):
    return fib(n)[0]
``` 
或者
```python
def F(n):
    def fib(n):
        if n <= 1:
            return (n, 1)   # 这里不返回(0,1),因为f(n)返回的是左边的元素.
        else:               # f(0)[0]返回0, f(1)[0]返回的还是1
            (a, b) = fib(n-1)
            return (b, a+b)
    return fib(n)[0]
```

## 也可以用字典暂时存储递归中的值
```python
memo = {0:0, 1:1}
def fib2(n):
    if not n in memo:
        memo[n] = fib2(n-1)+fib2(n-2)
    return memo[n]
```
与上面 元组 的作用一样, 存储之前计算的值.  
不同的是, 返回的元组 有固定结构 (an, an+1), 每次返回只存储两个值. 而这个字典把之前所有的值都存储起来.

# 迭代完成
## for-loop完成
```python
def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
```
## while-loop 完成
```python:
def fib(n):
    a, b = 0, 1
    while n >= 1:
        a, b = b, a+b
        n -= 1
    return a
 ```
 或者 用`yield`生成器
 ```python
 def fib(n):
    a, b = 0, 1
    while n > 0:
        yield a
        a, b = b, a+b
        n -= 1
 ```
 
 # 听说还能用矩阵方法表示, 不过暂时就到这里吧
