# Autômato com Pilha para Reconhecimento de Sequências de DNA (Regra de Chargaff)

## Integrantes

- Leonardo de Oliveira
- Gustavo Botezini


## Descrição

Este projeto implementa um autômato com pilha (PDA) para reconhecer sequências de DNA que obedecem à seguinte propriedade (Regra de Chargaff): a quantidade de bases nitrogenadas do tipo Adenina (A) deve ser igual à quantidade de Timina (T), e a sequência deve terminar com o símbolo `#`.

Bases nitrogenadas possíveis:
- Adenina (A)
- Guanina (G)
- Citosina (C)
- Timina (T)

Exemplos de sequências aceitas:
- `AGCT#`
- `AATT#`

Exemplos de sequências rejeitadas:
- `AAAC#` (quantidade de A ≠ quantidade de T)
- `AATT` (não termina com #)

## Especificação do Autômato

- O autômato segue as especificações de autômatos com pilha dadas em aula.
- Para cada estado, símbolo de entrada e símbolo da pilha, existe no máximo uma transição possível.
- O autômato é determinístico.

## Implementação

- Linguagem: Python
- O autômato é implementado nos arquivos `main.py` e `pda.py`.
- A função de transição é explicitamente definida como um dicionário.

## Como usar

1. Instale o Python 3.x.
2. Clone este repositório.
3. Execute o arquivo principal:

   ```
   python main.py
   ```

4. Modifique a variável `entrada` em `main.py` para testar diferentes sequências.

## Testes

Altere a variável `entrada` em `main.py` para testar diferentes sequências de DNA, seguindo o formato especificado.

## Referências

- [Wikipedia: Regra de Chargaff](https://pt.wikipedia.org/wiki/Regra_de_Chargaff)
- Material de aula sobre autômatos com pilha.