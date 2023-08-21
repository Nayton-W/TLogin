import PySimpleGUI as sg

layout = [

    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='msg')],
]

window = sg.Window('Login', layout= layout)

while(True):
    event,values = window.read()
   
    if event ==sg.WIN_CLOSED:
        break
    elif event== 'login':
        
        pswC='admin'
        userC='admin'
        
        user= values['usuario']
        psw = values['senha']
        
        if psw == pswC and user == userC:
            window['msg'].update('Login efetuado com sucesso!')
        else:
             window['msg'].update('ERROR , senha ou usuario incorretos!')