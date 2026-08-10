from pathlib import Path
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

class PromptGenerator:

    def __init__(self, resume: str, job_description: str):
        self.resume = resume
        self.job = job_description

    def build(self, task: str) -> str:

        return f"""# SYSTEM


# CANDIDATE RESUME

{self.resume}

---

# JOB DESCRIPTION

{self.job}

---

{task}

Prompt generated on {timestamp}.

"""

    def save(self, task: str, output_path="outputs/prompt.md"):

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf8") as f:
            f.write(self.build(task))