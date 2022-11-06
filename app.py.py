import streamlit as st
import requests
def getAllBookstore() -> list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList
def getAllBookstore() -> list:
    url = "https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res

def getCountyOption(items) ->list:
    optionList = []
    for item in items:
        name = item['cityName'][0:3]#把cityname蘭問中的縣市名稱擷取出來，並指定給變數name
        if name not in optionList:#如果name不在optiopList中，把他加入進去
            optionList.append(name)
    return optionList
def app():
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118)
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()
def getAllBookstore():
	url = 'http://localhost:8501/'
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()# 將 response 轉換成 json 格式
	return res# 回傳值

def app():
	bookstorelist = getAllBookstore()# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
	st.header('特色書店地圖')
	st.metric('Total bookstore', 118) # 將 118 替換成書店的數量
	county = st.selectbox('請選擇縣市', ['A', 'B', 'C'])
	district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])
def getCountyOption(items):
	optionList = items = []# 創建一個空的 List 並命名為 optionList
	for item in items:
        name = item['cityName'][0:3]#台北市中正區，只要拿3個字
        if name not in name: continue
        for district in districts:
            if district not in name: continue
            specificBookstoreList.append(item)
    return specificBookstoreList
		# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		# hint: 想辦法處理 item['cityName'] 的內
    specificBo
		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
return optionList