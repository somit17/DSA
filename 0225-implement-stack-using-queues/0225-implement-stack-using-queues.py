# #Using 2 queue
# class MyStack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()
        
#     def push(self, x: int) -> None:
#         self.q1.append(x)
        

#     def pop(self) -> int:
#         while len(self.q1) > 1 :
#             self.q2.append(self.q1.popleft())

#         last_val = self.q1.popleft()
#         self.q1,self.q2 = self.q2,self.q1
#         return last_val

#     def top(self) -> int:
#         while len(self.q1) > 1:
#             self.q2.append(self.q1.popleft())

#         top_val = self.q1[0]
#         self.q2.append(self.q1.popleft())
#         self.q1,self.q2 = self.q2,self.q1
#         return top_val
        

#     def empty(self) -> bool:
#         return len(self.q1) ==0
        
#Using 1 queue
class MyStack:
    def __init__(self):
        self.q1 = deque()
        
    def push(self, x: int) -> None:
        self.q1.append(x)
        for _ in range(len(self.q1)-1):
            self.q1.append(self.q1.popleft())
        

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1) ==0


# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()