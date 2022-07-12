import requests
import json
import sqlite3

def SortNumbers(num1, num2, num3, num4, num5, num6):
    numbers = [num1, num2, num3, num4, num5, num6]
    s = ''
    for num in sorted(numbers):
        s = s + str(num) + '-'
    return s


def DataSave(jsResult):
    drwNo = jsResult["drwNo"]                   # 회차
    drwNoDate = jsResult["drwNoDate"]           # 당첨일
    drwtNo1 = jsResult["drwtNo1"]               # 당첨번호1
    drwtNo2 = jsResult["drwtNo2"]               # 당첨번호2
    drwtNo3 = jsResult["drwtNo3"]               # 당첨번호3
    drwtNo4 = jsResult["drwtNo4"]               # 당첨번호4
    drwtNo5 = jsResult["drwtNo5"]               # 당첨번호5
    drwtNo6 = jsResult["drwtNo6"]               # 당첨번호6
    bnusNo = jsResult["bnusNo"]                 # 보너스번호
    totSellamnt = jsResult["totSellamnt"]       # 누적당첨금
    firstWinamnt = jsResult["firstWinamnt"]     # 1등당첨금
    firstPrzwnerCo = jsResult["firstPrzwnerCo"] # 1등당첨인원
    firstAccumamnt = jsResult["firstAccumamnt"] # 1등당첨금총액
    sortedNumbers = SortNumbers(drwtNo1, drwtNo2, drwtNo3, drwtNo4,drwtNo5, drwtNo6)
    returnValue = jsResult["returnValue"]       # 실행결과

    conn = sqlite3.connect("lottoAdd.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS LottoNo (drwNo integer, drwNoDate text, drwtNo1 integer, 
                drwtNo2 integer, drwtNo3 integer, drwtNo4 integer, drwtNo5 integer, drwtNo6 integer, 
                bnusNo integer, totSellamnt integer, firstWinamnt integer, firstPrzwerCo integer, 
                firstAccumamnt integer, sorted Numbers)''')

    c.execute("INSERT INTO LottoNo VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (drwNo,drwNoDate,drwtNo1,drwtNo2,drwtNo3,drwtNo4,drwtNo5,drwtNo6,bnusNo,totSellamnt,
               firstWinamnt,firstPrzwnerCo,firstAccumamnt, sortedNumbers))

    conn.commit()

    conn.close()

    print(str(drwNo) + "|" + drwNoDate + str(drwtNo1) + "|" + str(drwtNo2) + "|" + str(drwtNo3) + "|" + str(drwtNo4) + "|" + str(drwtNo5) + "|" + str(drwtNo6) + "|" + str(bnusNo) + "|" + str(totSellamnt) + "|" + str(firstWinamnt) + "|" + str(firstPrzwnerCo) + "|" + str(firstAccumamnt) + "|" + sortedNumbers)


lotto_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="

#### 1022회, 22.06.25
for i in range(1021, 1022):
    i += 1
    resp = requests.get(lotto_url + str(i))
    jsResult = resp.json()
    DataSave(jsResult)