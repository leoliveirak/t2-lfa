from collections import deque

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
        if(poppilha != 'EMPTY'):
            self._stack.pop()
        
        if(appendpilha != 'EMPTY'):
            self._stack.append(appendpilha)
        
        if(q not in self._Q):
            raise Exception(f"Estado {q} não pertence ao conjunto de estados Q")
        else:
            self.qA = q

    def run(self, entrada):
        self.clean()

        self._stack.append('EMPTY')

        for simbolo in entrada:
            print(f"DEBUG: qA: {self.qA}, w[i]: {simbolo}, Pilha: {list(self._stack)}")
            if(self.fazer_transicao_vazia_se_existir()):
                continue
            transicao = self._delta.get((self.qA, simbolo, self._stack[-1]))
            print(f"DEBUG: qA: {self.qA}, w[i]: {simbolo}, Pilha: {list(self._stack)}")
            if transicao:
                self.realizar_transicao(transicao[0], transicao[1], self._stack[-1])

        if self.qA in self._F:
            return True
        else:
            return False

    def fazer_transicao_vazia_se_existir(self):
        transicao = self._delta.get((self.qA, 'EMPTY', 'EMPTY'))
        if transicao:
            print(f"DEBUG: Fez transição vazia: {transicao}")
            self.realizar_transicao(transicao[0], transicao[1], 'EMPTY')
            return True
        return False
        