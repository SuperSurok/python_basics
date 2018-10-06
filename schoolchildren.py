"""N школьников делят K яблок поровну,
не делящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику?"""
schoolchildrenNumbers = int(input())
appleNumbers = int(input())
schoolchildrenApples = appleNumbers // schoolchildrenNumbers
print(schoolchildrenApples)
