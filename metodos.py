from sympy import *
import matplotlib.pyplot as plt

#globais 
y,t = symbols('y t')
listaT = []
listaY = []
arq = open('arquivo.txt','r')
arq_save = open('resultado.txt','w+')
count = 0

def plotG(): # funcao responsavel por printar os graficos
	plt.style.use('ggplot')
	plt.rcParams['figure.figsize'] = (11,7)
	plt.plot(listaT,listaY)
	plt.title('Grafico metodos')
	plt.xlabel('t')
	plt.ylabel('y')
	plt.scatter(listaT, listaY, marker="*", color='red')
	global count;
	count += 1
	string = 'graficos/Figure ' + str(count ) + '.png'
	plt.savefig(string)
	plt.show()
	listaT.clear() # apagando as listas
	listaY.clear()

def euler(expr,y0,t0,h,qnt):
	yn = y0
	tn = t0
	listaY.append(yn)
	listaT.append(tn)
	for i in range(qnt):
		expa = expr.subs([(t,tn),(y,yn)])
		yn += expa*h
		tn += h
		listaY.append(yn)
		listaT.append(tn)
'''
def euler_inverso_implicito(expr,y0,t0,h,qnt): # yn+1 = yn + fn+1*h
	yn = y0
	tn = t0
	listaY.append(yn)
	listaT.append(tn)
	for i in range(qnt):
		tn += h
		yn += expr.subs(t,tn) * h
		yn = solve(Eq(y,yn),y) # y = f(y)
		yn = yn[0]
		listaY.append(yn)
		listaT.append(tn)
'''
def euler_inverso(expr,y0,t0,h,qnt): # yn+1 = yn + fn+1*h
	yn = y0
	tn = t0
	listaY.append(yn)
	listaT.append(tn)
	for i in range(qnt):
		tn += h
		expa = expr.subs([(t,tn),(y,yn)])
		aux = yn + expa*h
		yn += h*expr.subs([(t,tn),(y,aux)])
		listaY.append(yn)
		listaT.append(tn)

def euler_aprimorado(expr,y0,t0,h,qnt):
	yn = y0
	tn = t0
	listaY.append(yn)
	listaT.append(tn)
	for i in range(qnt):
		a = expr.subs([(t,tn),(y,yn)])
		b = expr.subs([(t,tn+h),(y,yn + h*a)])
		yn += ((a+b)/2) * h
		tn += h
		listaY.append(yn)
		listaT.append(tn)

def runge_kutta(expr,y0,t0,h,qnt):
	yn = y0
	tn = t0
	listaY.append(yn)
	listaT.append(tn)
	for i in range(qnt):
		k1 = expr.subs([(t,tn),(y,yn)]) # f(tn,yn)
		k2 = expr.subs([(t,tn + (h/2) ),(y,yn + ((h/2)*k1))])
		k3 = expr.subs([(t,tn + (h/2) ),(y,yn + ((h/2)*k2))])
		k4 = expr.subs([(t,tn + h),(y,yn + h*k3)])
		yn += (h/6) * (k1 + (2*k2) + (2*k3) + k4)
		tn += h
		listaY.append(yn)
		listaT.append(tn)
	
def calcular_por_metodos_anteriores(expr,y0,t0,h,qnt,grau,metodo):
	if metodo == 'euler' :
		euler(expr,y0,t0,h,grau-1)
	elif metodo == 'euler_inverso' :
		euler_inverso(expr,y0,t0,h,grau-1)
	elif metodo == 'euler_aprimorado' :
		euler_aprimorado(expr,y0,t0,h,grau-1)
	elif metodo == 'runge_kutta' :
		runge_kutta(expr,y0,t0,h,grau-1)

