def calculator(func,*args):
	return func(*args)

def sum_num(*args):
	return sum(args)

def sub_num(*args):
	return args[0] - args[1]

def mul_num(*args):
	return args[0] * args[1]

def div_num(*args):
	return args[0] / args[1]