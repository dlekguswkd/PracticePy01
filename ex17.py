# 키보드에서 정수로 된 돈의 액수를 입력받아 50000원권, 10000원권, 5000원권, 1000원권, 500원동전, 100원동전, 50원동전, 1원동전 각 몇 개로 변환 되는지 작성 하세요.

no = int(input("금액: "))


# print(f"50000원: {int(no//50000)}개")
# print(f"10000원: {int(no//10000)}개")
# print(f"5000원: {int(no//5000)}개")
# print(f"1000원: {int(no//1000)}개")
# print(f"500원: {int(no//500)}개")
# print(f"100원: {int(no//100)}개")
# print(f"50원: {int(no//50)}개")
# print(f"10원: {int(no//10)}개")
# print(f"5원: {int(no//5)}개")
# print(f"1원: {int(no//1)}개")


units = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

for unit in units:
    count = no // unit  # 현재 단위로 나눈 몫
    no %= unit          # 남은 금액 업데이트
    print(f"{unit}원: {count}개")