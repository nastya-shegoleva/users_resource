import requests

print(requests.post('http://localhost:5000/api/v2/users', json={}).json())
# пустой запрос

print(requests.post('http://localhost:5000/api/v2/users/3', json={'surname': 33}).json())
# число вместо строки

print(requests.post('http://localhost:5000/api/v2/users/2', json={'age': 20}).json())
# передали только возраст

print(requests.post('http://localhost:5000/api/v2/users',
                    json={'surname': 'Scott', 'name': 'John', 'age': 23, 'position': 'начальник',
                          'speciality': 'инженер', 'address': 'г. Москва', 'email': 'johnscott@gmail.com',
                          'modified_date': 12}).json())
# верный запрос

print(requests.delete('http://localhost:5000/api/v2/users').json())
print(requests.delete('http://localhost:5000/api/v2/users/1').json())
print(requests.delete('http://localhost:5000/api/v2/users/999').json())
print(requests.delete('http://localhost:5000/api/v2/users/q').json())

print(requests.get('http://localhost:5000/api/v2/users').json())
print(requests.get('http://localhost:5000/api/v2/users/1').json())
print(requests.get('http://localhost:5000/api/v2/users/999').json())
print(requests.get('http://localhost:5000/api/v2/users/q').json())
