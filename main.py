import asyncio
import msvcrt
from os import system
from time import sleep
from wapp_web import captar_clientes

class CaptacaoClientes:

    def __init__(self) -> None:
        self.vendedor = ''
        self.contatos = []

    def cabecalho(self):
        system('cls')
        print(f'―'*50)
        print(f'{"ATACADÃO DA TECNOLOGIA - CAPTAÇÃO DE CLIENTES":^50}')
        print(f'―'*50)

    def tela_home(self):
        self.cabecalho()
        print(f'Vendedor: {self.vendedor}')
        print(f'Contatos: {len(self.contatos)}')
        print('\n[1] Inserir Vendedor')
        print('[2] Inserir Contatos')
        print('[3] Ver Contatos Inseridos')
        print('[4] Deletar Contatos')
        print('\n[I] Iniciar')
        print('[S] Sair')
        opc = input('\n> ').strip().upper()
        return opc

    def inserir_vendedor(self):
        self.cabecalho()
        print('\nNome do Vendedor:')
        nome = input('> ').strip()
        _nome = nome.split(' ')

        try:
            for x in _nome:
                assert x.isalpha()

            self.vendedor = nome.title()
        except:
            print('\nNOME INVÁLIDO!')
            sleep(1)

    def inserir_contato(self):
        self.cabecalho()
        print('\nNúmero do Cliente: (Ex: 82912345678)')
        numero = input('> ').strip()

        try:
            assert numero.isdigit()
            assert len(numero) == 11
            assert numero not in self.contatos
            self.contatos.append(numero)
        except:
            print('\nNÚMERO INVÁLIDO!')
            sleep(1)

    def ver_contatos(self):

        try:
            assert len(self.contatos) > 0
            self.cabecalho()

            for i, x in enumerate(self.contatos):
                print(f'{i} - {x}')

            print('\nPressione qualquer tecla pra voltar...')
            _ = msvcrt.getch()
        except:
            print('\nLISTA DE CONTATOS VAZIA!')
            sleep(1)

    def deletar_contato(self):
        pass

    def iniciar(self):
        try:
            assert self.vendedor != ''
            assert len(self.contatos) > 0
            print('\nINICIANDO...')
            asyncio.run(captar_clientes(self.vendedor, self.contatos))
            print('\nCAPTAÇÃO CONCLUIDA.')
        except:
            print('\nNÃO FOI POSSÍVEL INICIAR!')
            sleep(1)

    def main(self):

        while True:
            opc = self.tela_home()

            try:
                assert opc in ['1', '2', '3', '4', 'I', 'S']

                if opc == '1':
                    self.inserir_vendedor()
                elif opc == '2':
                    self.inserir_contato()
                elif opc == '3':
                    self.ver_contatos()
                elif opc == '4':
                    pass
                elif opc == 'I':
                    self.iniciar()
                elif opc == 'S':
                    print('\nSAINDO...')
                    sleep(1)
                    break

            except:
                print('\nOPÇÃO INVÁLIDA!')
                sleep(1)

if __name__ == '__main__':
    CaptacaoClientes().main()
