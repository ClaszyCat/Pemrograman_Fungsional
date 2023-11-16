def point(x,y):
    return x,y
def line_equation_of(p1, M):
    #TODO 1: gunakan inner function dan closure untuk menghitung nilai C
    def calculate_c():
        result = p1[0] - M * p1[1]
        return result 
    #TODO 2: panggil fungsi inner untuk mendapatkan nilai C
    C = calculate_c()
    return f"y = {M:.2f}x + {C:.2f}"
# Ubah nilai input dengan 3 digit NIM akhir 424 (Genap)
print("Persamaan garis yang melalui titik (4,2) dan bergradien 4:")
print(line_equation_of(point(4, 2),4))