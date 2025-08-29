
nama = "Radit"
program_kesukaan = "Python"
umur = 18
input_user = input("Mau tau nama saya? Kalo mau ketik 'ya'!: ")
if input_user == "ya":
    print("Nama saya adalah " + nama)
    input_user = input("Mau tau umur saya?: ")
    if input_user == "ya":
        print("Umur saya adalah " + str(umur) + " tahun")
        input_user = input("Mau tau program kesukaan saya?: ")
        if input_user == "ya":
            print("Program kesukaan saya adalah " + program_kesukaan)
        else:
            print("Oke deh, makasih ya udah mampir :)")
    else:
        print("Oke deh, makasih ya udah mampir :)")
else:
    print("Oke deh, makasih ya udah mampir :)")