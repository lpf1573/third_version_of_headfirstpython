import requests

# 替换为你的 Shadowsocks 代理地址和端口
proxies = {
     'http':'127.0.0.1:1080',
     'https':'127.0.0.1:1080',
     
}

# 替换为你需要访问的被禁网址
url = 'https://en.wikipedia.org/wiki/List_of_world_records_in_swimming'
# url='https://google.com'

try:
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # 检查是否有 HTTP 错误
    print(response.text)
except requests.RequestException as e:
    print(f"Request failed: {e}")