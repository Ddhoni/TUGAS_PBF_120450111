#Author : MUHAMMAD DHONI APRIYADI
#NIM : 120450111
#Affiliation : Sains Data ITERA
#Program Description : Simple Pass Encrypt

def encrypt(pw):
  splitpass = list(pw) #mengubah input password menjadi bentuk list
  asciipass = list()
  for char in splitpass:
    asciichar = ord(char) #mengubah setiap karakter password menjadi nomor ASCII
    asciipass.append(asciichar) #menambahkan hasil pengubahan kedalam variabel 'asciipass'

  encryptedpass = ""
  #mengubah setiap nomor ASCII kemudian membaginya menjadi tiga buah value yg berbeda
  for num in asciipass: 
    val_1 = num//26 + 80 #nilai pertama menghasilkan 'faktor pembagi' yang telah ditambahkan 80
    val_2 = num%26 + 80 #nilai kedua menghasilkan modulus yang telah ditambahkan 80
    if val_1 > val_2: #nilai ketiga
      val_3 = '+'
    else:
      val_3 = '-'

    encryptedpass = encryptedpass + chr(val_1) + chr(val_2) + val_3
    #chr(string) akan mengubah nomor menjadi karakter sesuai ketentuan ASCII
    #hasilnya tinggal digabung dan ditambahkan ke variabel 'encryptedpass'
    

  return encryptedpass #akan mengembalikan password yang telah dienkripsi



def decrypt(pw):
  #kode untuk membagi encrypted pass setiap 3 Value
  #misalkan passwordnya 'TP+Sc-TQ+ ', nanti berubah menjadi ['TP+','Sc-','TQ+']
  splitpass = [pw[i:i+3] for i in range(0, len(pw), 3)]

  asciipass = list()
  for word in splitpass:
    
    val_1 = ord(word[0]) - 80 

    val_2 = ord(word[1]) - 80 
    
    val = 26 * val_1 + val_2 # a = mq + r
    asciipass.append(val) #nomor ASCII karakter yang diperolah ditambahkan ke variabel 'asciipass'

  password = ''
  for i in asciipass: #tinggal mengubah setiap nomor ASCII di 'asciipass' menjadi karakter biasa :)
    char = chr(i)
    password = password + char
    
  return password #akan mengembalikan password yang telah di-decrypt




print('mengenkripsi password')
x = 'Anak-anakcerdas2020'
hasilencrypt = encrypt(x)
print(hasilencrypt)

print('_' * 30)
print('mendekripsi password')
y = 'R]-TV-Sc-TS+Qc-Sc-TV-Sc-TS+Se-Sg-TZ-Sf-Sc-T[-Qh-Qf-Qh-Qf-'
print(decrypt(y))