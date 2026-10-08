# 快速排序
# 选定list的首个元素为哨兵，把list分为两部分，左边小于哨兵，右边大于哨兵，然后递归对左右两部分进行排序
#        先从list右侧开始，直到遇见比哨兵小的放左边。high-=1
#        然后从low开始，知道遇见比哨兵大的放右边。low+=1
#        low==high时，哨兵放在low位置
# 然后对子序列进行同样的选哨兵、左右对比
# 注意：编写代码时，先右后左

# 注意：
# partition部分，需要设置=号，否则low/high不更新，陷入死循环
# 在quicksort中，设置 low<high避免出现 quicksort(ls,3,2) 等low>=high的情况

# 该代码应该额外引入随机交换数值的操作，避免复杂度过高

ls = [9,8,0,7,6,5,4,3,2,1]

def partition(ls, low, high):
    val = ls[low]
    while low < high:
        while low < high and ls[high] >= val:
            high -= 1
        ls[low] = ls[high]
        while low < high and ls[low] <= val:
            low += 1
        ls[high] = ls[low]
    ls[low] = val
    return low

def quicksort(ls, low, high):
    if low >= high:
        return
    nl = len(ls)
    x = partition(ls, low, high)
    quicksort(ls, low, x-1)
    quicksort(ls, x+1, high)
    return ls

ls = quicksort(ls, 0, len(ls)-1)
print(ls)