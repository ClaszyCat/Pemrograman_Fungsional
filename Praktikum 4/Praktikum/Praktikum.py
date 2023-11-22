import math

def input_point(prompt):
    point = input(prompt)
    x, y = map(int, point.split())
    return x, y

def calc_gradient(a, b):
    x1, y1 = a
    x2, y2 = b
    return (y2 - y1) / (x2 - x1)

def calc_constanta(point, gradient):
    x1, y1 = point
    return y1 - gradient * x1

def transformation(gradient, c):
    return f"y = {gradient:.2f}x + {c:.2f}"

def decorator(transformation_func):
    def wrapper(pointA, pointB, *args):
        transformed_points = transformation_func(pointA, pointB, *args)
        return transformed_points
    return wrapper

@decorator
def translasi(pointA, pointB, tx, ty):
    x1, y1 = pointA
    x2, y2 = pointB
    return [(x1 + tx, y1 + ty), (x2 + tx, y2 + ty)]

@decorator
def rotasi(pointA, pointB, theta_degrees):
    def rotate_point(x, y, theta_degrees):
        theta_radians = math.radians(theta_degrees)
        x_rotated = x * math.cos(theta_radians) - y * math.sin(theta_radians)
        y_rotated = x * math.sin(theta_radians) + y * math.cos(theta_radians)
        return x_rotated, y_rotated

    def rotate_line(pointA, pointB, theta_degrees):
        x1, y1 = pointA
        x2, y2 = pointB

        x1_rotated, y1_rotated = rotate_point(x1, y1, theta_degrees)
        x2_rotated, y2_rotated = rotate_point(x2, y2, theta_degrees)

        return [(x1_rotated, y1_rotated), (x2_rotated, y2_rotated)]

    return rotate_line(pointA, pointB, theta_degrees)

@decorator
def dilatasi(pointA, pointB, scaleX, scaleY):
    x1, y1 = pointA
    x2, y2 = pointB
    return [(x1 * scaleX, y1 * scaleY), (x2 * scaleX, y2 * scaleY)]

def main(): 
    pointA = input_point("Masukkan titik A ( , ): ")
    pointB = input_point("Masukkan titik B ( , ): ")

    tx = float(input("Masukkan nilai translasi tx: "))
    ty = float(input("Masukkan nilai translasi ty: "))
    sudut = int(input("Masukkan sudut rotasi: "))
    scaleX = float(input("Masukkan faktor skala X: "))
    scaleY = float(input("Masukkan faktor skala Y: "))

    gradient = calc_gradient(pointA, pointB)
    constanta = calc_constanta(pointA, gradient)

    print("Sebelum ditransformasi : \n", transformation(gradient, constanta))

    translated_points = translasi(pointA, pointB, tx, ty)
    rotated_points = rotasi(*translated_points, sudut)
    scaled_points = dilatasi(*rotated_points, scaleX, scaleY)
    

    newGradient = calc_gradient(scaled_points[0], scaled_points[1])
    newConstanta = calc_constanta(scaled_points[0], newGradient)
    print("Setelah ditransformasi : \n", transformation(newGradient, newConstanta))
    
if __name__ == '__main__':
    main()