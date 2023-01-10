import time
import PySimpleGUI
import pyautogui
import pyperclip


pyautogui.PAUSE = 1.5

# abrir o crhome
pyautogui.click(x=78, y=1059)
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=683, y=604)

#abrir pagina drive
pyautogui.click(x=624, y=50)
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')

time.sleep(5)

#abrir pasta com o relatorio e efetuar o download
pyautogui.click(x=330, y=236, clicks=2)
time.sleep(5)
pyautogui.click(x=330, y=266)
pyautogui.click(x=1733, y=151)
pyautogui.click(x=1563, y=510)

#abrir email
pyautogui.hotkey("ctrl", "t")
pyautogui.click(x=624, y=50)
pyperclip.copy("https://mail.google.com/mail/u/2/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press('enter')
time.sleep(5)

#enviar email
pyautogui.click(x=70, y=169)
pyperclip.copy("pedro")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
pyautogui.click(x=1360, y=497)
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

#corpo
texto = """
Bom dia!

Aqui esta o relatorio de vendas...

Atenciosamente
Pedro Barros
"""
pyautogui.write(texto)

#anexar arquivo
pyautogui.click(x=1424, y=951)
pyautogui.click(x=255, y=156)
confirmar = PySimpleGUI.popup("Este arquivo está correto?")
time.sleep(3)
if confirmar:
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.click(x=1301, y=954)
else:
    pyautogui.press("esc")








