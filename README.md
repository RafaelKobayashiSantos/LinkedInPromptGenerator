# LinkedInPromptGenerator

LinkedIn Prompt Generator is a Python tool that transforms a candidate's resume and a LinkedIn job posting into structured AI prompts.

The project was created to automate part of the job application workflow, allowing users to analyze how well their resume matches a specific position and generate different types of career-related outputs.

Instead of directly connecting to an LLM API, the project generates ready-to-use Markdown prompts that can be submitted to the user's preferred AI platform.

## What It Does

The current workflow is:

1. Upload or provide a resume in PDF format.
2. Extract the resume text automatically.
3. Provide a LinkedIn job posting URL.
4. Extract the job description using Playwright.
5. Select the type of analysis or output to generate.
6. Combine the resume, job description and selected task into a structured prompt.
7. Save the resulting prompt as a Markdown file.


## Technology Stack

## Technology Stack

- 🐍 Python
- 📄 PDF Parsing
- 🎭 Playwright
- 📝 Markdown
- ☁️ Google Colab
- 🐙 Git & GitHub

### Stack Details

- Python 3.x: data processing, parsing, script automation.
- `requirements.txt`: dependency management for any future libraries.
- `src/`: code organization for analyzer modules.
- `data/`: storage for job listings, processed results, and reports.

## Goals

1. Build a reliable job evaluation engine.
2. Provide clear, side-by-side comparisons of job opportunities.
3. Make career decisions more transparent with quantitative support.
4. Allow users to customize scoring criteria.
5. Keep the tool simple and easy to extend.

## Further Improvements

- Add a graphical report generator (charts or dashboards).
- Improve parsing for more job posting formats.
- Add support for company culture and remote work factors.
- Enable weighting of criteria by user preference.
- Provide export options: CSV, JSON, or PDF.

## Privacy & Data Handling

This project is designed to process resumes temporarily within the Google Colab runtime.

**Your resume and generated files are not stored by this project or sent to an external LLM API.**

The notebook uploads the resume to the temporary Colab runtime so it can be processed during the current session. The project does not include a database, persistent storage, or an API that collects uploaded resumes.

Google Colab runs code inside a virtual machine, and Google states that these virtual machines are deleted after periods of inactivity and have a maximum lifetime. Files stored in the runtime are therefore not intended to be used as permanent storage.

> **Important:** If you want to keep your generated prompt or any processed file, download it before ending your Colab session.

For more information, see Google's official [Colab FAQ](https://research.google.com/colaboratory/faq.html).

### Personal Data

Resumes may contain personal and professional information. Only upload documents you are comfortable processing through Google Colab.

This project *does not* require an LLM API key and does not intentionally transmit resume contents to an external AI service.

## Visualization

Current status:

- [x] Job parsing
- [x] Comparison logic
- [x] Scoring engine
- [ ] Graphical output
- [ ] NLP-based analysis
- [ ] Web or notebook UI


## Installation

git clone https://github.com/RafaelKobayashiSantos/LinkedInPromptGenerator.git
cd LinkedInPromptGenerator

### Install the dependencies:

```
- pip install -r requirements.txt
```

Install the Playwright browser:

```
- playwright install chromium
```

## Usage

python main.py

The program will guide the user through the available tasks and generate the corresponding Markdown prompt.

The generated prompt contains:

- Candidate resume
- Job description
- Selected task instructions
- System instructions for the AI

The tool does not send the prompt to an LLM automatically.

## Project Structure

LinkedInPromptGenerator/
│
├── inputs/
│   └── resume.pdf
│
├── outputs/
│   └── generated prompts
│
├── parsers/
│   └── pdf_parser.py
│
├── tasks/
│   ├── career_report.md
│   ├── cover_letter.md
│   ├── gap_analysis.md
│   ├── interview.md
│   └── recruiter.md
│
├── main.py
├── main_colab.ipynb
├── job_overview.py
├── prompt_generator.py
├── task_reader.py
├── requirements.txt
└── README.md

## Google Colab

The project can also be executed through Google Colab. [By clicking right here!](https://colab.research.google.com/drive/1UlaQAyUWqKXhPj3vIglX0ecv7_rC0skq#scrollTo=s8GQ78ZPVpxE)

Open the project in Google Colab

The notebook allows users to:

- Clone the repository.
- Install the required dependencies.
- Upload their resume.
- Provide a LinkedIn job posting.
- Select a task.
- Generate the corresponding Markdown prompt.

#### Why Generate Prompts Instead of Calling an LLM?

The project intentionally separates prompt generation from AI execution.

This makes the tool:

1. Model independent
2. Compatible with different AI platforms
3. Easy to customize
4. Free from API key requirements
5. Easier to inspect and modify

The user remains in control of which AI model receives their resume and job information.

## Design Decisions
Task-based architecture

Each output type is represented by a separate Markdown file.

This allows new workflows to be added without modifying the core Python logic.

For example, adding:

```
tasks/linkedin_about.md
```

automatically makes a new task available to the task selector.

Separation of responsibilities

The project separates:

Resume parsing
Job description extraction
Task selection
Prompt generation

This keeps each component simple and easier to maintain.

## Future Improvements

Possible future improvements include:

- Better PDF structure preservation
- Support for additional job platforms
- Resume formatting analysis
- More career-oriented task templates
- Optional direct LLM integration
   Web interface
- Automated application tracking

## License

This project is intended as a personal portfolio and learning project.