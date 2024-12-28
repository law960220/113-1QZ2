class Stack:
    def __init__(self, max_size):
        self.stack = []           #用來儲存堆疊元素的列表
        self.max_size = max_size  #設定最大容量

    def top_item(self):
        if self.is_empty(): #檢查堆疊是否為空，是的話顯示訊息
            print("Stack is empty! No top item.")
            return None
        else: #否則顯示頂端內容
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0 #判斷堆疊是否為滿

    def is_full(self):
        return len(self.stack) >= self.max_size #判斷堆疊是否為滿
