Teori = 70
Praktek = 70
nilai1 = int (input ("Masukkan Nilai Teori : "))
nilai2 = int (input("Masukkan Nilai Praktek : ")) 

if nilai1 & nilai2 >= 70:
    print ("Selamat anda lulus!")
elif nilai2 < 70 & nilai1 >= 70:
    print ("Anda harus mengulang ujian praktek")
elif nilai1 < 70 & nilai2 >= 70:
    print ("Anda harus mengulang ujian teori")
else:
    print ("Anda harus mengulang ujian teori dan praktek")
