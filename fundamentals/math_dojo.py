class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += a
        # print(self.result)
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= a
        # print(self.result)
        return self
# create an instance:
md = MathDojo()
a = md.add(3,5,1,8,10,5,6,7).result
print(a)
b = md.subtract(10,5,1,2,6,7).result
print(b)

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

