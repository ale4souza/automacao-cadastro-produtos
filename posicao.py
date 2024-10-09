import pyautogui
import time

# Espera 5 segundos para você posicionar o cursor no local desejado
print("Mova o cursor para o local desejado em 5 segundos...")
time.sleep(5)

# Captura a posição atual do cursor e imprime
posicao = pyautogui.position()
print(f"A posição atual do cursor é: {posicao}")