from playwright.async_api import async_playwright
import re

# =========================================
# Module responsible for scraping job 
# descriptions from LinkedIn job postings.
# =========================================

# Asynchronously fetch the job description 
# from a LinkedIn job posting URL. If the URL 
# is a search results page, extract the job ID 
# and navigate to the specific job posting.

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

        # Handle the case where the job description is not found within the timeout period
        except Exception as e:
            await browser.close()
            print("""❌⁴⁰⁴ Error ⁴⁰⁴:
            Job description not found, 
            please check the URL or the page structure.
            """)  
            raise SystemExit()

        # Extract the job description text from the 
        # page using the specified selector           
        description = await page.locator(
            description_selector
        ).first.inner_text()

        await browser.close()

        return description