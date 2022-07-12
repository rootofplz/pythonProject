import sqlite3
from collections import Counter

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
    print(Counter(k_lott))

    # print(c.most_common(10))
    mostCommon = c.most_common()
    mostCommonNum = c.most_common(n)

    commonNumbers = []
    for numbers in mostCommonNum:
        commonNumbers.append(numbers[0])

    return mostCommon, commonNumbers


mostCommon, commonNumbers = MostCommon(10)
worstNumbers = WorstCommon(mostCommon, 10)

print (mostCommon)
print (commonNumbers)
print (worstNumbers)