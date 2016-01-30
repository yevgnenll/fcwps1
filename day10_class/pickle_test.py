import pickle
import datetime
from .fileio import readFile

file = readFile()
print(file.readTextLine('/Users/yevgnenll/Desktop/fileio.txt', "rt"))





#날짜 데이터를 가져온다
now1 = datetime.datetime.utcnow()
#가져온 날짜 데이터를 암호화 한다
pickled = pickle.dumps(now1)
#위에서 암호화한 값을 복호화 한다
now2 = pickle.loads(pickled)



file = open("/Users/yevgnenll/Desktop/pickle1", "wb")
file.write(pickled)
file.close()

dcrypt = open("/Users/yevgnenll/Desktop/pickle1", "rb")
result = dcrypt.read()
"""
8003 6364 6174 6574 696d 650a 6461 7465
7469 6d65 0a71 0043 0a07 e001 0f08 3b1c
03d1 4971 0185 7102 5271 032e
"""
print(result)
dcrypt.close()

print(now2)