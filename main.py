import PySimpleGUI as sg

sg.theme("DarkBlue15")
def clear_inputs():
    window["num1"].update("")
    window["num2"].update("")
    window["symbol"].update("")
    window["result"].update("")

label = sg.Text('Enter Numbers')
user_num1 = sg.Input(key="num1", size=(10,5), justification="c")
user_num2 = sg.Input(key="num2", size=(10,5), justification="c")
user_symbol = sg.Input(key="symbol", size=(2,2), justification="c")
output = sg.Text("", key="result")
clear_button = sg.Button("Clear", key="clear")
calc_button = sg.Button("Calculate",key="calc")
exit_button = sg.Button("Exit", key="exit")



layout = [[label],
          [user_num1, user_symbol, user_num2, output],
          [clear_button, calc_button, exit_button]]


window = sg.Window("Calculator", layout=layout,
                   size=(300, 100))

while True:
    event, values = window.read()
    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break
        case "clear":
            clear_inputs()
    try:
        num1 = float(values["num1"])
        num2 = float(values["num2"])
        sym = values["symbol"]
        if (sym == "+"):
            result = num1 + num2
        elif (sym == "-"):
            result = num1 - num2
        elif (sym == "*"):
            result = num1 * num2
        elif (sym == "/"):
            result = num1 / num2
        window["result"].update(result)
    except ValueError:
        sg.popup("Enter numbers only!", font=("Helvetica", 10))



window.close()
