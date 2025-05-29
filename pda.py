from collections import deque
from constants import EPSILON
class AP:
    def __init__(self, Q, Sigma, gama, delta, q0, F):
        self._Q = Q
        self._Sigma = Sigma
        self._gama = gama
        self._delta = delta
        self._q0 = q0
        self._F = F
        self.qA = q0
        self._stack = deque()

    def clean(self):
        self.qA = self._q0
        self._stack.clear()

    def realizar_transicao(self, q, appendpilha, poppilha):
        if(poppilha != EPSILON):
            self._stack.pop()
        
        if(appendpilha != EPSILON):
            self._stack.append(appendpilha)
        
        if(q not in self._Q):
            raise Exception(f"Estado {q} não pertence ao conjunto de estados Q")
        else:
            self.qA = q

    def run(self, entrada):
        self.clean()

        self._stack.append(EPSILON)

        for simbolo in entrada:
            if simbolo not in self._Sigma:
                print(f"Símbolo {simbolo} não pertence ao alfabeto Sigma")
                return False
            self.fazer_transicao_vazia_se_existir()
            transicao = self._delta.get((self.qA, simbolo, self._stack[-1]))
            if transicao:
                self.realizar_transicao(transicao[0], transicao[1], self._stack[-1])
        if self.qA in self._F:
            return True
        else:
            return False

    def fazer_transicao_vazia_se_existir(self):
        transicao = self._delta.get((self.qA, EPSILON, EPSILON))
        if transicao:
            print(f"DEBUG: Fez transição vazia: {transicao}")
            self.realizar_transicao(transicao[0], transicao[1], EPSILON)
            return True
        return False
        