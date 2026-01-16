import pyautogui

pyautogui.press("win")


pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.sleep(6)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #link do site
pyautogui.press("enter")
pyautogui.sleep(2)

pyautogui.click(x=729, y=475) #clicar no campo do email
pyautogui.write("marcelo@gmail.com") #email de login
pyautogui.press("tab")
pyautogui.write("senhaforte123") #senha de login
pyautogui.press("tab")

pyautogui.press("enter")

pyautogui.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv") #base de dados

print(tabela)

for linha in tabela.index:

    pyautogui.click(x=772, y=321) #clicar no campo do codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo) #digitar o codigo  
    pyautogui.press("tab")
    pyautogui.sleep(2)      

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) #digitar o marca
    pyautogui.press("tab")
    pyautogui.sleep(2)

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo) #digitar o tipo produto
    pyautogui.press("tab")
    pyautogui.sleep(2)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria) #digitar o tipo produto
    pyautogui.press("tab")
    pyautogui.sleep(2)

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco) #digitar o preco produto
    pyautogui.press("tab")
    pyautogui.sleep(2)

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo)) #digitar o custo produto
    pyautogui.press("tab")
    pyautogui.sleep(2)

    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs)) #digitar o Obs produto
    pyautogui.sleep(2)
   
    pyautogui.press("enter")

    pyautogui.scroll(5000) #rolar a tela para cima