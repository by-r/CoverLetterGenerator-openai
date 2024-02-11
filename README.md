# CoverLetterGenerator
This a flask app that utilizes openai APIs to tailor a cover letter for your needs.

## Features
- Create cover letters in just a few seconds
- Tailor the cover letter with specific info
- More to be added

## Technologies
- Flask
- Tailwdindcss UI Library

## Run Locally
1. Clone this repo to your machine

2. Fill in `.env` file based on template   
  ```python
  # Make a .env file or just modify the .env.template file
  # Insert your OpenAI api key here
  API_KEY=
  ```

3. Assuming you have pipenv 
```bash
pipenv shell
```

4. Run the app with 
```bash
python app.py
```
and 
```bash
tailwindcss -i static/src/style.css -o static/css/main.css --watchcss --watch
```

## Future improvements
1. Polish UI
2. Make this an electron app
