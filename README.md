						# Metodos Numericos

Aplicações dos Métodos Numéricos feitos por Emmanuel Nery (efn@cin.ufpe.br) utilizando a linguagem de programação Python

## Métodos Implementados

```
	1 - Euler Simples
	2 - Euler Inverso
	3 - Euler Aprimorado
	4 - Runge-Kutta  
	5 - Adam-Bashforth (2ª Ordem)
	6 - Adam-Bashforth (3ª Ordem)
	7 - Adam-Bashforth (4ª Ordem)
	8 - Adam-Bashforth (5ª Ordem)
	9 - Adam-Bashforth (6ª Ordem)
  	10 - Adam-Bashforth (7ª Ordem)
  	11 - Adam-Bashforth (8ª Ordem)
	12 - Adam-Moulton (2ª Ordem)
	14 - Adam-Moulton (3ª Ordem)
	15 - Adam-Moulton (4ª Ordem)
	16 - Adam-Moulton (5ª Ordem)
>>>>>  	17 - Adam-Moulton (6ª Ordem)   >>>>>
  	18 - Adam-Moulton (7ª Ordem)
  	19 - Adam-Moulton (8ª Ordem)
	20 - Formula-Inversa (2ª Ordem)
	21 - Formula-Inversa (3ª Ordem)
	22 - Formula-Inversa (4ª Ordem)
	23 - Formula-Inversa (5ª Ordem)
	24 - Formula-Inversa (6ª Ordem)
	
```

## Informações Gerais

### Dependências

Para executar o programa é necessário estar em ambiente ***Linux*** e com a biblioteca [Simpy](http://docs.sympy.org/latest/install.html) e o [Matplotlib](http://matplotlib.org/users/installing.html)
instalados em sua máquina.
### Executando o Código

```
$ python3 metodos.py

```

### Entradas

É feita atraves de um arquivo de texto com o nome arquivo.txt e estando no mesmo diretorio do arquivo de codigo-fonte

Deverá ter o seguinte formato:

```
(nome referente ao método escolhido) y0 t0 h quantidade_de_passos dF(y, t)/dt grau (Se o método escolhido for Adams-Bashforth, Adams-Moulton ou Forumula-Inversa o campo deve ficar vazio caso contrário)
Ex :
euler 0 0 0.1 20 1-t+4*y
euler_inverso 0 0 0.1 20 1-t+4*y
# casos especiais dado valores iniciais siga o exemplo
adam_bashforth 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 5 
adam_multon 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
formula_inversa 0.0 0.1 0.23 0.402 0.6328 0 0.1 20 1-t+4*y 6
#
adam_bashforth_by_runge_kutta 0 0 0.1 20 1-t+4*y 6
adam_multon_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
formula_inversa_by_euler_aprimorado 0 0 0.1 20 1-t+4*y 6
```
### Saida

A saida é salva em um arquivo com o nome resultado.txt no mesmo diretorio do arquivo de codigo-fonte.
Os graficos são salvos em um diretorio chamado **graficos** onde o mesmo contem os arquivos de foto com o nome **figure numero.png**.

