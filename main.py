import pyautogui as py
import pandas as pd
import time
import keyboard

py.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
email = 'email@email.com'
password = 'password'

tabela = pd.read_csv('produtos.csv')

# Acess the browser and open the website
py.press('win')
py.write('brave')
py.press('enter')
py.write(link)
py.press('enter')
time.sleep(3)

# Fill in the login form
py.click(x=529, y=367)
py.write(email)
py.press('tab')
py.write(password)
py.press('tab')
py.press('enter')

# Fill the form with data from the CSV file
for linha in tabela.index:
    py.click(x=517, y=254)
    py.write(str(tabela.loc[linha, 'codigo']))
    py.press('tab')
    py.write(str(tabela.loc[linha, 'marca']))
    py.press('tab')
    py.write(str(tabela.loc[linha, 'tipo']))
    py.press('tab')
    py.write(str(tabela.loc[linha, 'categoria']))
    py.press('tab')
    py.write(str(tabela.loc[linha, 'preco_unitario']))
    py.press('tab')
    py.write(str(tabela.loc[linha, 'custo']))
    py.press('tab')
    if str(tabela.loc[linha, 'obs']) != 'nan':
        py.write(str(tabela.loc[linha, 'obs']))
    py.press('tab')
    py.press('enter')
    py.scroll(5000)