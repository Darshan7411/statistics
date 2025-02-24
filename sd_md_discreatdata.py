import math
# Get space-separated input
data = list(map(int, input("Enter space-separated X values numbers: ").split()))
freq = list(map(int, input("Enter space-separated Frequency numbers: ").split()))


def standard_deviation(data,freq):
    # Step 1: Calculate weighted mean
    mean = sum(x * f for x, f in zip(data, freq)) / sum(freq)
    mean = round(mean, 3)  # Round to 3 decimal places

    # Step 2: Compute (Xi - mean)^2
    x_m = [abs(round((x - mean),3))  for x in data]
    x_mean = [round((x - mean) ** 2,3) for x in data]

    # Step 3: Multiply by corresponding frequencies
    fx = [round(f * xm,3) for f, xm in zip(freq, x_mean)]
    fm=[round(f * xm,3) for f, xm in zip(freq, x_m)]


    # Step 4: Compute standard deviation
    variance = sum(fx) / sum(freq)
    std_dev = math.sqrt(variance)

    return x_mean, mean, fx, round(std_dev, 2),round(sum(fm)/sum(freq),3)



sd=standard_deviation(data,freq)
print("\n|-----------|--------------|-----------------------|--------------------|")
print("|     X     |       F      |       (x - x̄)²        |    f(x - x̄)²       |")
print("|-----------|--------------|-----------------------|--------------------|")

for i in range(len(data)):

    print(f"|  {data[i]:<5}    |    {freq[i]:<5}     |      {sd[0][i]:<10}       |    {sd[2][i]:<10}      |")
    print("|-----------|--------------|-----------------------|--------------------|")

print(f"|    ∑      |    {sum(freq):<5}     |       {round(sum(sd[0]),2):<10}      |     {round(sum(sd[2]),2):<10}     |")
print("|-----------|--------------|-----------------------|--------------------|")

print("\nstandard deviation is",sd[3])
print("\n Mean deviation is ",sd[4])