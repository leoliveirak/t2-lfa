class AP:
    def __init__(self, Q, Sigma, gama, delta, q0, F):
        self._Q = Q
        self._Sigma = Sigma
        self._gama = gama
        self._delta = delta
        self._q0 = q0
        self._F = F
        self._estado_atual = q0

    def realizar_transicao(self, q, appendpilha, poppilha, pilha):
        if(poppilha != 'EMPTY'):
            pilha.pop()
        
        if(appendpilha != 'EMPTY'):
            pilha.append(appendpilha)
        
        if(q not in self._Q):
            raise Exception(f"Estado {q} não pertence ao conjunto de estados Q")
        else:
            self._estado_atual = q
        
        return pilha