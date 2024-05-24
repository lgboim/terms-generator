from flask import Flask, render_template, request, redirect, url_for, session
import os
import re
from openai import OpenAI

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Updated generate_term_explanation and generate_related_terms functions
def generate_term_explanation(term, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"Provide a detailed explanation of the term '{term}'."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
        n=1,
        temperature=0.7,
    )
    explanation = response.choices[0].message.content
    explanation = explanation.replace('\n', '<br>')
    return explanation

def generate_related_terms(term, api_key):
    client = OpenAI(api_key=api_key)
    prompt = f"List 5 terms closely related to '{term}', separated by commas."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=50,
        n=1,
        temperature=0.7,
    )
    related_terms = response.choices[0].message.content
    related_terms = re.split(r'\d+\.\s*|\s*,\s*|\s+and\s+', related_terms)
    return [t.strip() for t in related_terms if t.strip()]

# Function to save term details to a file
def save_term(term, explanation, related_terms):
    term_path = os.path.join(app.root_path, 'pages', f'{term}.txt')
    with open(term_path, 'w') as file:
        file.write(f"{explanation}\n\nRelated Terms:\n" + ', '.join(related_terms))

# Function to retrieve term details from a file
def get_term(term):
    term_path = os.path.join(app.root_path, 'pages', f'{term}.txt')
    if os.path.exists(term_path):
        with open(term_path, 'r') as file:
            content = file.read().split('\n\nRelated Terms:\n')
            return {
                'term': term,
                'explanation': content[0],
                'related_terms': content[1].split(', ')
            }
    return None

@app.route('/set_api_key', methods=['GET', 'POST'])
def set_api_key():
    if request.method == 'POST':
        api_key = request.form['api_key']
        session['api_key'] = api_key
        return redirect(url_for('home'))
    return render_template('set_api_key.html')

@app.route('/term/<term>')
def term_page(term):
    api_key = session.get('api_key')
    if not api_key:
        return redirect(url_for('set_api_key'))
    
    term_data = get_term(term)
    if not term_data:
        explanation = generate_term_explanation(term, api_key)
        related_terms = generate_related_terms(term, api_key)
        save_term(term, explanation, related_terms)
        term_data = get_term(term)
    return render_template('term_page.html', term=term_data['term'], explanation=term_data['explanation'], related_terms=term_data['related_terms'])

@app.route('/')
def home():
    initial_term = "Artificial Intelligence"
    return redirect(url_for('term_page', term=initial_term))


# Search functionality
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        return redirect(url_for('term_page', term=search_term))
    return render_template('search.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
