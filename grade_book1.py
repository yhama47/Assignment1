english_grade = input("英語の成績を入力して下さい>")
math_grade = input("数学の成績を入力して下さい>")

print("英語の得点:" + (english_grade))
print("数学の得点:" + (math_grade))

total = int(english_grade) + int(math_grade)
average = (int(english_grade) + int(math_grade))/ 2

print("合計:" + str(total))
print("平均:" + str(average))