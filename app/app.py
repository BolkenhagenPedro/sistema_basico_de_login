from os import linesep
from getpass import getpass

def criar_arquivo():
    with open('./app/usuarios.txt', 'a'):
        pass

def cadastrar(usuario, senha):
    with open('usuarios.txt', 'a', newline='') as file:
        file.write(f'{usuario},{senha}' + linesep)

def verificar_usuario(usuario):
    with open('usuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            if usuario == line[:ind]: return False
            return True
        
def verificar_senha(usuario, senha):
    with open('usuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            if usuario == line[:ind]:
                if senha == (line[ind+1:]).strip():
                    return True
                else:
                    print('Senha incorreta!')
                    return False


criar_arquivo()

print("""Opções:
[1] - Fazer Login
[2] - Cadastrar novo usuário""")

opc = int(input('Informe uma das opções a cima: '))
print('=' * 31)
while opc not in [1, 2]:
    print('Informe uma opção correta!')
    opc = int(input('Informe uma das opções a cima: '))
    
if opc == 1:
    usuario = input('Informe o nome do usuário: ').strip()
    senha = getpass('Informe a senha: ')
    if verificar_usuario(usuario):
        while verificar_usuario(usuario):
            print('Nome de usuário incorreto!')
            usuario = input('Informe o nome do usuário: ').strip()

    if verificar_senha(usuario, senha):
        print('Entrou com sucesso!')
    else:
        print('Não foi possível entrar, verifica suas informações de login.')
else:
    usuario = input('Digite um nome para um novo usuário: ').strip()
    if verificar_usuario(usuario):
        while verificar_usuario(usuario) == False:
            print('Esse nome de usuário já existe! Digite um nome inovador.')
            usuario = input('Digite um nome para um novo usuário: ').strip()
            
    senha = getpass('Digite uma senha: ')
    while len(senha) < 8:
        print('Escreva uma senha com 8 ou mais caracteres!')
        senha = getpass('Digite uma senha: ')

    cadastrar(usuario,senha)

    print('Usuário cadastrado com sucesso!')
