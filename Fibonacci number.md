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
    if n < 2:
        return n
    else:   
        return Fib(n-1) + Fib(n-2)
```
Fib() 每次调用时, 都会再调用两次Fib(). 所以这种写法的复杂度是 `O(2^n)`, 指数函数.不可接受.

## 2. 递归的优化写法
尝试 Fib()中每次只调用一次自身.
```python
def Fib(n):
    if n < 2:
        return (n, 0)
    else:
        (a, b) = Fib(n-1)
        return (b, a+b)
```
