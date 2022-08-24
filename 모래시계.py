count = int(input("입력: "))
print("#"*count)
b = " "
s = "*"
for i in range(count-2, 0, -2):
    print("#%s%s%s#" % (" "*round((count-i-2)/2), "*"*i, " "*round((count-i-2)/2)))
for i in range(3, count-1, 2):
    print("#%s%s%s#" % (" "*round((count-i-2)/2), "*"*i, " "*round((count-i-2)/2)))
print("#"*count)

###################


# def sandglass(a):
#     print("#"*a)
#     blank = 0
#     for i in range(a-2):
#         print("#" + " "*blank + "*" * (a-2-2*blank) + " "*blank + "#")
#         if i < (a-3)/2:
#             blank += 1
#         else:
#             blank -= 1
#     print("#"*a)


# sandglass(13)
