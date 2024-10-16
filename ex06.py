# 상품을 구매하면 정가의 10%를 부가세로 부여한다. 아래와 같이 출력되도록 프로그램을 작성하세요

price = float(input("상품가격: "))
money = float(input("받은돈: "))

print("====================")
print(f"받은돈: {money}")
print(f"상품가격: {price}")
print(f"부가세: {price*0.1}")
print(f"잔액: {money-price}")