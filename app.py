import PySimpleGUI as sg

FONT = 'Helvetica'
FONT_SIZE = 15

LISTA_DE_ATIVOS = ('AÇÕES', 'FII', 'RENDA FIXA', 'BDR', 'ETF')

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]


column_text = [[sg.Text('Cadastro', size=(30, 1), justification='center', font=(FONT, FONT_SIZE), relief=sg.RELIEF_RIDGE)]]
column1 = [[sg.Text('Ativo'), sg.InputText('ITS4', size = (7, 1)), sg.InputCombo(LISTA_DE_ATIVOS, size=(20, 1))]]
column2 = [[
    sg.Text('dia'), sg.Spin(values=(list(range(1, 31))), initial_value=1),
    sg.Text('mes'), sg.Spin(values=(list(range(1, 12))), initial_value=1),
    sg.Text('ano'), sg.Spin(values=(list(range(2022, 2030))), initial_value=2022)
]]

column_end = [[sg.Button('Cadastrar'), sg.Button('Fechar')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Column(column_text, justification='center')],
    [sg.Column(column1), sg.Column(column2)],
    [sg.Column(column_end, justification='center')]
]

def main():

    # Create the window
    window = sg.Window("Gerenciador de Carteiras", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event in ("Fechar", sg.WIN_CLOSED):
            break
    window.close()


if __name__ == "__main__":
    main()