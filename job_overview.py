from playwright.sync_api import sync_playwright


def get_job_description(url):

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded")

        # Espera o container público carregar
        seletor = ".show-more-less-html__markup, .description__text"
        page.wait_for_selector(seletor, timeout=10000)

        # Extrai o texto completo direto do DOM
        description = page.locator(seletor).first.inner_text()

        browser.close()

    return description