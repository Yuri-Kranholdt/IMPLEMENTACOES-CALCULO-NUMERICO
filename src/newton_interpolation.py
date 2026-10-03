def newton_interpolation(x_points, y_points, x_target):
    if len(x_points) == 0 or len(y_points) == 0:
        raise ValueError("nenhum ponto para interpolação informado")

    if len(x_points) != len(y_points):
        raise ValueError("estrutura inválida")

    polynomial_result = y_points[0]
    basis_product = 1

    depth_limit = len(x_points)
    remaining_points = len(x_points)

    order = 1
    while order < depth_limit:
        basis_product *= x_target - x_points[order-1]
        divided_differences = []
        order_base = order

        for i in range(0, remaining_points-1):
            x_right = x_points[order_base]
            x_left = x_points[i]
            actual_y = y_points[i]
            next_y = y_points[i+1]
            c = (next_y - actual_y) / (x_right - x_left)
            divided_differences.append(c)

            if i == 0:
                polynomial_result += c * basis_product

            order_base += 1

        y_points = divided_differences
        order += 1
        remaining_points -= 1

    return polynomial_result


if __name__ == "__main__":
    print(newton_interpolation([0, 10, 20], [4.20, 3.95, 3.80], 25))
