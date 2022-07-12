import sqlite3
import numpy as np
import sqlite3
from collections import Counter

# 번호 정렬 및 구분자 - 추가하여 문자열화
def SortNumbers2(numbers):
    # numbers = [num1, num2, num3, num4, num5, num6]
    s = ''
    for num in sorted(numbers):
        s = s + str(num) + '-'
    return s

# 추출번호, 빈도수를 순서를 변경하여 오름차순 정렬하여 빈도수가 가장 적은 숫자를 추출
def WorstCommon(numbersList, n):
    tempCommon = []
    for number in numbersList:
        # print(number)
        a, b = number
        number2 = b, a
        # print(number2)
        tempCommon.append(number2)

    # print (mostCommon)
    # print (worstCommon)
    worstCommon = sorted(tempCommon)

    # print(worstCommon)

    worstNumbers = []
    for i in range(n):
        # print(worstCommon[i][1])
        worstNumbers.append(worstCommon[i][1])

    return worstNumbers

# 로또 db를 조회하여 숫자별 빈도수를 빈번한 수 기준으로 리턴하고,
# 추가로 n 파라미터를 전달 받아 최대 빈번순으로 n개의 숫자를 리턴
def MostCommon(n):
    # 담청번호 db를 조회하여 번호출 빈도수 추출
    allNumbers = []
    conn = sqlite3.connect("lottoAdd.db")

    # 커서 바인딩
    c = conn.cursor()

    # 데이터 조회(전체)

    c.execute("SELECT sorted FROM LottoNo")

    # print('param', c.fetchone())
    # print('param', c.fetchall())

    allNumbers = c.fetchall()
    # allNumbers = c.fetchone()
    # print(len(allNumbers))

    k_lott = []

    for numbers in allNumbers:
        # print (numbers)
        # print (type(numbers))
        numbersList = []
        numbersStr = ''.join(numbers)

        num = numbersStr.split('-')
        num = ' '.join(num).split()
        # print(num)
        for x in num:
            k_lott.append(int(x))

    c = Counter(k_lott)
    # print (k_lott)
    # print(Counter(k_lott))

    # print(c.most_common(10))
    mostCommon = c.most_common()
    mostCommonNum = c.most_common(n)

    commonNumbers = []
    for numbers in mostCommonNum:
        commonNumbers.append(numbers[0])

    return mostCommon, commonNumbers

def GetLottoNum(numberlist, n):
    lottoNumList = []
    # numberlist = range(1, 46)
    extractCnt = n
    while extractCnt != 0:
        # 임의 번호 6개 추출
        x = []
        # for i in range(6):
        #     x.append(random.randint(1,45))
        x = list(np.random.choice(numberlist, 6, replace=False))
        #print(SortNumbers2(x))

        ###########################################################
        # 1~1021 담청 번호 기존재하는지 조회
        # DB 파일 조회(없으면 새로 생성)
        conn = sqlite3.connect("lottoAdd.db")

        # 커서 바인딩
        c = conn.cursor()

        # 데이터 조회(전체)

        c.execute("SELECT * FROM LottoNo")

        param = SortNumbers2(x)
        c.execute("SELECT * FROM LottoNo WHERE sorted='%s'" % param)  # %s %d %f
        #print('param', c.fetchone())
        # print('param', c.fetchall())

        # conn.close()
        ###########################################################

        if (c.fetchone() is None):
            # print("Numbers not founded")
            lottoNumList.append(x)
            extractCnt -= 1

        if (c.fetchone() is not None):
            print("Numbers founded")
        #print(extractCnt)

    return lottoNumList

# 1. 기본 기준
numberlist = range(1, 46)
print(GetLottoNum(numberlist, 2))

# 2. 최빈 기준, 숫자 10개
mostCommon, commonNumbers = MostCommon(10)
# # print(numberlist)
# print(GetLottoNum(commonNumbers, 2))
#
# 3. 가장 드문 기준, 숫자 10개
worstNumbers = WorstCommon(mostCommon, 10)
# # print(numberlist)
# print(GetLottoNum(worstNumbers, 2))

# 4. 최빈 + 가장 드문 기준, 숫자 20개
print(GetLottoNum(commonNumbers+worstNumbers, 3))