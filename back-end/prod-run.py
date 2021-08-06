from api import create_app
from dotenv import load_dotenv

load_dotenv('.env-prod') 
app = create_app()

app.run()