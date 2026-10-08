from collections import deque
# 是高性能双端容器，单线程刷题 BFS 用
dq = deque()
dq.append(1) # 队尾入队
dq.popleft() # 队首出队
dq.pop() # 队尾出队
len(dq) # 队列大小
if dq: # 判断队列是否非空
    pass


from queue import Queue
# 是带锁的线程安全队列，做多线程任务传递
q = Queue() 
q.put(1) # 入队
q.get() # 出队
q.qsize() # 队列大小
q.empty() # 判断队列是否为空
