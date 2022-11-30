from playwright.async_api import async_playwright

def script(vendedor):
    return f'''Olá, tudo bem!? 🙋🏻‍♂️
Sou o {vendedor}, do Atacadão da Tecnologia.

O motivo do meu contato é para informar que toda a loja está com desconto de até 70%.

Temos um grande mix de produtos, headset, fones bluetooth, mouse, teclado, acessórios gamers, cabos, smartwach, caixas de som e monitor com descontos imperdíveis.
Computadores i3 de R$2.399,90 por R$1.399,90...
R$1.000,00 de desconto 👏🏻👏🏻👏🏻

Fazemos entrega para toda Maceió!
Obrigado. 🙏🏻😊'''

async def captar_clientes(vendedor, contatos):

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel='chrome', headless=False)
        page = await browser.new_page()

        for contato in contatos:
            await page.goto(f'https://web.whatsapp.com/send/?phone=55{contato}&text&type=phone_number&app_absent=0')

            while True:
                await page.wait_for_load_state('networkidle')

                if await page.get_by_test_id('conversation-compose-box-input').is_visible(timeout=1000):
                    await page.get_by_test_id('conversation-compose-box-input').fill(script(vendedor))
                    await page.get_by_test_id('compose-btn-send').click()
                    await page.get_by_title('Anexar').click()
                    await page.locator('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/div/ul/li[1]/button/input').set_input_files('black.jpg')
                    await page.locator('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div').click()
                    await page.wait_for_load_state('networkidle')
                    break
                elif await page.get_by_text('O número de telefone compartilhado através de url é inválido.').is_visible(timeout=1000):
                    await page.get_by_test_id('popup-controls-ok').click()
                    break

        await page.get_by_title('Mais opções').click()
        await page.get_by_text('Desconectar').click()
        await page.get_by_test_id('popup-controls-ok').click()
        await page.wait_for_load_state('networkidle')
        await browser.close()
