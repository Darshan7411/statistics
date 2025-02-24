import math
import matplotlib.pyplot as plt
import seaborn as sns

x = list(map(int, input("Enter space-separated X values : ").split()))
y = list(map(int, input("Enter space-separated Y values : ").split()))

mean_x=round(sum(x)/len(x),3)
mean_y=round(sum(y)/len(y),3)

x_mean=[round((x-mean_x),3) for x in x ]
y_mean=[round((x-mean_y),3) for x in y ]
x_meansquared=[round(x**2,3) for x in x_mean ]
y_meansquared=[round(x**2,3) for x in y_mean ]

xy=[round(x*y,3) for x,y in zip(x_mean,y_mean)]

cov=round((sum(xy)/len(x)),3)

sdx=round((math.sqrt(sum(x_meansquared)/len(x))),3)
sdy=round((math.sqrt(sum(y_meansquared)/len(y))),3)

r=round((cov/(sdx*sdy)),3)

yonx=r*(sdy/sdx)


ybar=[ round((round(yonx,3)*x-(r*mean_x)+mean_y),3) for x in x]


#display tables
print("\n|--------------|---------------|---------------------|-----------------|----------------------|-----------------|-----------------|")
print("|      X       |        Y      |      (x - x̄)        |    (y - y)      |    (X - X̄)(y - y)    |    (x - x̄)^2    |     (y - y)^2   |")
print("|--------------|---------------|---------------------|-----------------|----------------------|-----------------|-----------------|")
for i in range(len(x)):
    print(f"|      {x[i]:<3}     |      {y[i]:<3}      |        {x_mean[i]:<5}        |    {y_mean[i]:<5}        |      {xy[i]:<5}           |     {x_meansquared[i]:<5}       |     {y_meansquared[i]:<5}       |")
    print("|--------------|---------------|---------------------|-----------------|----------------------|-----------------|-----------------|")
print(f"| sum ={sum(x):<3}     |      {sum(y):<3}      |        {sum(x_mean):<5}        |    {sum(y_mean):<5}        |      {sum(xy):5}           |     {sum(x_meansquared):<5}       |     {sum(y_meansquared):<5}       |")
print(
    "|--------------|---------------|---------------------|-----------------|----------------------|-----------------|-----------------|")

print(f"\n line of regression Y on x is Y={round(yonx,3)}X{'+' if round(yonx*mean_x+mean_y,3) >0 else '-'}{round(-yonx*mean_x+mean_y,3)}")
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x, y=y, color='blue', label="Actual Data")
sns.lineplot(x=x, y=ybar, color='red', label=f"Y={round(yonx,3)}X{'+' if round(yonx*mean_x+mean_y,3) >0 else '-'}{round(-yonx*mean_x+mean_y,3)}")

# Labels and Title
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title(f"Correlation Graph (r = {r})")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()