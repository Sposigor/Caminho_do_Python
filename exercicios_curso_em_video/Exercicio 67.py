while True:
    T = int(input("Tabuada de qual valor? [Digite 0 para parar] "))
    if T == 0:
        print("Gostou, deixei o like!")
        break
    for I in range(1, 11):
        print(f"{T} x {I} = {T * I}")
   