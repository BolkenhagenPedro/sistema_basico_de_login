from sys import exit
from getpass import getpass

def ler_senha(msg='Digite a senha: '):
    senha = getpass(msg)
    while len(senha) < 8:
        print('Digite um senha com 8 ou mais caracteres.')
        senha = getpass(msg)
    return senha


def ler_usuario(msg='Digite um nome de um novo usuário: '):
    usuario = input(msg).strip()
    with open('./app/usuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            while line[:ind] == usuario:
                print('Digite um nome de usuário que não está em uso.')
                usuario = input(msg)
        return usuario

def leiaopc(msg=''):
    while True:
        try:
            n = int(input(msg))
            if n == 1 or n == 2:
                return n
            else:
                while n not in [1,2]:
                    print('Digite uma opção válida.')
                    n = int(input(msg))
        except:
            print('Digite uma opção válida.')

def criar_arquivo():
    with open('./app/usuarios.txt', 'a'):
        pass

def cadastrar_novo_usuario():
    from os import linesep
    usuario = ler_usuario()
    senha = ler_senha()
    with open('./app/usuarios.txt', 'a', newline='') as file:
        file.write(f'{usuario},{senha}' + linesep)
    print('Usuário cadastrado com sucesso.')
    exit()

def login():
    usuario = input('Digite o nome de usuário: ').strip()
    senha = getpass('Senha: ')

    with open('./app/usuarios.txt', 'r') as file:
        for line in file:
            ind = line.index(',')
            if line[:ind] != usuario:
                if line[ind+1::].strip() == senha:
                    print('Login efetuado com sucesso.')
                    return True
                else:
                    print('Senha incorreta!')
                    return False
        print(f'Não foi encontrado um usuário {usuario}.')
        return False

criar_arquivo()

print("""Escolha alguma das opções a baixo:
    [1] - Login
    [2] - Cadastrar um novo usuário""")
opc = leiaopc('Sua opção: ')
if opc == 2:
    cadastrar_novo_usuario()
login()
