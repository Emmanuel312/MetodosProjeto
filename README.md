# MetodosNumericos

Aplicações dos Métodos Numéricos feitos por Emmanuel Nery (efn@cin.ufpe.br) utilizando a linguagem de programação Python

## Métodos Implementados

```
	1 - Euler Simples
	2 - Euler Inverso
	3 - Euler Aprimorado
	4 - Runge-Kutta  
	5 - Adam-Bashforth (1ª Ordem)
	6 - Adam-Bashforth (2ª Ordem)
	7 - Adam-Bashforth (3ª Ordem)
	8 - Adam-Bashforth (4ª Ordem)
	9 - Adam-Bashforth (5ª Ordem)
	10 - Adam-Bashforth (6ª Ordem)
  	11 - Adam-Bashforth (7ª Ordem)
  	12 - Adam-Bashforth (8ª Ordem)
	14 - Adam-Moulton (1ª Ordem)
	15 - Adam-Moulton (2ª Ordem)
	16 - Adam-Moulton (3ª Ordem)
	#17 - Adam-Moulton (4ª Ordem)
	18 - Adam-Moulton (5ª Ordem)
	19 - Adam-Moulton (6ª Ordem)
  	20 - Adam-Moulton (7ª Ordem)
  	21 - Adam-Moulton (8ª Ordem)
```

## Informações Gerais

### Dependências

Para executar o programa é necessário estar em ambiente ***Linux*** e com a biblioteca [Simpy](http://docs.sympy.org/latest/install.html) instalada em sua máquina.

### Executando o Código

```
$ python3 metodos.py

```

### Entradas

É possível de duas formas:

#### Diretamente pelo terminal

Basta digitar os valores que são pedidos no terminal

#### Através de arquivo texto

Deverá ter o seguinte formato:

```
(número referente ao método escolhido)
dF(y, t)/dt
t0
Y(0)
h
tf
grau (Se o método escolhido for Adams-Bashforth ou Adams-Moulton, o campo deve ficar vazio caso contrário)
```

Exemplo de entrada:

```
1
1 - t + 4*y
0
1
0.05
1
```
