import math

# Get class intervals input
class_intervals = input("Enter space-separated class intervals (e.g., '10-20 20-30 ...'): ").split()
freq = list(map(int, input("Enter space-separated Frequencies: ").split()))

# Convert class intervals to midpoints
data = [(int(interval.split('-')[0]) + int(interval.split('-')[1])) / 2 for interval in class_intervals]

def compute_statistics(data, freq):
    N = sum(freq)  # Total frequency

    # Step 1: Compute mean (X̄)
    mean = round(sum(x * f for x, f in zip(data, freq)) / N, 3)

    # Step 2: Compute standard deviation (σ)
    x_mean_sq = [round((x - mean) ** 2, 3) for x in data]  # (X - X̄)^2
    fx_mean_sq = [round(f * xm, 3) for f, xm in zip(freq, x_mean_sq)]  # f(X - X̄)^2
    variance = round(sum(fx_mean_sq) / N, 3)
    std_dev = round(math.sqrt(variance), 3)  # Standard deviation (σ)

    # Step 3: Compute skewness (Sk)
    x_mean_cube = [round((x - mean) ** 3, 3) for x in data]  # (X - X̄)^3
    fx_mean_cube = [round(f * xm, 3) for f, xm in zip(freq, x_mean_cube)]  # f(X - X̄)^3
    skewness = round(sum(fx_mean_cube) / (N * (std_dev ** 3)), 3)

    # Step 4: Compute kurtosis (Ku)
    x_mean_quad = [round((x - mean) ** 4, 3) for x in data]  # (X - X̄)^4
    fx_mean_quad = [round(f * xm, 3) for f, xm in zip(freq, x_mean_quad)]  # f(X - X̄)^4
    kurtosis = round(sum(fx_mean_quad) / (N * (std_dev ** 4)), 3)

    return mean, std_dev, skewness, kurtosis, x_mean_sq, fx_mean_sq, x_mean_cube, fx_mean_cube, x_mean_quad, fx_mean_quad

# Compute statistics
mean, std_dev, skewness, kurtosis, x_mean_sq, fx_mean_sq, x_mean_cube, fx_mean_cube, x_mean_quad, fx_mean_quad = compute_statistics(data, freq)

# Display results
print("\n|-----------------|-----------|------|--------------|----------------|----------------|----------------|----------------|--------------|")
print("|  Class Interval |   Mid(X)  |  F   |   (X - X̄)²   |  f(X - X̄)²     |  (X - X̄)³      |  f(X - X̄)³     |  (X - X̄)⁴      |  f(X - X̄)⁴   |")
print("|-----------------|-----------|------|--------------|----------------|----------------|----------------|----------------|--------------|")

for i in range(len(data)):
    print(f"|  {class_intervals[i]:<12}   |   {data[i]:<7} | {freq[i]:<4} |   {x_mean_sq[i]:<10} |   {fx_mean_sq[i]:<10}   |   {x_mean_cube[i]:<10}   |   {fx_mean_cube[i]:<10}   |   {x_mean_quad[i]:<10}   |   {fx_mean_quad[i]:<10} |")
    print("|-----------------|-----------|------|--------------|----------------|----------------|----------------|----------------|--------------|")

print(f"|      ∑          |           | {sum(freq):<4} |   {round(sum(x_mean_sq), 3):<10} |   {round(sum(fx_mean_sq), 3):<10}   |   {round(sum(x_mean_cube), 3):<10}   |   {round(sum(fx_mean_cube), 3):<10}   |   {round(sum(x_mean_quad), 3):<10}   |   {round(sum(fx_mean_quad), 3):<10} |")
print("|-----------------|-----------|------|--------------|----------------|----------------|----------------|----------------|--------------|")

print(f"\nMean (X̄)          : {mean}")
print(f"Standard Deviation (σ) : {std_dev}")
print(f"Skewness (Sk)     : {skewness}")
print(f"Kurtosis (Ku)     : {kurtosis}")
