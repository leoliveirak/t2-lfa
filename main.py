from pda import AP

# Definição do autômato de pilha
Q = ['q0', 'q1', 'q2', 'q3', 'q4']
Sigma = ['T', 'C', 'A', 'G', 'EMPTY']
gama = ['$', 'T', 'A', 'EMPTY']
delta = {
	('q0', 'EMPTY', 'EMPTY'): ('q1', '$'),
	
	('q1', 'T', '$'): ('q1', '$'),
	('q1', 'C', '$'): ('q1', '$'),
	('q1', 'C', 'T'): ('q1', 'EMPTY'),
	('q1', 'C', 'A'): ('q1', 'EMPTY'),
	('q1', 'T', 'A'): ('q1', 'EMPTY'),
	('q1', 'A', 'T'): ('q1', 'EMPTY'),
	('q1', 'A', '$'): ('q2', '$'),
	('q1', 'A', 'A'): ('q2', 'A'),
	('q1', 'T', '$'): ('q3', '$'),
	('q1', 'T', 'T'): ('q3', 'EMPTY'),
	
	('q2', 'EMPTY', 'EMPTY'): ('q1', 'A'),
	
	('q3', 'EMPTY', 'EMPTY'): ('q1', 'T'),
	
	('q1', 'EMPTY', '$'): ('q4', 'EMPTY'),
}
F = ['q4']

# Criação do autômato de pilha
pda = AP(Q, Sigma, gama, delta, 'q0', F)

# Teste do autômato de pilha com uma entrada
entrada = 'T C A T C A T C A T C A T C A T C A' 

entrada = entrada.strip().split()  # Divide a entrada em símbolos

# Adiciona o símbolo 'EMPTY' ao final da entrada
entrada.append('EMPTY') 

# Adiciona o símbolo 'EMPTY' ao início da entrada
entrada.insert(0, 'EMPTY')


resultado = pda.run(entrada)

if resultado:
    print("A entrada é aceita pelo autômato de pilha.")
else:
    print("A entrada não é aceita pelo autômato de pilha.")