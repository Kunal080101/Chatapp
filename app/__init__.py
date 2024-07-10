from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    # Define the template folder path
    template_folder = os.path.join(app.root_path, 'templates')

    # Debugging information
    print("Template folder path:", template_folder)

    # Check if the directory exists and list its contents
    if os.path.exists(template_folder):
        print("Templates available:", os.listdir(template_folder))
    else:
        print("Template folder does not exist")

    from .routes import main
    app.register_blueprint(main)

    return app
app = create_app()