# 📘 Assignment: Hangman Game in Python

## 🎯 Objective

Pratique manipulação de strings, listas, entrada de dados, loops e condicionais ao criar um jogo da Forca em Python. O objetivo é adivinhar uma palavra oculta antes que as tentativas se esgotem.

## 📝 Tasks

### 🛠️ Preparar a Palavra e o Progresso do Jogo

#### Descrição
Crie a estrutura inicial do jogo: selecione uma palavra aleatoriamente de uma lista e prepare uma forma de mostrar quais letras já foram descobertas.

#### Requisitos
O programa concluído deve:

- Manter uma lista predefinida com pelo menos cinco palavras.
- Selecionar aleatoriamente uma palavra dessa lista.
- Exibir cada letra ainda não descoberta como `_`, mantendo visíveis as letras acertadas.

### 🛠️ Implementar as Rodadas e o Resultado

#### Descrição
Permita que o jogador tente adivinhar a palavra uma letra por vez. Atualize o progresso e as tentativas restantes até que o jogador vença ou perca.

#### Requisitos
O programa concluído deve:

- Solicitar palpites de uma letra usando `input()`.
- Revelar no progresso todas as posições em que a letra escolhida aparece.
- Reduzir as tentativas restantes quando o palpite não estiver na palavra e exibir esse total.
- Encerrar quando todas as letras forem adivinhadas ou não houver tentativas restantes.
- Exibir uma mensagem de vitória ou derrota; em caso de derrota, revelar a palavra.
