import pyautogui
import time
import pandas
import pyperclip

#Acesso a pagina

pyautogui.PAUSE = 0.5

pyautogui.click(x=453, y=745)
pyautogui.click(x=389, y=49)
pyautogui.write('https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema')
pyautogui.press('enter')

#Login

pyautogui.click(x=563, y=344)
pyautogui.write('Meu Login')
pyautogui.hotkey('tab')
pyautogui.write('Minha senha')
pyautogui.click(x=742, y=487)

#Download arquivo

time.sleep(2)
pyautogui.click(x=1078, y=256)
time.sleep(5)
pyautogui.hotkey('alt', 'f4')


#Arquivo

pyautogui.PAUSE = 1
tabela = pandas.read_csv('C:/Users/Estudo/Downloads/Compras.csv', sep=';')
print(tabela)

total_Gasto = tabela['ValorFinal'].sum()
quantidade = tabela['Quantidade'].sum()
precoMedio = total_Gasto / quantidade

print(f' Total Gasto {total_Gasto} \n Quantidade {quantidade} \n Preço Medio {precoMedio}')

#E-mail

pyautogui.PAUSE = 1

pyautogui.click(x=453, y=745)
pyautogui.click(x=389, y=49)
pyautogui.write('gmail.com')
pyautogui.press('enter')

time.sleep(0.5)
pyautogui.click(x=994, y=103)

#Login e-mail

pyautogui.PAUSE = 2
pyautogui.click(x=636, y=367)
pyautogui.write('exemplo@gmail.com')
pyautogui.click(x=837, y=558)
pyautogui.write('senha')
pyautogui.press('enter')
time.sleep(5)

#Escrever e-mail

pyautogui.PAUSE = 1.5
pyautogui.click(x=87, y=158)
pyautogui.write('exemplo@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Mensagem Automatizada')
pyautogui.press('tab')

texto = f"""
#Segue o relatório com os dados
#Valor total: {total_Gasto:,.2f}
#Quantidade: {quantidade:,.2f}
#Média de Preço: {precoMedio:,.2f}"""

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)
pyautogui.hotkey('ctrl', 'enter')

pyautogui.PAUSE = 1
pyautogui.click(x=1331, y=102)
pyautogui.click(x=1152, y=391)
pyautogui.hotkey('alt', 'f4')
