class Reverse:
    def_int_(self,data):
        self.data=data
        self.index=len(data)
    def_iter_(self):
        return self
    def_next_(self):
        if self.index==0:
            raise StopIteration
        self.index-=1
        return self.data[self.index]
rev=Reverse('giraffe')
for char in rev:
    print(char)
print("This code is written and excecuted by MEHAK BHUTANI with ERP 0231BCA063")
