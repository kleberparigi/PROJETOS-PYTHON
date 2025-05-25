CURSO PYTHON 
AULA 02
PYTHON AUTOMAÇÃO DE TAREFAS

!!!!!!!!!!!!!!VERIFICAR BIBLIOTECAS EXISTENTES
EXEMPLO PYCHARM O QUE É 

INSTALAR JUPITER EM LINK
https://www.youtube.com/watch?v=_eK0z5QbpKA

ESCREVER CÓDIGO INICIALMENTE COLOCANDO O PASSO A PASSO DA LÓGICA

caixa de perguntas @hashtagprogramacao

#passo 1 - importar base pegar banco de dados
#passo 2 - visualizar o banco de dados capturado
#passo 2.1 - entender as informações
#passo 2.2 - procurar os erros do banco de dados capturado
#passo 3 - tratamento das informações
#passo 3.1 - valores e formato errado
#passo 3.2 - valores nulos e obrigados
#passo 4 - analise inicial dos dadso tratados 
#passo 5 - analise completa dos dados tratadoss


*******************************************************
#precisa usar pandas - biblioteca
*******************************************************
#passo1

import pandas as pd
#nome = pandas leitura e extensão do arquivo
#nome = pandas.read_bak(nome_do_banco_sem_espaço)
tabela = pd.read_csv("clientes.csv")

*******************************************************
#passo2
display(tabela)
#display(nome_do_criado_de_leitura)
#erro utf caracteres especiais
#correção
tabela = pd.read_csv("clientes.csv"), encoding ="latin")
#ajustando separação
tabela = pd.read_csv("clientes.csv"), encoding ="latin"), sep =";")
#novamente display
display.(tabela)

#deletando colunas erradas inutil

tabela = tabela.drop()
#tabela = tabela.drop(nome de que você quer deletar, eixo)
#exemplo: tabela = tabela.drop("unamed 8", axis =1) 1= Coluna 0=linha
abela = tabela.drop("unamed 8", axis =1)

#se houver duas colunas com o mesmo nome o python altera o nome em leitura



*******************************************************

*******************************************************
#passo3

*******************************************************

*******************************************************
#passo4

*******************************************************

*******************************************************
#passo5

*******************************************************