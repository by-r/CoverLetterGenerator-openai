from flask import Flask, render_template, jsonify, redirect, url_for, request, json
import openai
import textwrap

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        job = request.form.get('job')
        company = request.form.get('company')
        
        # Write a cover letter for Software Engineer Role at Facebook
        prompt = f"Write a cover letter for {job} role at {company}"
        
        response = openai.Completion.create(
            model = 'text-curie-001',
            prompt = prompt,
            max_tokens = 512,
            temperature=0.99,
            frequency_penalty=0.3,
            n=1,
        )
        
        text = format_text(response['choices'][0]['text'])
        
        return render_template("coverletter.html", text = text)
    return render_template("index.html")

def format_text(text):
    # Remove leading and trailing whitespace
    text = text.strip()

    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    # Format each paragraph
    formatted_paragraphs = []
    for paragraph in paragraphs:
        # Wrap the paragraph text to a line width of 80 characters
        wrapped_lines = textwrap.wrap(paragraph, width=80)

        # Add a blank line between each wrapped line
        formatted_paragraph = '\n'.join(wrapped_lines)

        # Add the formatted paragraph to the list
        formatted_paragraphs.append(formatted_paragraph)

    # Join the formatted paragraphs with double line breaks
    formatted_text = '\n\n'.join(formatted_paragraphs)

    return formatted_text

@app.route("/json")
def get_json():
    return jsonify({'name':'bob', "age": 1})

@app.route("/gotohome")
def gotohome():
    return redirect(url_for("home"))

if __name__ == '__main__':
    print("running py app")
    app.run(debug=True)