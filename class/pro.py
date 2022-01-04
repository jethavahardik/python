class one():
    def balance(self,a):
        self.a=a
        return self.a
    def deposit(self):
        self.a=self.a+5
        return self.a

obj=one()
print(obj.balance(700))
print(obj.deposit())