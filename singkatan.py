input = input("Masukkan kalimat: ")
kalimat = input.split()
output = ''.join([kata[0].upper() for kata in kalimat])
print("Output:", output)
