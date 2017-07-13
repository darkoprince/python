def calculate (op1, op2, f):
	if f == "add":
		return op1 + op2 
	elif f == "subtract":
		return op1 - op2
	elif f == "multiply":
		return op1 * op2 
	elif f == "division":
		return op1 /op2
	else:
		print ("invalid")

print("Options")
print(" ")
print("add")
print("subtract")
print("multiply")
print("division")

print(" ")		
	
Options= raw_input("Enter Options:")
print(" ")
op1 = int(raw_input("Enter first number: "))
op2 = int(raw_input("Enter second number: "))

results = calculate(op1, op2, Options)
print results



i = 7
while (i < 20):
	i = i + 1
	print i
	
p = 2
while (p < 40):
	p = p +2
	print p
	
