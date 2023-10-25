random_list = [3.1, 2.7, 5.5, 105, 737, 412, 'Hello', 'Python', 'world', 'AI']

# Filter() untuk memisahkan nilai float, int, dan string
# Dapat dikatakan menerapkan HoF tipe function as parameter karena ada filter() yang argumenya adalah fungsi dalam bentuk lambda
float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
string_data = list(filter(lambda x: isinstance(x, str), random_list))

# Dapat dikatakan menerapkan HoF tipe function as parameter karena ada map() yang argumenya adalah fungsi dalam bentuk lambda
# Map() untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
intdata_mapped = list(map(lambda x: {'ratusan': x // 100, 'puluhan': (x % 100) // 10, 'satuan': x % 10}, int_data))

# Output
print("Data Float:")
print(float_data)
print("Data Int:")
for item in intdata_mapped:
    print(item)
print("Data String:")
print(string_data)