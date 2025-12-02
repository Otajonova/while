son = int(input("Sonni kiriting:"))
yigindi = 0
asl_son = son
while asl_son > 0:
    qoldiq = asl_son % 10
    yigindi = yigindi + qoldiq
    asl_son = asl_son // 10
print(f"{son} ning raqamlari yig'indisi: {yigindi}")
