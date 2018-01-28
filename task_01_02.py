plates = int(input())
detergent = float(input())
while True:
    if plates / detergent > 2:
        N = plates - detergent / 0.5
        print(">>> Моющее средство закончилось. Осталось " + str(int(N)) + " тарелок")
        break
    elif plates / detergent < 2:
        N = (detergent / 0.5 - plates)/2
        print(">>> Все тарелки вымыты. Осталось " + str(N) + " ед. моющего средства")
        break
    elif plates % detergent == 0:
        print(">>> Все тарелки вымыты, моющее средство закончилось")
        break
