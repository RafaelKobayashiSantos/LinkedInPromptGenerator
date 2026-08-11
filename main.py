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
        "https://www.linkedin.com/jobs/view/4446256327/"
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