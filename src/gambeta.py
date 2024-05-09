import pygetwindow
import pyautogui
import time

# Título da janela do Microsoft Teams
title = 'Microsoft Teams'

# Obtém a primeira janela com o título especificado
window = pygetwindow.getWindowsWithTitle(title)[0]

# Redimensiona a janela para 1280x720 pixels
window.resizeTo(1280, 720)

# Ativa a janela (traz para a frente)
window.activate()

while True:
    pyautogui.write('a')
    time.sleep(30)  # Espera 30 segundos
