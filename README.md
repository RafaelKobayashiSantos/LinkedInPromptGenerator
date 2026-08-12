# LinkedInPromptGenerator

LinkedInPromptGenerator is a prompt file generator that creates structured AI prompts from job listing data. It helps users prepare prompt content for their preferred AI platform to analyze job details, compare opportunities, and make data-driven career decisions. The project is already capable of parsing job details, scoring opportunities, and generating structured comparisons.

## Progress So Far

- Core parsing engine implemented in `main.py`.
- Job posting data ingestion and normalization completed.
- Basic comparison logic for salary, benefits, and role fit added.
- Local data storage with `data/` folder for input and output.
- Initial scoring system for evaluating job offers.
- Documentation and repository structure established.

## Technology Stack

- 🐍 Python – main language for data parsing and analysis.
- 📄 Markdown – documentation and README.
- 📁 Local file system – input/output data handling.
- 🧠 Custom logic – scoring and comparison rules.

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

## Future Implementations

- 🔍 Natural language processing for job description analysis.
- 📊 Visual charts for salary trends and offer comparisons.
- 🌐 Web interface or notebook integration for interactive use.
- ⚙️ Automated LinkedIn job scraping pipeline.
- 📈 Advanced scoring with career growth and total compensation.

## Visualization

Current status:

- [x] Job parsing
- [x] Comparison logic
- [x] Scoring engine
- [ ] Graphical output
- [ ] NLP-based analysis
- [ ] Web or notebook UI

Simple progress chart:

```
Progress: [#####-----] 50%
Features implemented: 4 / 8
```

## Usage

1. Open the repository in your code editor.
2. Place job listings or example data in `data/`.
3. Run:

   ```bash
   python main.py
   ```

4. Check the generated prompt files and review the output.

## Google Colab

The project is also available as a running notebook on Google Colab:

https://colab.research.google.com/drive/1UlaQAyUWqKXhPj3vIglX0ecv7_rC0skq#scrollTo=RLkJkxuVDZ3s

Step-by-step guide:

1. Open the Colab link in your browser.
2. If needed, sign in with your Google account.
3. Click `Open in Playground` or `Copy to Drive` to create your own editable notebook.
4. Review the notebook cells to see how the repository is loaded and executed.
5. Run the cells in order using the play button or `Runtime > Run all`.
6. Upload or link your job listing data if prompted by the notebook.
7. View the generated file and export any results from the notebook, the file will be downloaded once the process is finished.

## Project Structure

- `README.md` - Current project documentation
- `main.py` - Main analyzer script
- `requirements.txt` - Dependencies list
- `data/` - Job listings, input, and output storage
- `src/` - Analyzer implementation modules