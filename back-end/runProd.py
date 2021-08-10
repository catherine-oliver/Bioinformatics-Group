"""
@package Production App Run

Creates and runs a Flask API using the production environment configuration.

Dependencies:
 - Dotenv
"""
from api import create_app
from dotenv import load_dotenv

def runProduction():
    """Loads the requirements from the production environment file (.env-prod)
    and creates a new app using create_app()
    """
    load_dotenv('.env-prod') 
    app = create_app()

    app.run()

if __name__ == "__main__":
    runProduction()