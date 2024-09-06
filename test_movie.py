#pytest -s -m test_auth
import pytest
import requests

ENDPOINT = "https://api.themoviedb.org/3/movie/popular"
movie_key="d78cfb8acb70922ed2c45fc903e9bcea"
languaje="es-MX"

ENDP2 = "https://api.themoviedb.org/3/authentication"
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkNzhjZmI4YWNiNzA5MjJlZDJjNDVmYzkwM2U5YmNlYSIsInN1YiI6IjY0MTg4MTMxYTE0YmVmMDA3YzZiZWQ5NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.HhQbHZqCBndiHhPDFUGc7QP4Q00TowRUZrLO3ui1x14',
    'accept': 'application/json'
}

ENDP3 = "https://api.themoviedb.org/3/account/18442630/favorite"

@pytest.mark.test_auth
def test_auth():
    print('---------------------------------test_movie---------------------------------------------')
    response = get_auth()
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    json_response = response.json()
    assert 'success' in json_response and json_response['success'] == True, "Authentication failed"
    print('----------------------response_auth',json_response)

@pytest.mark.test2_auth
def test_can_call_movie():
    response = get_movie()
    assert response.status_code == 200
    response_data = response.json()
    print("----response_data",response_data)






def get_movie():
    print('----liga movie ',ENDPOINT + f"?api_key={movie_key}&language={languaje}")
    return requests.get(ENDPOINT + f"?api_key={movie_key}&language={languaje}")
    

def get_auth():
    return requests.get(ENDP2, headers=headers)
    




