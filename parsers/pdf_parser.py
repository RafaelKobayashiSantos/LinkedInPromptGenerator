from pathlib import Path
import pdfplumber
import re

class ResumeParser:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def extract_text(self) -> str:

        pages = []

        with pdfplumber.open(self.pdf_path) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:
                    pages.append(text)

        text = "\n\n".join(pages)

        return self.clean(text)

    @staticmethod
    def clean(text: str) -> str:

        # remove espaços duplicados
        text = re.sub(r"[ \t]+", " ", text)

        # remove muitas linhas vazias
        text = re.sub(r"\n{3,}", "\n\n", text)

        # remove caracteres invisíveis
        text = text.replace("\x00", "")

        return text.strip()