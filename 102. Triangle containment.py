# Calculate the area of ABC
# Calculate areas of PAB PBC and PCA (P being Origin)
# If origin in triangle, ABC should be equal to sum of PAB PBC and PCA
# Area A = [ x1(y2 – y3) + x2(y3 – y1) + x3(y1-y2)]/2

def triangle_area(a, b, c):
    """Returns area of triangle given 3 co-ordinates"""
    (x1, y1) = (a[0], a[1])
    (x2, y2) = (b[0], b[1])
    (x3, y3) = (c[0], c[1])
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area


def read_data(file_name):
    """Reads the data file and returns a list of list containing 3 triangle co-ordinates"""
    triangles = []
    with open(file_name, mode="r") as file:
        for line in file.readlines():
            co_ordinates_str = line.rstrip().split(",")
            co_ordinates = [int(i) for i in co_ordinates_str]
            (x1, y1) = (co_ordinates[0], co_ordinates[1])
            (x2, y2) = (co_ordinates[2], co_ordinates[3])
            (x3, y3) = (co_ordinates[4], co_ordinates[5])
            triangles.append([(x1, y1), (x2, y2), (x3, y3)])

    return triangles


def is_origin_in(coordinate_list):
    """Checks if a triangle contains the origin"""
    (a, b, c, o) = (coordinate_list[0], coordinate_list[1], coordinate_list[2], (0, 0))

    (abc, obc, aoc, abo) = (triangle_area(a, b, c), triangle_area(o, b, c),
                            triangle_area(a, o, c), triangle_area(a, b, o))

    return abc == obc + aoc + abo

def main():
    """The main function"""
    triangles = read_data("coordinates.txt")
    triangle_with_origin = 0
    for coordinate_list in triangles:
        if is_origin_in(coordinate_list):
            triangle_with_origin += 1
    print(f"No of triangles with origin: {triangle_with_origin}")


main()
