with open('token') as f:
    TOKEN = f.read().strip()

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
}

HEADERS = {'Authorization': f'Bearer {TOKEN}'}


API_URL = 'https://api.github.com'
SEARCH_ENDPOINT = '/search/issues'
SEARCH_URL = API_URL + SEARCH_ENDPOINT
