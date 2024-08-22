# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locc.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

from django.core.cache import cache

def some_expensive_operation(arg1, arg2):
    # Generate a unique key for this specific set of arguments
    cache_key = f'unique-prefix-{arg1}-{arg2}'
    # Try to retrieve the cached result
    result = cache.get(cache_key)
    if result is None:
        # If not found in the cache, perform the operation
        result = expensive_operation(arg1, arg2)
        # Store the result in the cache for next time
        cache.set(cache_key, result, timeout=300)  # cache for 5 minutes
    return result