from parsers.pdf_parser import ResumeParser
from prompt_generator import PromptGenerator
from job_overview import get_job_description

# ===========================
# CONFIGURAÇÃO
# ===========================

TASK = "cover_letter"  # Nome do arquivo de tarefa (sem extensão) em tasks/

# ===========================
# CURRÍCULO
# ===========================

resume = ResumeParser("inputs/resume.pdf").extract_text()

# ===========================
# VAGA
# ===========================

job = get_job_description("https://www.linkedin.com/jobs/view/4442311004/")

# ===========================
# TAREFA
# ===========================

with open(f"tasks/{TASK}.md", encoding="utf8") as f:
    task = f.read()

# ===========================
# GERA O PROMPT
# ===========================

generator = PromptGenerator(resume, job)

generator.save(
    task=task,
    output_path=f"outputs/{TASK}.md"
)

print(f"Prompt '{TASK}' gerado com sucesso!")