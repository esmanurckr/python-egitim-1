# input ile first_name bilgisini al
# input ile last_name  bilgisini al
# input ile year_of_birth bilgisini al
# first_name ve last_name bilgilerinin karakter sayisini yazdır
# fString ile kullanıcının adının ilk harfi büyük olacak şekilde full_name yazdır
# yaşını ve gelecek senedeki yaşını fString ile yazdır
# 18 yasından büyükse True bilgisini dön 

first_name=input("Adiniz: ")
last_name=input("sayadiniz: ")
year_of_birth=input("Dogum yiliniz: ")
print(f"ad karakter sayisi: {len(first_name)}, soyad karakter sayisi: {len(last_name)}")
full_name= f"{first_name[0].upper()}. {last_name}"
print(f"yasiniz: {2022 - int(year_of_birth)}, Gelecek yil{(2022+1)-int(year_of_birth)} Yasinda olacaksınız ")
#2022 yi elle yazıyor olmak yanlış bir çözüm .. muhakkak tarihin yil bilgisi alınmaliydi ama
#bu video hazirkanirken aslında sen bunu bilmediğin için çözüm olarak elle yazdik

print(f"yasiniz 18 den büyük mü??{2022- int(year_of_birth>18)}")
 