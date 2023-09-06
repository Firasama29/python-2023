def list_benefits():
	return ["easy to learn", "easy to write code", "powerful"]

def define_python_benefits(detail):
	return "python is %s " % detail


def justify_learning_python():
	benefits = list_benefits()
	for benefit in benefits:
		print(define_python_benefits(benefit))


