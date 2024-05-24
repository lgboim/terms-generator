from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import re
from openai import OpenAI

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'fallback_secret_key')  # Use environment variable for secrets

# Correcting the DATABASE_URL for PostgreSQL compatibility
uri = os.getenv('DATABASE_URL')
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri or 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Term(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    term = db.Column(db.String(120), unique=True, nullable=False)
    explanation = db.Column(db.Text, nullable=False)
    related_terms = db.Column(db.Text, nullable=False)

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

def save_term(term, explanation, related_terms):
    new_term = Term(term=term, explanation=explanation, related_terms=', '.join(related_terms))
    db.session.add(new_term)
    db.session.commit()

def get_term(term):
    term_record = Term.query.filter_by(term=term).first()
    if term_record:
        return {
            'term': term_record.term,
            'explanation': term_record.explanation,
            'related_terms': term_record.related_terms.split(', ')
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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['search_term']
        return redirect(url_for('term_page', term=search_term))
    return render_template('search.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
