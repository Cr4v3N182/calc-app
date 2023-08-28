import PySimpleGUI as sg

label = sg.Text('Enter a nums')
user_num1 = sg.Input(key="num1", size=(10,5), justification="c")
user_num2 = sg.Input(key="num2", size=(10,5), justification="c")
user_symbol = sg.Input(key="symbol", size=(2,2), justification="c")



layout = [[label],
          [user_num1, user_symbol, user_num2]]


window = sg.Window("Calculator", layout=layout,
                   size=(300, 100), element_justification="c")

window.read()
window.close()
