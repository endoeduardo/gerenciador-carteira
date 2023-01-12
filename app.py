import PySimpleGUI as sg

FONT = 'Helvetica'
FONT_SIZE = 25

LISTA_DE_ATIVOS = ('AÇÕES', 'FII', 'RENDA FIXA', 'BDR', 'ETF')

menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('Cadastro', size=(30, 1), justification='center', font=(FONT, FONT_SIZE), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Ativo'), sg.InputText('ITS4', size = (7, 1)), sg.InputCombo(LISTA_DE_ATIVOS, size=(20, 1))],

]

def main():

    # Create the window
    window = sg.Window("Gerenciador de Carteiras", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event in ("Close", sg.WIN_CLOSED):
            break
    window.close()


if __name__ == "__main__":
    main()