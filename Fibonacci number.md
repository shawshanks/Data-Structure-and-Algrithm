# 斐波那契数列

## 1.数学定义
斐波那契数列: [维基百科](https://en.wikipedia.org/wiki/Fibonacci_number)
<img src = "https://github.com/shawshanks/Data-Structure-and-Algrithm/blob/master/image/%E8%8F%B2%E6%B3%A2%E9%82%A3%E5%88%87%E6%95%B0%E5%88%97%E5%AE%9A%E4%B9%89.PNG" width = '100%'>

即
```python
Fib(n) = n    ,  if n = 0,1
       = Fib(n-1) + Fib(n-2) , if n >2 
```

## 1.Python的第一种写法 (效率比较差的递归)
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
尝试 Fib()中每次只调用一次自身.
```python
def fib(n):
    if n <= 1:
        return (n, 1)   # 这里不返回(0,1),因为f(n)返回的是左边的元素.
    else:               # f(0)[0]返回0, f(1)[0]返回的还是1
        (a, b) = fib(n-1)
        return (b, a+b)
```
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
