import os
import sys
from dotenv import load_dotenv
if __name__ == "__main__":
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
```
```python
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
class Command(BaseCommand):
    help = 'Checks the health of the project.'
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting health check...'))
        db_conn = connections['default']
        try:
            c = db_conn.cursor()
        except OperationalError:
            self.stdout.write(self.style.ERROR('Database connection failed.'))
            return
        self.stdout.write(self.style.SUCCESS('Database connection looks good.'))
        self.stdout.write(self.getPath())
        self.stdout.write(self.style.SUCCESS('Health check passed.'))