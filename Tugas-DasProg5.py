#Tugas DasProg ke 5 

print("        DODONGKAL DONG      ")
print("===============================")
print("     DAFTAR VARIANT HARGA   ")
print("===============================")
print("O     Original       13000")
print("K     Keju           15000")
print("P     Pisang         15000")
print("PK    Pisang keju    18000")
print("N     Nangka         15000")

#deklarasi penggunaan variable awal

f = 0

dataRasa = []
dataHarga = []
dataQty = []
subTotal = []
total = 0

#perulangan tidak berhenti
while True :
    i=1 
    data = input ('inputkan kode pesanan '+str (i) +" : ")


    if data == "O" :
        dataRasa.append('Original')
        dataHarga.append(13000)

    elif data == "K":
        dataRasa.append('Keju')
        dataHarga.append(15000)

    elif data == "PK":
        dataRasa.append('Pisang Keju')
        dataHarga.append(18000)

    elif data == "P":
        dataRasa.append('Pisang')
        dataHarga.append(15000)

    elif data == "N":
        dataRasa.append('Nangka')
        dataHarga.append(15000)

    else :
        dataRasa ("variant rasa tidak ditemukan")
        dataHarga.append("0")
    
    qty = int(input("masukan jumlah yang ingin dibeli : "))
    dataQty.append(qty)
    print("apakah ada yang mau ditambahkan ?")
    lagi = input ("Y=ya / T=tidak...: ")
    if lagi == "T":
        break

print("\t\t Total Pesanan ")
print("___________________________________________________________")
for j in range (len(dataRasa)):
    print("Varian Rasa ke",j+1, "adalah :",dataRasa[j])
    print("jumlah beli  \t\t:", dataQty[j])
    subTotal.append(dataQty[j]*dataHarga[j])
    total = total + subTotal [j]
    print("Subtotal adalah \t:",subTotal [j]) 
    print("___________________________________________________________")

#print total dan ppn

print("\t\t Total \t\t:",total)
print("\t\t PPN \t\t:",total*0.1)

#print total bayar

print("___________________________________________________________")
totalBayar = total+total*0.1
print("\t\t Total Pembayaran \t:",totalBayar)

#print kembalian 

print("___________________________________________________________")
bayar = int(input('\t Masukan pembayaran \t:'))
print('\t Kembalian \t\t: ',bayar-totalBayar)
