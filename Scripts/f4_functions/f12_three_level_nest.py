x = 10 # global

def funct1():
    x = 20
    def funct2():
        x = 30
        print("funct2", x)
        def funct3():
            print("funct3", x)
        funct3()
            
    funct2()
    print("funct1", x)
    
funct1()
print(x)