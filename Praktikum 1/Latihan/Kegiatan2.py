random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

float_list = ()
str_list = []
int_dict = {}

i = 0
for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict[item] = {"ratusan": ratusan,
                          "puluhan": puluhan, "satuan": satuan}
        # int_dict["key{}", format(i)] = item
        # i += 1
    elif isinstance(item, float):
        float_list += (item)
    elif isinstance(item, str):
        str_list.append(item)
    # elif isinstance(item,int):
    #     # int_dict["key{}", format(i)] = item
    #     # i += 1

print("Data dalam float dalam bentuk Tuple:", float_list, end='\n\n')
print("Data dalam string dalam bentuk Tuple:", str_list, end='\n\n')
print("Data dalam integer dalam bentuk Tuple:", int_dict, end='\n\n')
