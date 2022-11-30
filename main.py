import asyncio
import msvcrt
from os import system
from time import sleep
<<<<<<< HEAD
from playwright.async_api import async_playwright, expect
=======
from wapp_web import captar_clientes
>>>>>>> eeec5cbe6260f67f5ca2c9efd1bb44716541e172

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

<<<<<<< HEAD
                    while True:

                        if len(self.contatos) <= 0:
                            print('\nNENHUM CONTATO INSERIDO!')
                            sleep(1)
                            break

                        else:
                            system('cls')
                            print('CONTATOS INSERIDOS:\n')

                            for i, contato in enumerate(self.contatos):
                                print(f'{i} - {contato}')

                            print('\n[D] Deletar contato')
                            print('[L] Limpar contatos')
                            print('[V] Voltar')
                            opc = input('> ').strip().upper()

                            if opc not in ['D', 'L', 'V']:
                                print('\nOPÇÃO INVÁLIDA!')
                                sleep(1)
                            else:

                                if opc == 'D':
                                    print('\nDigite o índice do contato')

                                    try:
                                        ind = int(input('> '))
                                        assert ind <= len(self.contatos)
                                        self.contatos.pop(ind)
                                        print('\nCONTATO DELETADO.')
                                    except:
                                        print('\nCONTATO NÃO ENCONTRADO!')

                                    sleep(1)
                                elif opc == 'L':

                                    try:
                                        self.contatos.clear()
                                        print('\nLISTA DE CONTATOS LIMPA.')
                                        sleep(1)
                                        break
                                    except:
                                        print('\nERRO AO LIMPAR CONTATOS!')
                                        sleep(1)

                                elif opc == 'V':
                                    break
=======
                elif opc == '4':
                    pass

>>>>>>> eeec5cbe6260f67f5ca2c9efd1bb44716541e172
                elif opc == 'I':

                    try:
                        assert self.vendedor != ''
                        assert len(self.contatos) > 0
                        print('\nINICIANDO...')
                        asyncio.run(captar_clientes(self.vendedor, self.contatos))
                        print('\nCAPTAÇÃO CONCLUIDA.')
                    except:
                        print('\nNÃO FOI POSSÍVEL INICIAR!')
                        sleep(1)
<<<<<<< HEAD
                elif opc == 'R':
                    print('\nEM BREVE...')
                    sleep(1)
=======

>>>>>>> eeec5cbe6260f67f5ca2c9efd1bb44716541e172
                elif opc == 'S':
                    print('\nSAINDO...')
                    sleep(1)
                    break
<<<<<<< HEAD

    async def main(self):

        async with async_playwright() as pw:
            browser = await pw.chromium.launch(channel='chrome', headless=False)
            page = await browser.new_page()

            for cliente in self.contatos:
                await page.goto(f'https://web.whatsapp.com/send/?phone=55{cliente}&text&type=phone_number&app_absent=0')

                while True:

                    if await page.get_by_test_id('conversation-compose-box-input').is_visible(timeout=1000):
                        await page.get_by_test_id('conversation-compose-box-input').fill(self.script())
                        await page.get_by_test_id('compose-btn-send').click()
                        await page.get_by_title('Anexar').click()
                        await page.locator('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').set_input_files('black.jpg')
                        await page.get_by_test_id('send').click()
                        sleep(2)
                        break
                    elif await page.get_by_text('O número de telefone compartilhado através de url é inválido.').is_visible(timeout=1000):
                        await page.get_by_test_id('popup-controls-ok').click()
                        break

            await page.get_by_test_id('menu-bar-menu').click()
            await page.get_by_test_id('mi-logout menu-item').click()
            await page.get_by_test_id('popup-controls-ok').click()
            await expect(page.get_by_text('Para usar o WhatsApp no seu computador:')).to_be_visible(timeout=0)
            await browser.close()
=======
            except:
                print('\nOPÇÃO INVÁLIDA!')
                sleep(1)
>>>>>>> eeec5cbe6260f67f5ca2c9efd1bb44716541e172

if __name__ == '__main__':
    CaptacaoClientes().iniciar()
