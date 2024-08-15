import gazpacho
import json


import requests
from gazpacho import Soup

# 定义代理
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}

# 目标 URL
url = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"

try:
    # 使用 requests 库通过代理获取网页内容
    response = requests.get(url, proxies=proxies)
    response.raise_for_status()  # 检查是否有 HTTP 错误
    
    # 获取 HTML 内容
    html = response.text
    
    # 使用 gazpacho 解析 HTML
    soup = Soup(html)
    
    # 选择和打印所有的表格行
    # rows = soup.select('tr')  # 使用 CSS 选择器选择所有表格行
    # for row in rows:
    #     print(row.text)  # 打印每一行的文本内容

except requests.RequestException as e:
    print(f"Request failed: {e}")


URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
RECORDS = (0, 2, 4, 5)
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")
WHERE = "/home/headfirstpython/webapp/"
# WHERE = ""
JSONDATA = "records.json"

# html = gazpacho.get(URL)
soup = gazpacho.Soup(html)
tables = soup.find("table")
records = {}
for table, course in zip(RECORDS, COURSES):
    records[course] = {}
    for row in tables[table].find("tr")[1:]:
        columns = row.find("td")
        event = columns[0].text
        time = columns[1].text
        if "relay" not in event:
            records[course][event] = time
with open(WHERE + JSONDATA, "w") as jf:
    json.dump(records, jf)
