Sistema Bancário em Python
Este código implementa um sistema bancário simples com operações básicas via terminal, seguindo os requisitos do desafio de projeto DIO.

Principais funcionalidades:
Cadastro de Usuários:

Armazena nome, CPF, data de nascimento e endereço

Valida CPF único para cada usuário

Gerenciamento de Contas Bancárias:

Cadastro de contas vinculadas a usuários

Número de agência fixo "0001"

Numeração automática de contas

Operações Financeiras:

Depósitos (valores positivos)

Saques (limite de R$500 por operação e 3 saques diários)

Visualização de extrato com histórico de movimentações

Estrutura do Sistema:
Dados armazenados em memória (listas e dicionários)

Menu interativo via terminal

Validações básicas nas operações

Regras de Negócio Implementadas:
Limite de R$500 por saque

Máximo de 3 saques diários

Não permitir saldo negativo

CPF como identificador único de usuário

O sistema é executado em loop até que o usuário escolha a opção de sair ("q").

