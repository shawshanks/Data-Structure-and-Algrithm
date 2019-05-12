# Linked list 链表
## list的的缺点
1. list 中存储的元素数量可能小于list长度, 浪费存储空间
2. 均摊阻塞(Amortized bounds): 即当list的存储空间不能满足插入数量要求,要扩大容量时,insert()需要很多的操作时间. 而这种阻塞是实时系统所不能接受的.
3. 在list内部插入和删除元素的操作开销很大

## 链表和列表的区别
### 内部存储方式不同
列表是 array-based sequence, 是建立在一块 集中的 较大的 连续的 内存 之上的. 

链表是 node-based sequence, 是建立在 多块 分布式的 较小的 单个的 节点(内存)之上的.

### 链表的优缺点
链表的优点即为上面所述的list的缺点的反面

链表的缺点 是 很难快速定位中间元素, 而array-based 的列表可以利用 硬件本身的特性实现快速寻址. 

## 链表的种类
### 1.Singley Linked List 单向链表
### 2. Circularly Linked List 环形链表
### 3. Doubly Linked List 双向链表
### 4. Positional Linked List 位置链表
### 5. Skiped linked List 跳表