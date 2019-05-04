class GameEntry:
    """Represents one entry of a list of high scores."""

    def __init(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0},{1})'.format(self._name, self._score)


class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=100):
        """Initialize scoreboard with given maximum capacity."""
        """All entries are initially None."""

        self._board = [None] * capacity
        self._n = 0  # 统计表中实际项的数量

    def __getitem__(self, x):
        """Return entry at index x."""
        return self._board[x]

    def __str__(self):
        """Return string representating of the high score list."""
        return '\n'.join(str(self._board[j] for j in range(self._n + 1)))

    def add_1(self, entry):
        score = entry.get_score()
        # 分类讨论法
        # 分成表已经满和没满两种情况
        # 区别:
        # 1. 没满的话, 加入新的元素后,self._n的值要+1
        # 2. 两者在置换边界有区别: 没满,最后一个值要保留,占用之后的一个None
        # 而满了的话, 最后一个值被丢弃
        full = (self._n >= len(self._board))
        if not full:

            # for i in range(self._n):
            #     if self._board[i].get_score < score:
            #         for _ in range(i+1, self._n + 1):
            #             self._board[i+1] = self._board[i]
            #         self._board[i] = entry
            #         self._n += 1 这行其实可以写在开头,这样在下面的
            #                      for _ in ..循环中不需要额外边界检查
            self._n += 1
            for i in range(self._n):
                if self._board[i].get_score() < score:
                    for _ in range(i+1, self._n):
                        self._board[i+1] = self._board[i]
                    self._board[i] = entry
                    break
        else:
            for i in range(self._n):
                if self._board[i].get_score < score:
                    for j in range(self._n - 1, i):
                        self._board[j] = self._board[j-1]
                    self._board[i] = entry
                    break

    def add_2(self, entry):
        """
        对 add_1()的改进:
        消除add_1()中有很多重复代码
        """

        score = entry.get_score()
        full = (self._n >= len(self._board))


        # if self._board[i].get_score < score:
        #     # 使用条件表达式来消除小的分歧
        #     for _ in range(i+1, self._n + (1 if not full else 0)):
        #         self._board[i+1] = self._board[i]
        #     self._board[i] = entry
        #     if not full:      这行和上一行可以写在开头,这样可以免去边界检查
        #         self._n += 1
        if not full:
            self._n += 1    # 锁定数组长度

        for i in range(self._n):
            if self._board[i].get_score() < score:
                for j in range(self._n - 1, i):
                    self._board[j] = self._board[j-1]
                self._board[i] = entry
                break

    """
    add_1() 和 add_2() 在移动现有成员时,顺序为:从左往右 这样有缺点

    # 注:其实可以通过 锁定数组实际大小来避免以下两个问题.
    # 通过 if not full: self._n += 1 来把 notfull 和full两种区别消除.
    # 然后就可以使用range()的自动边界检查,而不是自己的检查了.

    1. 传递的副作用:
        array[i] = array[i+1] 这样移动有传递性,
        这样当移动出边界后,后面的所有None值, 也都会被传递成array[end_value], 这是一个额外的 副作用.
    2. 需要额外的边界检查:
        如果不设置边间检查, 那么当i到达数组末尾,而其后又没有额外存储的空间时,
        便会导致异常. 因此必须小心的检查 i的值,保证其在到达 倒数第二个元素时完成后
        终止.

    从边界向目标点移动就可以轻松避免上述两个问题

    """
    def add_3(self, entry):
        score = entry.get_score()
        full = (self._n >= len(self._board)-1)

        if not full:
            self._n += 1

        j = self._n - 1  # j为最后一位成员的索引
        # 使用while要小心的检查边界条件

        # 如果j之前还有成员(j>0),就检查是否前面的成员是否需要交换 score大小检查
        # 如果需要交换,就顺序交换,然后j-=1
        # for语句自动帮你检查 边界,和递变变量 ,所以还是用for更简单
        while j > 0 and self._board[j-1].get_score() < score:
            self._board[j] = self._board[j-1]
            j -= 1
        self._board[j] = entry  # 然后替换j位置的成员





















