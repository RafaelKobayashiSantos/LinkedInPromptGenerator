from playwright.async_api import async_playwright
import re

async def get_job_description(url):

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        # Validate the URL format and extract the job ID if it's a search results URL
        if "/jobs/search-results/?currentJobId" in url:
    
            job_id = re.search(r"currentJobId=(\d+)", url)
            job_url = f"https://www.linkedin.com/jobs/view/{job_id.group(1)}/"

        page = await browser.new_page()

        await page.goto(
            job_url if 'job_url' in locals() else url, #In case the job_url variable is defined, use it; otherwise, use the original URL
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