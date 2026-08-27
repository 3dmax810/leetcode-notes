class Heap:
    def __init__(self, ls):
        self.ls = []

    def push(self, value):
        self.ls.append(value)
        self.sift_up(len(self.ls)-1)
        
    def pop(self, iD):
        if not self.ls:
            pass

    def sift_up(self, iD):
        while iD>0:
            parent = (iD-1)//2
            if self.ls[iD]>self.ls[parent]:
                self.ls[iD], self.ls[parent] = self.ls[parent], self.ls[iD]
                iD = parent

    def sift_down(self, iD):
        n = len(self.ls)       
        if iD == 0:
            self.ls[iD], self.ls[-1] = self.ls[-1], self.ls[iD]
            lose = self.ls.pop()
            n = len(self.ls)
            left = 2*iD + 1
            right = 2*iD + 2
            while (self.ls[iD]<self.ls[left] or self.ls[iD]<self.ls[right]) and left<=n-1 and right<=n-1:
                if self.ls[left] < self.ls[right]:
                    self.ls[iD], self.ls[right] = self.ls[right], self.ls[iD]
                    iD = right
                else:
                    self.ls[iD], self.ls[left] = self.ls[left], self.ls[iD]
                    iD = left
            return lose
        else:
            self.ls[iD], self.ls[-1] = self.ls[-1], self.ls[iD]
            lose = self.ls.pop()
            if self.ls[iD] < lose: # 下沉
                left = 2*iD + 1
                right = 2*iD + 2
                while (self.ls[iD] < self.ls[left] or self.ls[iD]<self.ls[right]) and left<=n-1 and right<=n-1:
                    if self.ls[left] < self.ls[right]:
                        self.ls[iD], self.ls[right] = self.ls[right], self.ls[iD]
                        iD = right
                    else:
                        self.ls[iD], self.ls[left] = self.ls[left], self.ls[iD]
                        iD = left
            else: # 上浮
                parent = (iD-1)//2
                while self.ls[iD] > self.ls[parent]:
                    self.ls[iD], self.ls[parent] = self.ls[parent], self.ls[iD]
                    iD = parent
                    parent = (iD-1)//2
            return lose