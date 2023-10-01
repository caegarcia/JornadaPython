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

pyautogui.PAUSE = 0.5

pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

time.sleep(3)

pyautogui.click (x=765, y=608, clicks = 2, button = "left") #passo para selecionar o usuario no chrome

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write (link)

pyautogui.press ("enter")

time.sleep(3)

login ="pythonimpressionador@gmail.com"

pyautogui.click (x=704, y=614)
pyautogui.write (login)

senha = "1234"

pyautogui.press ("tab")

pyautogui.write (senha)

pyautogui.press ("tab")
pyautogui.press ("enter")

# importando outra biblioteca para ajudar na BD # pip instal pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("C:/Users/SOUSAC13/OneDrive - Heineken International/Caetano/#Treinamentos/produtos.csv")



