# Terms Generator

A Flask web application that generates detailed explanations and related terms for a given term using OpenAI's GPT-3.5 model.

## Why This App?

The Terms Generator app was created to provide users with a convenient way to generate detailed explanations and related terms for any given term. Whether you are a student, a professional, or simply someone looking to expand your knowledge, this app can help you quickly understand complex terms and discover related concepts. By leveraging OpenAI's powerful GPT-3.5 model, the app ensures high-quality and informative content.

## Goals

- **Educational Resource:** Provide users with detailed explanations of various terms to enhance their learning experience.
- **Knowledge Expansion:** Help users discover related terms and concepts, broadening their understanding of different subjects.
- **Convenience:** Offer a user-friendly platform where users can easily search for terms and get instant, accurate information.
- **Integration with OpenAI:** Demonstrate the practical use of OpenAI's GPT-3.5 model in generating high-quality content.

## Features

- Generate detailed explanations for terms.
- Generate related terms for a given term.
- Save term details to a database.
- Retrieve term details from the database.
- Search functionality to find terms.
- User management of OpenAI API keys through session.

## Requirements

- Python 3.7+
- Flask
- SQLAlchemy
- Flask-Migrate
- OpenAI API Key

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/lgboim/terms-generator.git
    cd terms-generator
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Set your OpenAI API key by navigating to `/set_api_key` in the application, or directly store it in the session within the code.

2. Set the application's secret key:
    ```python
    app.secret_key = 'your_secret_key_here'
    ```

## Running the Application

1. Run the Flask application locally:
    ```sh
    python main.py
    ```

2. The application will be available at `http://127.0.0.1:5000`.

## Deploying to Heroku

1. Create a `Procfile` in the root directory with the following content:
    ```Procfile
    web: gunicorn main:app
    ```

2. Make sure `gunicorn` is listed in your `requirements.txt`:
    ```sh
    pip install gunicorn
    pip freeze > requirements.txt
    ```

3. Initialize a git repository, commit your code, and push to Heroku:
    ```sh
    git init
    heroku create
    git add .
    git commit -m "Initial commit"
    git push heroku main
    ```

4. Scale the web dyno:
    ```sh
    heroku ps:scale web=1 --app your-app-name
    ```

5. Open your application:
    ```sh
    heroku open --app your-app-name
    ```

## Usage

1. Set your OpenAI API key by navigating to `/set_api_key`.
2. To generate term details, navigate to `/term/<term>` where `<term>` is the term you want to search.
3. Use the search functionality to find terms by navigating to `/search`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT-3.5 model.
- [Flask](https://flask.palletsprojects.com/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) for the web framework and database migrations.
- [Heroku](https://www.heroku.com/) for deployment.
