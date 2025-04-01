import requests

def test_flask(): 
    url = 'http://localhost:5000/api/results'
    payload = {
        '1': 'word', 
        '2': 'test', 
        '3': 'monument', 
        '4': 'sailboat'
    }
    r = requests.post(url, json=payload)
    print(r.text)

test_flask()