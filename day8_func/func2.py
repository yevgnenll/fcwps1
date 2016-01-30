def computer(mouse, keyboard, os="OS X"):
    return {'keyword':keyboard, 'mouse':mouse, 'os':os}

def computer2(mouse, keyboard, os):
    return {'keyword':keyboard, 'mouse':mouse, 'os':os}


print(computer("mini", "mac keyboard", "mac os"))
print(computer(mouse="white", keyboard="silver", os="linux"))
print(computer("black", "white keyboard", os="linux centOS"))
#위치인자와 키워드 인자가 동시에 나타나면 키워드 인자가 뒤로 와야한다 : 키뒤
print(computer("silver", "linux keyboard"))
print(computer2("solo", "asus"))
