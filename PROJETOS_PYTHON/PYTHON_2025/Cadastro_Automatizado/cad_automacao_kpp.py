#Projeto 01 - Hashtag
#kpp_automacao
#Passo 01: entrar no sistema ficticio - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo 02: fazer login
#Passo 03: Importar a base de dados em csv
#Passo 04: Cadastrar 01 produto
#Passo 05: Repetir ação para todos os produtos
#===================================================================================================
#Acessando o sistema automaticamente
import pyautogui
import time 
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #aguardar para pegar a posição print(pyautogui.position())
#utilizado
#import time
#import pyautogui
#time.sleep(5)
#print(pyautogui.position())
pyautogui.click(x=415, y=413)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=660, y=569) # clique no botao de login
time.sleep(2)
pyautogui.click(x=838, y=365)
time.sleep(2.5)
pyautogui.click(x=398, y=293)
time.sleep(1.5)
#===================================================================================================
#alimentando com os dados / cadastrando os produtos
#utilizando pandas
import pandas as pd
tabela = pd.read_csv("produtos.csv") #"tabela" variavel para usar com pandas
print(tabela)
#cadastrar produto em sistema online da empresa
for linha in tabela.index: #para cada linha da tabela
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): #pd.isna retornar true se o valor é vazio (nan), neste caso if not ... mostrará o que não está vazio
        #poderia usar como também if obs != "nan":
        #ou mais limpo:
        #obs = tabela.loc[linha, "obs"]
        #if pd.notna(obs):
        #pyautogui.write(str(obs))
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    pyautogui.PAUSE = 0.3
    # dar scroll de tudo pra cima11.0       
    pyautogui.scroll(10000)
    # Passo 5: Repetir o processo de cadastro até o fim 
    pyautogui.click(x=392, y=288)    
  
     