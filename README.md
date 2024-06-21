# Calculadora de IMC

Este projeto é uma aplicação gráfica simples desenvolvida em Python usando a biblioteca Dear PyGui. A aplicação permite calcular o Índice de Massa Corporal (IMC) de uma pessoa com base no peso e altura fornecidos pelo usuário.

## Funcionalidades

- **Entrada de Dados:**
  - **Peso:** Campo de texto para o usuário inserir o peso (em quilogramas).
  - **Altura:** Campo de texto para o usuário inserir a altura (em metros).

- **Cálculo do IMC:**
  - A aplicação calcula o IMC com base na fórmula: `IMC = peso / (altura ** 2)`.
  - Classifica o resultado do IMC nas seguintes categorias:
    - **Magreza:** IMC < 18.5
    - **Normal:** 18.5 <= IMC < 24.9
    - **Sobrepeso:** 24.9 <= IMC < 29.9
    - **Obesidade:** 29.9 <= IMC < 39.9
    - **Obesidade Grau 2:** IMC >= 39.9
  - Exibição de mensagens de erro caso os valores inseridos não sejam válidos.

- **Interface Gráfica:**
  - Interface intuitiva com campos de texto e botão para cálculo.
  - Exibição do resultado do IMC e a classificação na própria janela da aplicação.

## Requisitos

- Python 3.x
- Biblioteca Dear PyGui

Você pode instalar a biblioteca necessária utilizando o pip:
```sh
pip install dearpygui
