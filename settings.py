from pathlib import Path

with open('name') as f:
    NAME = f.read().strip()

BASE_DIR = Path.cwd()
SYSTEMD_DIR = BASE_DIR / 'systemd'

with open('token') as f:
    TOKEN = f.read().strip()
HEADERS = {'Authorization': f'Bearer {TOKEN}'}

PROJECTS = {
    'django': {
        'owner': 'django',
        'repo': 'django',
    },
    'fastapi': {
        'owner': 'tiangolo',
        'repo': 'fastapi',
    },
    'flask': {
        'owner': 'pallets',
        'repo': 'flask',
    },
    'litestar': {
        'owner': 'litestar-org',
        'repo': 'litestar',
    },
    'blacksheep': {
        'owner': 'Neoteroi',
        'repo': 'BlackSheep',
    },
    'starlette': {
        'owner': 'encode',
        'repo': 'starlette',
    },
    'django-rest-framework': {
        'owner': 'encode',
        'repo': 'django-rest-framework',
    },
    'channels': {
        'owner': 'django',
        'repo': 'channels',
    },
}

# github
GITHUB_API = 'https://api.github.com'
SEARCH_ENDPOINT = '/search/issues'
SEARCH_URL = GITHUB_API + SEARCH_ENDPOINT
