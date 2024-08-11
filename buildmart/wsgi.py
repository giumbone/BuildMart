import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

project_directory = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(project_directory, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

application = get_wsgi_application()