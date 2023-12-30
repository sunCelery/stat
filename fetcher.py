import requests

import settings


class GithubStatisticFetcher:
    def __init__(self, owner: str, repo: str):
        self.open_pulls_number_params = {
            'q': f'type:pr state:open repo:{owner}/{repo}',
            'per_page': 1,
        }
        self.closed_pulls_number_params = {
            'q': f'type:pr state:closed repo:{owner}/{repo}',
            'per_page': 1,
        }
        self.open_issues_number_params = {
            'q': f'type:issue state:open repo:{owner}/{repo}',
            'per_page': 1,
        }
        self.closed_issues_number_params = {
            'q': f'type:issue state:closed repo:{owner}/{repo}',
            'per_page': 1,
        }

    def request(self, params: dict) -> requests.Response:
        return requests.get(
            settings.SEARCH_URL,
            headers=settings.HEADERS,
            params=params,
        )
