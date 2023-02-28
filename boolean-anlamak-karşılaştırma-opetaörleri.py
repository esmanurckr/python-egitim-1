# içinde bilgi var mı
# "lorem"
#10
#-10
#0
username=""
print(bool(username))

age=10
print(bool(age))

# yasi eşit mi sıfıra?

age=0
print(bool(age==0))

# yasi eşit değildir 0'a ?
age=25
print (age!=20)
print (not age==0)

# yasi 18 den büyük mü ?
print(age>18)


# yasi 18 den küçük mü ?
print(age<18)


# yasi 18 den büyük mü küçük mü?
print(age>=18)

# yas bilgisi 20 ile 30 arasında mı?

print(20<age<30)

# yasi 18 den büyük mü veya kadın mı?

gender="m"
age=10
print("yasi 18 den büyük mü kadın mı? Or kullanımı", age>18 or gender=="f")

# yasi 18 den büyük mü ve kullanıcı bilgisi var mı ?

username=""
print("yasi 18den büyük mü ve kullanıcı bilgisi var mı "age>18 and bool(username))
print("yasi 18den büyük mü ve kullanıcı bilgisi var mı "age>18 and username)
print("yasi 18den büyük mü ve kullanıcı bilgisi var mı "age>18 and not username=="")

username="lorem"
print("yasi 18den büyük mü ve kullanıcı bilgisi var mı "age>18 and bool(username))