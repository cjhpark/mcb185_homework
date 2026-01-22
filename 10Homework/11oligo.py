#For <=13nt, Tm = (A+T)*2 + (G+C)*4
#For >13nt, Tm = 64.9+41*(G + C -16.4)/(A+C+T+G)

def oligotm(A, C, T, G):
	if A+C+T+G == 0: return None
	elif A+C+T+G <=13: return (A+T)*2 + (G+C)*4
	else: return 64.9+41*(G+C-16.4)/(A+T+G+C)

print(oligotm(5, 4, 7, 3))
