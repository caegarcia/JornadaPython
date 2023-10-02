# Passo a passo do projeto
# Passo 1: Entrar no site da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2: Fazer login
# 3: Importar a base de dados de produtos
# 4: Cadastrar 1 produto
# 5: Repetir o cadastro para todosos produtos

# .click => clicar / .write => escrever / .press => aperta 1 tecla / .hotkey => atalho (combinacao)

import pyautogui #roda no terminal pip install pyautogui
import time

pyautogui.PAUSE = 0.5 #tempo de espera entre todos os comandos do pyautogui

pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

time.sleep(3)

pyautogui.click (x=4046, y=449, clicks = 1, button = "left") #passo para selecionar o usuario no chrome

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write (link)

pyautogui.press ("enter")

time.sleep(5) #pausa apenas nessa passagem

pyautogui.click(3693, y=599)

login ="pythonimpressionador@gmail.com"

pyautogui.write (login)

pyautogui.press ("tab")

senha = "1234"
pyautogui.write (senha)

pyautogui.press ("tab")
pyautogui.press ("enter")

# importando outra biblioteca para ajudar na BD # pip instal pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("C:/Users/SOUSAC13/OneDrive - Heineken International/Caetano/#Treinamentos/produtos.csv")

for linha in tabela.index:
    pyautogui.click(x=3672, y=425)
    codigo = tabela.loc[linha, "codigo"] #voce pode fazer assim e pedir pra ele escrever a variavel, ou pode pedir pra ele escrever direto a localizacao
    marca = tabela.loc[linha, "marca"]

    pyautogui.write(str(codigo))
    pyautogui.press ("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press ("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press ("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press ("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press ("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press ("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
            pyautogui.write(str(tabela.loc[linha, "obs"]))
   
    pyautogui.press ("tab")

    pyautogui.scroll(500)

#Fim de looping


