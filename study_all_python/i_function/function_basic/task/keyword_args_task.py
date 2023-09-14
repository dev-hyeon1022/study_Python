# def age(kr,en,math):
#     return (kr + en + math) / 3
#
# score = 70,80,90
# print(age(**score))

# unpacking
# def age(kr,en,math):
#     return (kr + en + math) / len(score_info)
#
# score_info = {"kr": 60, "en": 80, "math": 90}
# print(age(**score_info))

#packing
def age(**info):
    kr, en, math = info.values()
    return (kr + en + math) / len(info)

score_info = {"kr": 60, "en": 80, "math": 90}

print(age(**score_info))




