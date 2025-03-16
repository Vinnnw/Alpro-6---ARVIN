def ganjil(bawah, atas):
    if bawah < atas:
        start, end, step = bawah, atas, 1
    else:
        start, end, step = bawah, atas, -1
    
    if start % 2 == 0:
        start += step
    
    first = True
    for i in range(start, end, step * 2):
        if first:
            print(i, end="") 
            first = False
        else:
            print(f", {i}", end="")  
    print() 

print("Batas bawah = 10, batas atas = 30")
ganjil(10, 30)

print("Batas bawah = 97, batas atas = 82")
ganjil(97, 82)

