Chatbot Application with CI/CD Pipeline

Table of Contents
1. Project Overview
2. Features
3. Technology Stack
4. Installation
5. Usage
6. CI/CD Pipeline
7. Environment Management
8. Secrets and Tokens Management
9. Testing
10. Deployment

Project Overview

This project is a chatbot application built using Flask. It demonstrates a full CI/CD pipeline setup in GitLab, including automated testing, code quality checks, and deployment to Google Cloud Platform's App Engine. The project focuses on secure and efficient deployment practices, including the use of secrets and tokens, and artifact management.

Features

Chat Functionality: Users can send messages to the chatbot.
CI/CD Pipeline: Automated build, test, and deployment stages using GitLab CI/CD.
Code Quality Checks: Integrated with SonarQube for static code analysis.
Secure Deployment: Management of sensitive data using secrets and tokens.

Technology Stack

Frontend: HTML, CSS (with style.css), JavaScript (with script.js).
Backend: Flask (Python).
CI/CD: GitLab CI/CD.
Deployment: Google App Engine.
Testing: Pytest.
Code Quality: SonarQube.
Containerization: Docker.

Installation

Prerequisites

Python 3.9+
Docker
Google Cloud SDK
GitLab CI/CD account

Setup

Clone the repository:

git clone https://gitlab.com/c08951392grp1/chatapplication.git

Install the dependencies:

pip install -r requirements.txt

Run the application locally:

flask run

Usage

Access the application in your browser at http://localhost:5001.
Interact with the chatbot by entering a username and message.

CI/CD Pipeline

The GitLab CI/CD pipeline is defined in the .gitlab-ci.yml file and includes the following stages:

Build: Builds the Docker image of the application.
Test: Runs unit tests and code quality checks.
SonarQube Analysis: Performs static code analysis using SonarQube.
Deploy: Deploys the application to Google App Engine.

Pipeline Workflow

Code is pushed to the repository.
The pipeline is triggered and runs through the stages.
If all tests pass, the application is deployed to the testing environment, followed by production.

Environment Management
The application is configured to run in different environments:

Development: Local machine using Flask's development server.
Testing: Google App Engine staging environment.
Production: Google App Engine production environment.
Environment-specific settings are managed through environment variables and app.yaml configurations.

Secrets and Tokens Management

Sensitive data such as API keys and credentials are managed using GitLab CI/CD's secret and token management features.

Testing

Automated tests are written using Pytest and are executed during the CI/CD pipeline. The test suite is defined in the tests/test_app.py file and includes:
Unit tests for application routes.
Integration tests for the entire application flow.

Deployment

The application is deployed to Google App Engine using the app.yaml configuration file. The deployment process is automated in the CI/CD pipeline, ensuring a seamless and consistent deployment experience.