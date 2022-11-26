import asyncio
from os import system
from time import sleep
from playwright.async_api import async_playwright

class CaptacaoClientes:

    def __init__(self) -> None:
        self.vendedor = ''
        self.contatos = []
        self.opcoes = ['I', 'R', 'S', '1', '2', '3']

    def script(self):
        return f'''Olá, tudo bem!? 🙋🏻‍♂️
Sou o {self.vendedor}, do Atacadão da Tecnologia.

O motivo do meu contato é para informar que toda a loja está com desconto de até 70%.

Temos um grande mix de produtos, headset, fones bluetooth, mouse, teclado, acessórios gamers, cabos, smartwach, caixas de som e monitor com descontos imperdíveis.
Computadores i3 de R$2.399,90 por R$1.399,90...
R$1.000,00 de desconto 👏🏻👏🏻👏🏻

Fazemos entrega para toda Maceió!
Obrigado. 🙏🏻😊'''

    def header(self):
        print(f'_'*50)
        print('')
        print(f'{"ATACADÃO DA TECNOLOGIA - CAPTAÇÃO DE CLIENTES":^50}')
        print(f'_'*50)
        print(f'\nVendedor: {self.vendedor}')
        print(f'Contatos: {len(self.contatos)}')
        print('\n[1] Inserir vendedor')
        print('[2] Inserir contato')
        print('[3] Ver contatos inseridos')
        print('\n[I] Iniciar')
        print('[R] Relatório')
        print('[S] Sair')

    def homepage(self):

        while True:
            system('cls')
            self.header()
            opc = input('\n> ').strip().upper()

            if opc not in self.opcoes:
                print('\nOPÇÃO INVÁLIDA!')
                sleep(1)
            else:

                if opc == '1':

                    print('\nNome do vendedor')
                    nome = input('> ').strip()
                    _nome = nome.split(' ')

                    try:
                        for x in _nome:
                            assert x.isalpha()

                        self.vendedor = nome.title()
                        print('\nNOME INSERIDO.')
                    except:
                        print('\nNOME INVÁLIDO!')

                    sleep(1)

                elif opc == '2':
                    system('cls')
                    self.header()
                    print('\nDigite o numero com DDD (EX: 82912341234)')
                    contato = input('> ').strip()

                    try:
                        assert contato.isdigit()
                        assert len(contato) == 11
                        assert contato not in self.contatos
                        self.contatos.append(contato)
                        print('\nNÚMERO INSERIDO.')
                    except:
                        print('\nNÚMERO INVÁLIDO!')

                    sleep(1)

                elif opc == '3':

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

                elif opc == 'I':

                    try:
                        assert self.vendedor != ''
                        assert len(self.contatos) > 0
                        print('\nINICIANDO...')
                        asyncio.run(self.main())
                        break
                    except:
                        print('\nERRO AO INICIAR!')
                        sleep(1)

                elif opc == 'R':
                    print('\nEM BREVE...')
                    sleep(1)

                elif opc == 'S':
                    print('\nSAINDO..')
                    sleep(1)
                    break

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
            await page.wait_for_selector(page.get_by_text('Para usar o WhatsApp no seu computador:'), timeout=0)
            await browser.close()

if __name__ == '__main__':
    CaptacaoClientes().homepage()
