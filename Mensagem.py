import PySimpleGUI as sg

sg.theme('DarkPurple')

layout = [
    [sg.Text ('Nome'), sg.Input (key='nome', size=(25,2))],
    [sg.Text ('Mensagem'), sg.Input (key='mensagem', size=(25,2))],
    [sg.Button('Enviar')],
]

janela = sg.Window('Escreva uma mensagem.', layout = layout)


while True:
    evento, valores = janela.read()

    if evento == 'Enviar':
        nome = valores ['nome']
        mensagem = valores ['mensagem']
       
       

    if evento == sg.WIN_CLOSED: 
        break

janela.close()

