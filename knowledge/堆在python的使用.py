import heapq

ls = []
heapq.heapify(ls) # 列表转为堆，最小堆
heapq.heappush(ls, 1) # 插入元素
heapq.heappop(ls) # 弹出最小元素

# heapq 默认保存最小堆，如果要做最大堆，可以在插入元素时取负数，弹出元素时再取负数

# heapq 支持元组入堆
heapq.heappush(ls, (1, 'a')) # 插入元组

# heapq 允许重复元素，无hash冲突问题，重复元素会被当作不同的元素处理