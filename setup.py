from setuptools import setup, find_packages

setup(
    name="term_generator",
    version="0.1",
    description="A term generation web application using Flask and OpenAI",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.1",
        "gunicorn>=20.1.0",
        "openai>=0.8.0",
        "Jinja2>=3.0",
        "gunicorn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
