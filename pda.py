from collections import deque

class AP:
    def __init__(self, Q, Sigma, gama, delta, q0, F):
        self._Q = Q
        self._Sigma = Sigma
        self._gama = gama
        self._delta = delta
        self._q0 = q0
        self._F = F
        self._estado_atual = q0
        self._stack = deque()

    def clean(self):
        self._estado_atual = self._q0
        self._stack.clear()

    def realizar_transicao(self, q, appendpilha, poppilha):
        if(poppilha != 'EMPTY'):
            self._stack.pop()
        
        if(appendpilha != 'EMPTY'):
            self._stack.append(appendpilha)
        
        if(q not in self._Q):
            raise Exception(f"Estado {q} não pertence ao conjunto de estados Q")
        else:
            self._estado_atual = q

    def run(self, entrada):
        self.clean()

        self._stack.append('EMPTY')

        for simbolo in entrada:
            print(f"Estado atual: {self._estado_atual}, Símbolo: {simbolo}, Pilha: {list(self._stack)}")
            transicao = self._delta.get((self._estado_atual, simbolo, self._stack[-1]))
            self.realizar_transicao(transicao[0], transicao[1], self._stack[-1])

        if self._estado_atual in self._F:
            return True
        else:
            return False