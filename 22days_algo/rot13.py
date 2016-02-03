#https://www.acmicpc.net/problem/11655
crypto = input()
out = ""
for a in crypto:
    ch = ord(a)
    # print(ch,end=" ")
    if ch == 109:
        out+="z"
    elif ch == 109-32:
        out+="Z"
    elif ch >= 65 and ch <=90:
        ch += 13-64
        re = ch %26
        out += chr(re+64)
    elif ch >=97 and ch <= 122:
        # 122
        ch += 13 - 96
        re = ch % 26
        out += chr(re+96)
        # print(ch+96, re, re+96)
    else:
        out += a

print(out)
# Baekjoon Online Judge
# Onrxwbba Bayvar Whqtr
# Onrxwbba Bayvar Whqtr
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