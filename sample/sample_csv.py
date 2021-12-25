import csv
import time
import random

csv_file = open("./csv/sample.csv", "r", encoding="utf-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#header = next(f)
count = 0
question_list = []
for i in f:
    count += 1
    question_list.append(i)
print(count)
random.shuffle(question_list)

for i in question_list:
    print(i[0],len(i[0]),(len(i[0])//5 +1.0 )*0.5)
    time.sleep((len(i[0])//5 +1 )*1.0)
    print(i[1])
    time.sleep((len(i[1])//5 +1 )*1.0)
    
#辞書形式
#f = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

#for i in f:
    #print(i)

