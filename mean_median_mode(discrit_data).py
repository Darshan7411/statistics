n=int(input("enter the number of values to insert into data : "))
data=[]
freq=[]
for i in range(n):
    val=int(input("enter the value to be inserted : "))
    f=int(input("enter the freq to be inserted : "))
    data.append(val)
    freq.append(f)

def mean(data,freq):
    total_sum=0
    freq_total=0
    for i in range(n):
        total_sum+=(data[i]*freq[i])
        freq_total+=freq[i]

    print(f"∑fx = {total_sum}")
    print(f"∑f = {freq_total}")
    print(f"mean = {round(total_sum/freq_total)}")

dataset=sorted(data)
def median(data,freq):
    sum=0
    if len(data)%2==0:
        median_value = (dataset[(n // 2) - 1] + dataset[n // 2]) / 2
        print("median = ",median_value)
    else:
        print(f"median = {data[len(data)//2]}")

def mode(data,freq):
    print(f"mode = {data[freq.index(max(freq))]}")

print("|-----------|-----------|")
print("|     X     |     F     |")
print("|-----------|-----------|")
for i in range(n):
    print(f"|   {data[i]:5}   |   {freq[i]:5}   |")
    print("|-----------|-----------|")




mean(data,freq)
median(data,freq)
mode(data,freq)
