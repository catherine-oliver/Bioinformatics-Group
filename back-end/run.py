from api import create_app
from dotenv import load_dotenv

load_dotenv('.env-test') 
app = create_app()

app.run()
