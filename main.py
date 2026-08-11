from parsers.pdf_parser import ResumeParser
from prompt_generator import PromptGenerator
from job_overview import get_job_description
from task_reader import get_task_name as task_reader
import asyncio


# ===========================
# CURRÍCULO
# ===========================

resume = ResumeParser("inputs/resume.pdf").extract_text()

# ===========================
# VAGA
# ===========================

job = asyncio.run(
    get_job_description(
        "https://www.linkedin.com/jobs/search-results/?currentJobId=4451553060&eBP=CwEAAAGf8WHPPDOihyiuJGgQN1BZrN7KR76PaW618djjvsE-2QkfYNq8bReNjoHXjFemWK_QOBeHGgtroGadpQoLCvO4IEJOl8E3VzRqywzNBNyt9jw8d-qWr160TC1kBeKfV1kNWIcwo7n7jtPpoqVGuZs58J8y7VZPFi2TuK3POfXC2s94dgRs4aTqkJeJB7fhdOEaJf8TS3WRQiQ2_8E27DkTAS1GKdMMANSoR5-1x53PjTyD3fqSrL5ER923Hi2baxqzYweM7u3Q80e8CSAZcYBE6DNABkks89u637wRzhj91-KBzRegr0GgokllnSOS8rg_buPArpi_619AQXrsSO49oXDhgjeP_vWkpjJL1227Va_5OyF5BGWLEs8csAX0JapGW3RqygBfvKR3vYtSbd8G4sEo0FoLQePtLzPiJOGrx2QLs9ojep1pFwCIcOT-ikjF5VQOyoXafjSmX-wbaeL5_GwSEiulWO7W&refId=eTAaliH35KDNWyEHwxbkzQ%3D%3D&trackingId=SKQE9XDR9VjxX9BJ3FZgEA%3D%3D&keywords=Ciência%20de%20dados%20or%20Analista%20de%20dados%20or%20Engenheiro%20de%20dados%20or%20Assistente%20de%20dados%20or%20Gestão%20de%20dados%2C%20on-site%20or%20hybrid%20or%20remote&origin=PREFERENCES_LANDING&geoId=90009574%2C91000007%2C101355337%2C102601179%2C103644278%2C104447881%2C105149562%2C105871508"
    )
)

# ===========================
# Task selection
# ===========================

TASK = task_reader()  # Name of the task file (without extension) in tasks/

if TASK is None:
    exit()

with open(f"tasks/{TASK}.md", encoding="utf8") as f:
    task = f.read()

# ===========================
# Generate the prompt and save it to a file
# ===========================

generator = PromptGenerator(resume, job)

generator.save(
    task=task,
    output_path=f"outputs/{TASK}.md"
)

print(f"Prompt '{TASK}' gerado com sucesso!")