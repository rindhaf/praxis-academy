def func1():
	pass

def func2():
	pass

def func3():
	pass

executing = lambda f: f()
map(executing, [func1, func2, func3])