# AutPac – Calculadora de Parcelamento em Python

## 📌 Sobre o projeto

O **AutPac** é uma ferramenta simples desenvolvida em **Python** para automatizar o cálculo de datas de parcelamento.

O programa recebe prazos de pagamento (ex: `28/35/42`) e calcula automaticamente as datas correspondentes com base na data atual ou no dia anterior.

Além disso, o sistema aplica uma regra importante utilizada em rotinas financeiras:

* O cálculo é feito em **dias corridos**
* Se a data cair em **sábado ou domingo**, o sistema **adianta automaticamente 2 dias** para evitar finais de semana.

Esse projeto foi criado com o objetivo de **automatizar uma tarefa repetitiva do dia a dia**, além de servir como **exercício prático de desenvolvimento em Python**.

---

## ⚙️ Tecnologias utilizadas

* Python 3
* Biblioteca padrão `datetime`

---

## 🧠 Funcionalidades

* Entrada de múltiplos prazos (ex: `28/35/42`)
* Cálculo automático das datas
* Ajuste automático para finais de semana
* Saída formatada em **DD/MM/AAAA**

Exemplo de uso:

Entrada:

28/35/42

Saída:

28 dias -> 09/04/2026
35 dias -> 16/04/2026
42 dias -> 23/04/2026

---

## 🚀 Como executar o projeto

### 1️⃣ Clonar o repositório

git clone https://github.com/SEU-USUARIO/AutPac.git

### 2️⃣ Entrar na pasta do projeto

cd AutPac

### 3️⃣ Executar o script

python App.py

---

## 💻 Executando a versão compilada (.exe)

Se o executável estiver disponível, basta acessar a pasta:

dist/

e executar:

App.exe

---

## 📂 Estrutura do projeto

AutPac
│
├ App.py
├ README.md
├ .gitignore
└ dist/ (gerado automaticamente)

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido para:

* Automatizar cálculos de datas de parcelamento
* Praticar conceitos de **Python**
* Trabalhar com **manipulação de datas**
* Criar uma ferramenta simples de uso no ambiente de trabalho

---

## 👨‍💻 Autor

Desenvolvido por **Samuel Ferreira Lopes**
