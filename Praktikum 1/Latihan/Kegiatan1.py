def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        left_operand, operator, right_operand = node
        if operator == '+':
            return tambah(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))

# fungsi pertambahan


def tambah(kiri, kanan):
    return kiri + kanan


# fungsi pengurangan


def minus(kiri, kanan):
    return kiri - kanan

# fungsi perkalian


def mult(kiri, kanan):
    return kiri * kanan


# fungsi pembagian


def div(kiri, kanan):
    kiri / kanan


# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
# expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)
