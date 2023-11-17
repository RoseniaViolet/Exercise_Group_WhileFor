approximation = 3.0
sign = 1.0

for i in range(1, 16):
    denominator = 2 * i * (2 * i + 1) * (2 * i + 2)
    term = 4 / denominator
    approximation += sign * term
    sign *= -1  
print(f"Approximation {i}: {approximation}")