def adam_bashforth(expr,y0,t0,h,qnt,grau,metodo='nenhum'):
	if metodo != 'nenhum':
		calcular_por_metodos_anteriores(expr,y0,t0,h,qnt,grau,metodo)
	yn = listaY[grau-1]
	tn = listaT[grau-1]
	
	if grau == 2 :
		coef_list = [3,-1]
		haux = 2
	if grau == 3 :
		coef_list = [23,-16,5]
		haux = 12
	if grau == 4 :
		coef_list = [55,-59,37,-9]
		haux = 24
	if grau == 5 :
		coef_list = [1901,-2774,2616,-1274,251]
		haux = 720
	if grau == 6 :
		coef_list = [4277,-7923,9982,-7298,2877,-475]
		haux = 1440
	if grau == 7 :
		coef_list = [198721,-447288,705549,-688256,407139,-134472,19087]
		haux = 60480
	if grau == 8 :
		coef_list = [434241,-1152169,2183877,-2664477,2102243,-1041723,295767,-36799]
		haux = 120960

	for i in range(grau-1,qnt): # i começa do grau ja que foi calculado os y's anteriores com outros metodos
		k = 0
		aux = 0
		for j in range(grau) :
			aux += coef_list[j]*expr.subs([(t,listaT[i-k]),(y,listaY[i-k])])
			k += 1
		yn += aux*(h/haux)
		tn += h
		listaT.append(tn)
		listaY.append(yn)

def adam_multon(expr,y0,t0,h,qnt,grau,metodo='nenhum'):
	if metodo != 'nenhum':
		calcular_por_metodos_anteriores(expr,y0,t0,h,qnt,grau,metodo)
	yn = listaY[grau-1]
	tn = listaT[grau-1]

	if grau == 2 :
		coef_list = [1,1]
		haux = 2
	if grau == 3 :
		coef_list = [5,8,-1]
		haux = 12
	if grau == 4 :
		coef_list = [9,19,-5,1]
		haux = 24
	if grau == 5 :
		coef_list = [251,646,-264,106,-19]
		haux = 720
	if grau == 6 :
		coef_list = [475,1427,-798,482,-173,27]
		haux = 1440
	if grau == 7 :
		coef_list = [19087,65112,-46461,37504,-20211,6312,-863]
		haux = 60480
	if grau == 8 :
		coef_list = [36799,139849,-121797,123133,-88547,41499,-11351,1375]
		haux = 120960

	for i in range(grau-1,qnt): # i começa do grau ja que foi calculado os y's anteriores com outros metodos
		k = 0
		aux = 0
		tn += h
		for j in range(1,grau):
			aux += coef_list[j]*expr.subs([(t,listaT[i-k]),(y,listaY[i-k])])
			k += 1
		aux += coef_list[0]*expr.subs(t,tn)
		yn += aux*(h/haux)
		yn = solve (Eq(y,yn),y)
		yn = yn[0]
		listaT.append(tn)
		listaY.append(yn)

def formula_inversa(expr,y0,t0,h,qnt,grau,metodo='nenhum'):
	if metodo != 'nenhum': # caso tenha q calcular por outros metodos
		calcular_por_metodos_anteriores(expr,y0,t0,h,qnt,grau,metodo)
	yn = listaY[grau-1] # aqui eu atribuo ao yn e ao tn o ultimo valor calculado por outros metodos 
	tn = listaT[grau-1]
	# essa parte apenas vai selecionar o grau e de acordo com o mesmo vai criar uma lista de coeficientes
	if grau == 2 :
		coef_list = [4,-1,2]
		haux = 3
	if grau == 3 :
		coef_list = [18,-9,2,6]
		haux = 11
	if grau == 4 :
		coef_list = [48,-36,16,-3,12]
		haux = 25
	if grau == 5 :
		coef_list = [300,-300,200,-75,12,60]
		haux = 137
	if grau == 6 :
		coef_list = [360,-450,400,-225,72,-10,60]
		haux = 147

	for i in range(grau-1,qnt): # i começa do grau ja que foi calculado os y's anteriores com outros metodos
		yn = 0
		k = 0 
		for j in range(grau): # o yn vai ser a soma dos coef(j)*y(i-k) onde j = [0...grau] e os y anteriores
			yn += coef_list[j]*listaY[i-k]
			k += 1
		tn += h # incrementa o tn para poder substituir 
		yn += h*coef_list[grau]*expr.subs(t,tn) # isso faz parte da formula inversa
		yn /= haux # isso tambem
		yn = solve(Eq(y,yn),y) # aqui eu resolvo de forma implicita 
		yn = yn[0] # solve retorna uma lista e oq me interessa é o primeiro valor
		listaT.append(tn) 
		listaY.append(yn)

def printar(y0,t0,h,qnt,nome):
	print('Metodo %s ' %(nome),file = arq_save)
	print("y(%.4f) = %.4f" %(t0,y0),file = arq_save)
	print("h = %.4f" %(h),file = arq_save)
	for i in range(qnt+1):
		print("%d %f" %(i,listaY[i]),file = arq_save)
	arq_save.write('\n')

