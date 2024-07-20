x = 10
y = 20

if (diff := x - y) > 0:
    print(f"{x} is greater than {y} by {diff}")
elif diff < 0:
    print(f"{y} is greater than {x} by {abs(diff)}")
else:
    print(f"{x} is equal to {y}")
