import pyautogui
import time
import pandas as pd

# Define uma pausa entre as ações para garantir que sejam realizadas no tempo certo
pyautogui.PAUSE = 0.9

# Abrir o navegador Firefox (ajuste "mozilla" caso seja necessário)
pyautogui.press("win")
pyautogui.write("mozilla")
pyautogui.press("enter")
time.sleep(3)  # Aguarda o navegador abrir
    
# Digitar a URL e acessar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)  # Aguarda o site carregar

# Clicar no campo de e-mail com as coordenadas obtidas anteriormente
pyautogui.click(x=423, y=365)  # Substitua pelos valores que você obteve
time.sleep(3)

# Digitar o e-mail
pyautogui.write("email@teste.com")

pyautogui.click(x=400, y=472)  # Substitua pelos valores que você obteve
pyautogui.write("12345")
pyautogui.click(x=400, y=472)
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

tabela = pd.read_csv("produtos.csv")
print(tabela)




linha = 0

for linha in tabela.index:
    pyautogui.click(x=389, y=256)
    #codigo   
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    time.sleep(2)
    pyautogui.press("enter")
    pyautogui.scroll(5000)