def seleciona_metodo(expr,y0,t0,h,qnt,nome,grau):
	if nome == 'euler':
		euler(expr,y0,t0,h,qnt)
	elif nome == 'euler_inverso':
		euler_inverso(expr,y0,t0,h,qnt)
	elif nome == 'euler_aprimorado':
		euler_aprimorado(expr,y0,t0,h,qnt)
	elif nome == 'runge_kutta':
		runge_kutta(expr,y0,t0,h,qnt)
	elif nome == 'adam_bashforth':
		adam_bashforth(expr,y0,t0,h,qnt,grau)
	elif nome == 'adam_bashforth_by_euler' :
		adam_bashforth(expr,y0,t0,h,qnt,grau,'euler')
	elif nome == 'adam_bashforth_by_euler_inverso':
		adam_bashforth(expr,y0,t0,h,qnt,grau,'euler_inverso')
	elif nome == 'adam_bashforth_by_euler_aprimorado':
		adam_bashforth(expr,y0,t0,h,qnt,grau,'euler_aprimorado')
	elif nome == 'adam_bashforth_by_runge_kutta':
		adam_bashforth(expr,y0,t0,h,qnt,grau,'runge_kutta')
	elif nome == 'adam_multon':
		adam_multon(expr,y0,t0,h,qnt,grau)
	elif nome == 'adam_multon_by_euler':
		adam_multon(expr,y0,t0,h,qnt,grau,'euler')
	elif nome == 'adam_multon_by_euler_inverso':
		adam_multon(expr,y0,t0,h,qnt,grau,'euler_inverso')
	elif nome == 'adam_multon_by_euler_aprimorado':
		adam_multon(expr,y0,t0,h,qnt,grau,'euler_aprimorado')
	elif nome == 'adam_multon_by_runge_kutta':
		adam_multon(expr,y0,t0,h,qnt,grau,'runge_kutta')
	elif nome == 'formula_inversa':
		formula_inversa(expr,y0,t0,h,qnt,grau)
	elif nome == 'formula_inversa_by_euler':
		formula_inversa(expr,y0,t0,h,qnt,grau,'euler')
	elif nome == 'formula_inversa_by_euler_inverso':
		formula_inversa(expr,y0,t0,h,qnt,grau,'euler_inverso')
	elif nome == 'formula_inversa_by_euler_aprimorado':
		formula_inversa(expr,y0,t0,h,qnt,grau,'euler_aprimorado')
	elif nome == 'formula_inversa_by_runge_kutta':
		formula_inversa(expr,y0,t0,h,qnt,grau,'runge_kutta')
	
def main():
	y,t = symbols('y t')
	lista_de_expressoes = arq.readlines()
	
	for i in lista_de_expressoes: # percorrendo as listas de expressoes
		atual = i.split(" ")
		nome = atual[0]
		grau = 1
		if (nome == 'adam_bashforth' or nome == 'adam_multon' or nome == 'formula_inversa'):
			t0 = float(atual[-5])
			h = float(atual[-4])		
			qnt = int(atual[-3])
			expr = simplify(atual[-2])
			tn = t0
			grau = int(atual[-1])
			if nome == 'adam_bashforth':
				for j in range(1,grau+1):
					listaY.append(float(atual[j]))
				for k in range(grau):
					tn += h
					listaT.append(tn)
			else :
				listaY.append(float(atual[1]))
				for j in range(1,grau):
					listaY.append(float(atual[j]))
				for k in range(grau):
					listaT.append(tn)
					tn += h
			y0 = listaY[0]
		elif(nome == 'euler' or nome =='euler_inverso' or nome == 'euler_aprimorado' or nome == 'runge_kutta'):
			y0 = float(atual[1])
			t0 = float(atual[2])
			h = float(atual[3])		
			qnt = int(atual[4])
			expr = simplify(atual[5])
		else :
			y0 = float(atual[1])
			t0 = float(atual[2])
			h = float(atual[3])		
			qnt = int(atual[4])
			expr = simplify(atual[5])
			grau = int(atual[6])

		seleciona_metodo(expr,y0,t0,h,qnt,nome,grau)
		printar(y0,t0,h,qnt,nome)
		plotG()

	arq.close()	
	arq_save.close()

if __name__ == '__main__':
	main()