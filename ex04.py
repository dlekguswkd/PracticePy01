# 직사각형의 둘레와 면적을 구하는 프로그램을 작성하세요.(가로 세로 변수 double형으로 작성)
# double -> float

width = float(input("가로를 입력하세요: "))

height = float(input("세로를 입력하세요: "))

print(f"사각형의 넓이는 {width*height}")
print(f"사각형의 둘레는 {width*2+height*2}")