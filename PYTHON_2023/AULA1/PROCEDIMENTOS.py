CURSO PYTHON 
AULA 01
PYTHON AUTOMAÇÃO DE TAREFAS

!!!!!!!!!!!!!!VERIFICAR BIBLIOTECAS EXISTENTES
EXEMPLO PYCHARM O QUE É 

INSTALAR JUPITER EM LINK
https://www.youtube.com/watch?v=_eK0z5QbpKA

ESCREVER CÓDIGO INICIALMENTE COLOCANDO O PASSO A PASSO DA LÓGICA

PASSO 1 ACESSAR O SISTEMA DA EMPRESA
PASSO 2 FAZER LOGIN DO SISTEMA
PASSO 3 BAIXAR A BASE DE DADOS
PASSO 4 CALCULAR OS INDICADORES 
PASSO 5 ENVIAR UM E-MAIL PARA UM ENDERECO

' # ' COMENTARIO EM PYTHON

#PASSO 1 ACESSAR O SISTEMA DA EMPRESA
#PASSO 2 FAZER LOGIN DO SISTEMA
#PASSO 3 BAIXAR A BASE DE DADOS
#PASSO 4 CALCULAR OS INDICADORES 
#PASSO 5 ENVIAR UM E-MAIL PARA UM ENDERECO

#************
-pyautogui - onde está um monte de tarefas automatizadas prontos
-BIBLIOTECA
-pacote de codigos prontos 
-para instalar !pip install pyautogui 
-depois import pyautogui 
#**************
-- pyautogui.click  -- clicar com mouse 
-- pyautogui.write  -- escrever um texto
-- pyautogui.press  -- apertar uma tecla 
-- pyautogui.hotkey -- apertar uma combinação de teclas

#neste exemplo a pausa
pyautogui.PAUSE
#PASSO 1 ACESSAR O SISTEMA DA EMPRESA
pyautogui.hotkey ("ctrl","t")
pyautogui.write ("caminho do sistema nesse caso um site 'x'")
pyautogui.press ("enter")
time.sleep(5) #time.sleep já é uma biblioteca existente já no python
#--pyautogui.PAUSE 1  ou 2.5 ou 0.5 
pyautogui.click (x=, y= ) #colocar dados onde está o mouse 

#para achar onde está o pontero do mouse 
time.sleep (10)
print(payautogui.position())
point (x=983, y=441) #colocar no click

****************
sempre é necessário importar as bibliotecas
todas as linhas é necessário colocar a biblioteca

no google pyautogui ele trás as opções da biblioteca

#PASSO 2 FAZER LOGIN DO SISTEMA
pegar a posição do click para selecionar o arquivo em driver para fazer o download
button.right (botão direito)

#PASSO 4 CALCULAR OS INDICADORES 
IMPORTANTE
IMPORTAR BASE DE DADOS
PANDAS
import pandas
tabela = pandas.read
colocando o ponto e table ele abre a biblioteca
exemplo
tabela = pandas.read_csv()
"tabela" é o nome do que vem.... pode ser como "Pessoa" / "Processo" / "Desdobramento" / ou "Pessoa_Telefone"
exemplo usado:
tabela = pandas.read_csv("caminho do downloads pra tarzer o arquivo")
depois inserir
print(ytabela) ou usar Display(tabela) -- 
colocando o sep quando necessário 
exemplo 
tabela = pandas.read_csv("caminho do downloads pra tarzer o arquivo", sep=";")

!!!!!!!!!!!!!!!!!!! da para usar AS para apelidar 
exemplo import pandas as pd
tabela = pd.read_csv()

!!!!!!!!!!!!!!!!!!!!!!!!!
para a migração 
precisa criar um padrão de arquivos e documentos e colocar em pasta X baseando em nomes das pastas e scripts - pensamento

#PASSO 4 CALCULAR OS INDICADORES 
#total gasto- somar uma coluna
#exemplo:
total_gasto = tabela["valorFinal"].sum()
#quantidade:
quantidade = tabela["Quantidade"].sum() 
#entre [ ] é para apontar a coluna para ele somar
preco_medio = total_gasto / quantidade 

#PASSO 5 ENVIAR UM E-MAIL PARA UM ENDERECO
outra biblioteca é o pyperclip (copiar)
import pyperclip.copy(texto)
pyautogui.hotkey ("ctrl","v")

Como usar com condição? IF / case?

r ANTES DO TEXTO É PARA CRU FICAR O TEXTO CRU
f FORMATAR 

colocando f.... ele deixa colocar entre { } e dentro dele você coloca o valor como desejar 
exemplo :
texto = f""" 
O valor total é R${total_gasto:,.2f}
"""




**********************************

tecla ESC para a execução e stop tbm
TEM COMO TRANSFORMAR O CÓDIGO EM EXECUTÁVEL 
TEM COMO DEIXAR ELE COMO ROTINA DE EXECUÇÃO 

LINKS: https://www.youtube.com/watch?v=cGSerUmK0CE
LINKS: https://www.youtube.com/watch?v=SxEjHAlCqmo&t=1s

BIBLIOTECA: 
PYAUTOGUI

https://pyautogui.readthedocs.io/en/latest/

caixa de perguntas @hashtagprogramacao                                                                                                                                                                                                                                                                                                          



                                                                                                                                    