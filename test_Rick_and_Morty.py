import requests
import pytest


@pytest.mark.apitest
def test_rick_and_morty_params():
    response = requests.get("https://rickandmortyapi.com/api/character", params={"name": "Rick"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    json_data = response.json()
    # print(json_data)
    assert json_data['results'][0]['name'] == 'Rick Sanchez'