from playwright.async_api import async_playwright

async def get_job_description(url):

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            url,
            wait_until="domcontentloaded"
        )

        # Close any pop-ups or modals that may appear on the page
        await page.keyboard.press("Escape")

        description_selector = (
            ".description__text, "
            ".show-more-less-html__markup, "
            "section.core-section-container"
        )

        try:
            # Wait for the job description element to be visible on the page
            await page.wait_for_selector(
                description_selector,
                timeout=10000
            )
        
        except Exception as e:
            #print(f"Error: {e}")
            await browser.close()
            print("""❌⁴⁰⁴ Error ⁴⁰⁴:
            Job description not found, 
            please check the URL or the page structure.
            """)  
            raise SystemExit()
            
        descricao = await page.locator(
            description_selector
        ).first.inner_text()

        await browser.close()

        return descricao