#prac_sensspecf1 Chris Park

def sensspecf1(TP, FP, TN, FN):
	sens = TP/(TP+FN)
	spec = TN/(TN+FP)
	f1 = 2/((1/sens)+(1/spec))
	return sens, spec, f1

print(sensspecf1(92, 85, 1815, 8))