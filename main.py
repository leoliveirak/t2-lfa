from pda import AP
from constants import EPSILON

# Definição do autômato de pilha
Q = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
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
	
	('q1', '#', '$'): ('q4', EPSILON),
	
	('q2', EPSILON, EPSILON): ('q1', 'A'),
	
	('q3', EPSILON, EPSILON): ('q1', 'T'),
}
F = ['q4']

# Criação do autômato de pilha
pda = AP(Q, Sigma, gama, delta, 'q0', F)

# Testes
sequencia_testes = [
	("AAACGCCTCATTAAAGTGGTTT#", True),
	("AAACGCCTCATTAAAGTGGTTT", False),
	("AAACGCCTCATTAAAGTGGTTT#A", False),
	("AAACGCCTCATTAAAGTGGTTT#G", False),
	("AAACGCCTCATTAAAGTGGTTT#C", False),
	("AAACGCCTCATTAAAGTGGTTT#T", False),
    ("ABBC#", False),
    ("ACGTACGT#", True),
    ("##", False),
    ("#", True),
    ("###", False),
    ("", False),
    ("AGATAGAT#", False),
    ("AGGTCGAGGTCGAGGTCGAGGTCGAGGTCG#", True),
    ("AGCT#", True),
    ("AATT#", True),
    ("AAAC#", False),
    ("AATT", False),
]

for entrada, esperado in sequencia_testes:
	resultado = pda.run(entrada)
	print(f"entrada: {entrada}")
	print(f"esperado: {esperado}, obtido: {resultado}")
	print()