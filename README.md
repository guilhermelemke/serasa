# Automação da Página de login do Site: https://www.serasaconsumidor.com.br

## Objetivo

Testar a funcionalidade de login do site nos seguintes cenários:
* Login sem CPF e assert da mensagem de retorno
* Login com CPF inválido e assert da mensagem de retorno
* Login com CPF válido e assert da mensagem de requisitos de senha

## Pré requisitos para rodar o projeto:

* geckodriver versão 0.28.0 : incluso no projeto
* geckodriver deverá ser rodado pelo menos uma vez na máquina
* Firefox browser: versão 60 ou superior

## Como rodar o projeto:

* Clone esse repositório:  
```git clone https://github.com/guilhermelemke/serasa.git ```  
```cd serasa ```
* Crie um virtualenv com Python 3:  
```python3 -m venv venv ```
* Ative o virtualenv:  
```source venv/bin/activate ```  
* Instale as dependências, pip - windows ou pip3 linux/mac:   
```pip install -r requirements.txt ```
```pip3 install -r requirements.txt ```
* Execuçao dos testes com unittest:   
```cd serasa_project ```
```python3 login.py ```
* Execuçao dos testes BDD com Behave:
```behave ```
