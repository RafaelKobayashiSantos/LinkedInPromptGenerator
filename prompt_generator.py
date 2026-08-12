from pathlib import Path
from datetime import datetime
import textwrap

# ==================================================
# Module responsible for generating the prompt 
# based on the resume, job description, and task.
# =================================================

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

class PromptGenerator:

    # Initialize the PromptGenerator with the candidate's resume and job description.
    
    def __init__(self, resume: str, job_description: str):
        self.resume = resume
        self.job = job_description

    # Build the prompt by combining the resume, job description, and task into a structured format.
    def build(self, task: str) -> str:

        return f"""# SYSTEM


# CANDIDATE RESUME

{self.resume}

---

# JOB DESCRIPTION

{self.job}

---

# CURRENT TASK

{task}

Prompt generated on {timestamp}.

"""
    
    # Save the generated prompt to a specified output file path, creating any necessary directories.
    def save(self, task: str, output_path="outputs/prompt.md"):

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf8") as f:
            f.write(self.build(task))