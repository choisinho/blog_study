vips = ["홍길동", "청길동", "녹길동", "황길동"]
who = input("찾을 멤버는?")

for vip in vips: #무한루프
    if vip == who:
        print("찾았다... {}!!".format(vip))
        break
    else:
        continue
    print("{}를 비교하였음.".format(vip))