def perkalian(a):
    def dengan(b):
        return a*b
    return dengan #mengembalikan fungsi inner operator

#High Order Function
def perkalian_HOF():
    angka_pertama = perkalian(5)
    hasil = angka_pertama(5)
    print("Hasil dengan HOF: ", hasil)
perkalian_HOF()

#Currying Function

def perkalian_curry():
    hasil = perkalian (4)(5)
    print("Hasil dengan Curry: ", hasil)
perkalian_curry()