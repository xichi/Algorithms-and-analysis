# Algorithms-and-analysis


## 学习大纲

学习的这些方法更像是一种通用的解决问题的思路，而不是一种具体的算法。

### 1.分治法（divide and conquer, D&C）

将一个复杂的问题分解成若干个规模较小、 相互独立，但类型相同的子问题求解；然后再将各子问题的解组合成原始问题的一个完整答案，这样的问题求解策略就叫分治法。

#### 基本思路

1. 找出简单的基线条件。
2. 确定如何缩小问题的规模，使其符合基线条件。

#### 应用范例

+ 快速排序
+ 三分搜索算法

### 2.动态规划法

#### 基本思路

+ 最优子结构性质 （自底向上）
+ 重叠子问题性质

#### 与分治法、贪心法的异同

1. 贪心法接近于最优解，但不是最优解
2. 分治法自上而下，动态规划法自下而上

#### 应用范例

+ 多段图问题、关键路径问题
+ 每对结点间的最短路径
+ 最长公共子序列
+ 0/1背包问题

### 3.贪婪法（贪心法）

贪婪算法寻找局部最优解，企图以这种方式获得全局最优解。贪婪算法是易于实现、运行速度快的近似算法。

#### NP完全问题

没有快速算法的问题。使用近似算法，快速找到NP完全问题的近似解。
