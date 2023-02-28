first_name="Esmanur"
last_name="Çakır"
user_name="123456789"

# str nin ilk karakteri [0]
print(first_name[0])
print(last_name[1])

# belli bir yerden başlayan bilgiyi göster[3:10]
print(first_name[2:200])

# baştan 3 karakter[:3]
print(first_name[:3])

# sondan 3 karakter[:3]
print(first_name[-3:])

# son 3 karakteri gösterme [:-3]
print(first_name[:-3])

# ters çevir [::-1]
print(first_name[::-1])

# Tümü büyük harf olsun --> upper
full_name=first_name.upper()+" "+ last_name.upper()
print(full_name)

# İlk harfi büyük olsun -->capitalize
print(full_name.capitalize())

# İlk harfleri büyük olsun -->title
print(full_name.title())

# Ters çevir -->swapcase
print(full_name.swapcase())

# Küçük harf olsun -->lower
print(full_name.lower())

# say--> count
print(full_name.lower().count('n'))

# liste içindekileri birleştir-->join
names= ["Pelin","Cem","Esmanur","Melisa","Esra","Deniz"]
print(" ".join(names))



# parçala/ ayır -->split
print(full_name.split(" "))

# SOR:::

# Başlık şeklinde mi? istitle
print("Django".istitle())
print(last_name.istitle())

# Hepsi küçük harfle mi? islower
print("Django".islower())
print(last_name.islower())

# print(input("Adiniz Yaz: ").islower())

#belli bir karakterle başlıyor mu? startswith
print("belli bir karakterle basliyor mu? startswith",first_name.startswith("p"))

#belli bir karakterle bitiyor mu? endswith
print("belli bir karakterle basliyor mu? endswith",first_name.endswith("p"))

# aradiğim bilgi str içinde var mı ? find

print(user_name.find("3"))
print(user_name[user_name.find("7"): ])
print:(full_name[full_name.lower().find("n"):])

# belli bir bilgiyi değiştir? replace
print(full_name.replace("Esmanur","Python"))



