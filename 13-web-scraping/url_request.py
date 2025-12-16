import urllib.request

url = "https://www.example.com"

try:
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(f"Status: {response.status}")
    print(f"Content length: {len(html)}")
    print(f"First 200 characters:\n{html[:200]}")
except Exception as e:
    print(f"Error: {e}")
