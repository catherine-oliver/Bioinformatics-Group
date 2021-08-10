"""
@package Test/Dev App Run

Creates and runs a Falsk API using the test/dev environment configuration.

Dependencies:
 - Dotenv
"""
from api import create_app
from dotenv import load_dotenv

def runDevelopment():
    """Loads the requirements from the test environment file (.env-test)
    and creates a new app using create_app().
    """
    load_dotenv('.env.test') 
    app = create_app()

    app.run()

if __name__ == "__main__":
    runDevelopment()