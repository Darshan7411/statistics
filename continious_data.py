n=int(input("enter the number of values to insert into data : "))
data=[]
freq=[]
freq_total=0
fx_total=0
fx=0
cf=0
cum_freq=[]
for i in range(n):
    print("enter the value to be inserted : ")
    val1,val2=int(input()),int(input())
    f=int(input("enter the freq to be inserted : "))
    data.append([val1,val2])
    freq.append(f)


print("\n|-----------|--------------|---------------|---------------|")
print("|     X     |       F      |       fx      |       cf      |")
print("|-----------|--------------|---------------|---------------|")

for i in range(len(data)):
    freq_total += freq[i]
    fx = ((data[i][0] + data[i][1]) // 2) * freq[i]
    fx_total += fx
    cf+=freq[i]
    cum_freq.append(cf)
    print(f"|  {data[i][0]:<3}-{data[i][1]:<3}  |     {freq[i]:<5}    |    {fx:<7}    |      {cf:<5}    |")
    print("|-----------|--------------|---------------|---------------|")


print(f"|           |   ∑f = {freq_total:<3}   |  ∑fx = {fx_total:<5}  |               |")
print("|-----------|--------------|---------------|---------------|")


#mean caluculation
mean=fx_total/freq_total



#median
fdiv2=freq_total//2
for i in range(len(cum_freq)):
    if cum_freq[i]>fdiv2:
        cfans=cum_freq[i]
        break






print(f"mean = {mean:.2f}")