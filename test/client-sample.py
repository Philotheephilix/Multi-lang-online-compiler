import requests

base_url = 'http://127.0.0.1:5000'
headers = {
    'clientId': 'j'
}
response = requests.post(f'{base_url}/execute/C', json={"code":"""
#include <stdio.h>

int main() {
    printf("hello INFINITE LOOPS ");
    return 0;
}
"""},headers=headers)
print("API Response:", response.json()['received'])


response = requests.post(f'{base_url}/execute/java', json={"code":"""
class j{
public static void main(String[] args){
System.out.println("hello world");
}
}
"""},headers=headers)
print("API Response:", response.json()['received'])
