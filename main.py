#1
x = 2
a = "labas"
b = True
g = 3.545645645
#2
h = ["a", "b", "c"]
for x in h:
    print(x)

#3
mano_namas = 1
#4
f = float(3)
#5
def getting(t):
    return print(t)


getting(h);

#6. Kokias reikšmes turės x ir y kintamieji?
# kintamasis = "IlgasSakinys"
# x = kintamasis[2:5]
# y = kintamasis[7:9]
# x tures gas
# y tures ki

#7

#su mutable kintamieji gali buti pakeisti, not mutable kintamieji negali buti pakeisti

#8

def getting(t):
    if type(t) is dict:
        print(dict[t])
    else:
     print(t)