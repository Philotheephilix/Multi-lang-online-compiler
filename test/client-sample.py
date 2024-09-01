import requests

base_url = 'http://127.0.0.1:5000'
headers = {
    'clientId': 'qq'
}
response = requests.post(f'{base_url}/execute/C', json={"code":"""
#include <stdio.h>

int main() {
    printf("hello INFINITE LOOPS ");
    return 0;
}
"""},headers=headers)
print("API Response:", response.json()['received'])
