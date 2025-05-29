from pda import AP
from constants import EPSILON

# Definição do autômato de pilha
Q = ['q0', 'q1', 'q2', 'q3', 'q4']
Sigma = ['#', 'T', 'C', 'A', 'G', EPSILON]
gama = ['$', 'T', 'A', EPSILON]
delta = {
	('q0', EPSILON, EPSILON): ('q1', '$'),
    
	('q1', 'G', '$'): ('q1', '$'),
	('q1', 'G', 'T'): ('q1', 'T'),
	('q1', 'G', 'A'): ('q1', 'A'),
    
	('q1', 'C', '$'): ('q1', '$'),
	('q1', 'C', 'T'): ('q1', 'T'),
	('q1', 'C', 'A'): ('q1', 'A'),
    
	('q1', 'A', 'T'): ('q1', EPSILON),
	('q1', 'A', '$'): ('q2', '$'),
	('q1', 'A', 'A'): ('q2', 'A'),
    
	('q1', 'T', 'A'): ('q1', EPSILON),
	('q1', 'T', '$'): ('q3', '$'),
	('q1', 'T', 'T'): ('q3', 'T'),
	
	('q1', '#', '$'): ('q0', EPSILON),
	
	('q2', EPSILON, EPSILON): ('q1', 'A'),
	
	('q3', EPSILON, EPSILON): ('q1', 'T'),
}
F = ['q0']

# Criação do autômato de pilha
pda = AP(Q, Sigma, gama, delta, 'q0', F)

# Testes
# sequencia_testes = {
    
# }

# Teste do autômato de pilha com uma entrada
entrada = "AAACGCCTCATTAAAGTGGTTT#" 

#entrada = entrada.strip().split()  # Divide a entrada em símbolos

# Adiciona o símbolo EPSILON ao final da entrada
#entrada.append(EPSILON) 

# Adiciona o símbolo EPSILON ao início da entrada
#entrada.insert(0, EPSILON)


resultado = pda.run(entrada)

if resultado:
    print("A entrada é aceita pelo autômato de pilha.")
else:
    print("A entrada não é aceita pelo autômato de pilha.")