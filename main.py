import PySimpleGUI as sg

label = sg.Text('Enter Numbers')
user_num1 = sg.Input(key="num1", size=(10,5), justification="c")
user_num2 = sg.Input(key="num2", size=(10,5), justification="c")
user_symbol = sg.Input(key="symbol", size=(2,2), justification="c")
output = sg.Text("", key="result")
calc_button = sg.Button("Calculate",key="calc")
exit_button = sg.Button("Exit", key="exit")



layout = [[label],
          [user_num1, user_symbol, user_num2, output],
          [calc_button]]


window = sg.Window("Calculator", layout=layout,
                   size=(300, 100))

while True:
    event, values = window.read()
    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break




window.close()
