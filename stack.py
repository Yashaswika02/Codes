#STACK-LAST IN FIRST OUT PRINCIPLE
##class Stack:
##    def __init__(self):
##        self.stack=[]
##    def push(self,data):
##        if len(self.stack)<= 5:
##           self.stack.append(data)
##        else:
##            print("overflow")
##            return
##    def pop(self):
##        if len(self.stack)==0:
##            print("stack underflow")
##            return
##        else:
##            self.stack.pop()
##    def isEmpty(self):
##        return len(self.stack)==0
##    def peek(self):
##        print(self.stack[-1])
##    def display(self):
##        print(self.stack)
##s=Stack()
##s.push(7)
##s.push(10)
##s.push(23)
##s.push(46)
##s.pop()
##s.display()


#QUEUE-FIRST IN FIRST OUT PRINCIPLE
##class Queue:
##    def __init__(self):
##        self.queue=[]
##    def in_left(self,data):
##        self.queue.insert(0,data)
##    def in_right(self,data):
##        self.queue.append(data)
##    def re_left(self):
##        self.queue.remove(20)
##    def re_right(self):
##        self.queue.pop()
##    def rear(self):
##        print(self.queue[-1])
##    def front(self):
##        print(self.queue[0])
##    def display(self):
##        print(self.queue)        
##        
##t=Queue()
##t.in_left(10)
##t.in_left(55)
##t.in_right(20)
##t.in_right(40)
##t.re_left()
##t.re_right()
##t.rear()
##t.front()
##t.display()




#PARENTHESIS PROGRAM:valid or not checking
##def valid_p(s):
##    stack=[]
##    for ch in s:
##        if ch in "({[":
##          stack.append(ch)
##        else:
##            if not stack:
##                return False
##            top=stack.pop()
##            if (ch==")"and top!="(") or (ch=="}"and top!="{") or (ch=="]"and top!="["):
##                return False
##    return len(stack)==0
##print(valid_p("{(})]}"))
































        
