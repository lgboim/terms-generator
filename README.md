# Terms Generator

A Flask web application that generates detailed explanations and related terms for a given term using OpenAI's GPT-3.5 model.

## Features

- Generate detailed explanations for terms.
- Generate related terms for a given term.
- Save term details to a file.
- Retrieve term details from a file.
- Search functionality to find terms.

## Requirements

- Python 3.7+
- Flask
- Gunicorn
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

1. Set your OpenAI API key:
    - Run the application and navigate to `/set_api_key` to enter your API key.
    - Alternatively, set the API key directly in the session in the code.

2. Update the secret key in the `main.py` file:
    ```python
    app.secret_key = 'your_secret_key'
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
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Heroku](https://www.heroku.com/) for deployment.

