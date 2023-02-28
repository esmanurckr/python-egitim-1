first_name="peLin"
last_name="dJaNGo"

# birden fazla degisken icinde bilgiyi birleştirmek
full_name= "Merhaba " + first_name [0].upper() + ". " +last_name
print(full_name)

# fString ile yazimi:
full_name=f"Merhaba {first_name [0].upper()}. {last_name}"
print(full_name)

# hesaplama yaparak str sonucu dönmek 
# print("sonuc: "+ 10*10) #çalışmaz çünkü str ve int birleşmez
print("sonuc: ", 10*10 )
result="sonuc: 10*10"
result="sonuc:"+ str(10*10)
print(result)

result= f"sonuc:{10*10}"
print(result)


# function icinde yapılan hesaplamanın sonucunu dönmek 
def calculate(number):
    return number * number

result= f"sonuc { multiply (10)}"
print{"multiply  fonksiyonu kullanildi:", result}

# uzun iceriklerin belli bir kısmını göstermek
print{f"{result[:4]}"}

# yazıları ortalamak veya sağa yaslamak
print{" * " * 30}
print{f"{full_name:-^30}"}
print{f"{'python':->30}"}
print{f"{'django':->30}"}
print{"*" * 30}

# belli bir yapıda int yapılar olusturmak : 00034 gibi
print(f"{number:06}")