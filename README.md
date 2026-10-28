# Generative AI Internship — Code Review Prototype

A Streamlit prototype that sends Python code or coding questions to a Gemini model.

## Why this project matters

The example explores a simple AI interface: collect user input, apply a task-specific instruction, request a model response, and display it.

## Source

The implementation is in [AI Code Reviewer/app.py](<AI Code Reviewer/app.py>).

## Current status

The app needs corrections before it can serve as a reliable demo:

- API configuration currently contains an empty key; use environment-based credential loading.
- `st.ballons()` is misspelled.
- The model call is outside the button handler, so it can run before the user submits useful input.
- The hardcoded experimental model identifier needs to be checked for availability.
- Error handling and dependency documentation are not yet provided.

## Development setup

Review those issues before attempting startup. The source imports Streamlit, `google.generativeai`, and IPython.

```bash
git clone https://github.com/Arjun1443/Gen-Ai-Internship.git
cd Gen-Ai-Internship
python -m pip install streamlit google-generativeai ipython
python -m streamlit run "AI Code Reviewer/app.py"
```

The command identifies the entry point; it does not resolve the implementation issues above. Treat model feedback as suggestions requiring code review and testing.
