from inspect import isgeneratorfunction
import types
from collections import Iterable
#斐波那契数列方法1
#缺点：只print了，却没有返回
def fab1(max):
	n,a,b=0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n=n+1
#fab1(5)

#斐波那契数列方法2
#优点：有返回
#缺点：运行中会占用过多内存， 随着max的增大而增大，如果要控制内存占用，最好不用List列表
def fab2(max):
	count,previous,current=0,0,1
	Result=[] #结果是列表，要返回
	while count<max:
		Result.append(current)
		previous,current=current,previous+current 
		count=count+1
	return Result
def show(obj):
	for item in obj:
		print(item)
#show(fab2(5))

#斐波那契数列方法2
#优点：有返回，不会生成List，而是在每次迭代中返回下一个数值（返回iterable对象）
#缺点：不简洁，比较麻烦。 其实目前我还没有debug成功， (type error: iter() return non-iterator of type Fab)
class Fab(object):
	def __init__(self,max):
		self.max=max
		self.count,self.previous,self.current=0,0,1

	def __iter__(self):
		return self

	def next(self):
		if slef.count<self.max:
			result=self.current
			self.previous,self.current = self.current,self.previous+self.current
			self.count=self.count+1
			return result
		raise StopIteration()
'''		
for n in Fab(6):
	print(n.current)
'''	
def fab3(max):
	count,previous,current=0,0,1
	while count<max:
		yield current
		previous,current=current,previous+current
		count=count+1

max=5
show(fab3(max))
print("fab3函数是否是generator函数:",isgeneratorfunction(fab3))
print("fab3是否是generator类型的一个实例:",isinstance(fab3(max),types.GeneratorType))
print("fab3是否是可迭代的:",isinstance(fab3(max),Iterable))
f1=fab3(3)
print('f1:',f1.next())