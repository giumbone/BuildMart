# In your_app/views.py
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_500(request):
    return render(request, '500.html', {}, status=500)

# In your_project_name/urls.py
from django.conf.urls import handler404, handler500
from your_app.views import custom_404, custom_500

handler404 = 'your_app.views.custom_404'
handler500 = 'your_app.views.custom_500'
```
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'logs/django_errors.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}