
#SINGLE INHERITANCE:
##class Parent:
##    def land(self):
##        print("I have 10 acres of land")
##
##class Child(Parent):
##    pass
##obj=Child()
##obj.land()
##
##

#MULTIPLE INHERITANCE:
##class Parent1:
##    def land(self):
##        print("I have 10 acres of land")
##
##class Parent2:
##    def gold(self):
##        print("I have 10 kg of gold")
##
##class Child(Parent1,Parent2):
##    pass
##obj=Child()
##obj.land()
##obj.gold()


#POLYMORPHISM:what we give in last that will going to print...
##class A:
##    def a(self):
##        print("Welcome")
##        
##class B(A):
##    def a(self):
##        print("hello")
##class C(B):
##    def a(self):
##        print("GoodByee")
##obj=C()
##obj.a()


#ENCAPSULATION:
##class Bank:
##    def __admin(self):
##        print("amount is:",100000)
##
##obj=Bank()
##obj._Bank__admin()


#ABSTRACTION:
##from abc import ABC,abstractmethod
##class Bike(ABC):
##    @abstractmethod
##    def engine(self):
##        pass
##    @abstractmethod #@is used as decorator8
##    def acc(self):
##        pass
##class Bullet(Bike):
##    def engine(self):
##        print("it is 1000cc engine")
##    def acc(self):
##        print("it can pickup in 1.2 sec")
##gt=Bullet()
##gt.engine()

























        
