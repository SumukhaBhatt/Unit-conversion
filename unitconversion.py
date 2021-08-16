

def a():
    def a1():
        
        
        root=Tk()
        root.title("Converter")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO TEMPERATURE CONVERSION: \n THIS CONVERTS CELSIUS TO FAHRENHEIT \n WRITE THE DATA IN CELSIUS \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            
            if c.isalpha():
                root=Tk()
                root.title("Conversion")
                root.geometry("500x200")
                app=Frame(root)
                app.pack()
                label2=(Label(app,text="Error , enter a number"))
                label2.pack()
                
            else:
                root=Tk()
                root.title("Conversion")
                root.geometry("400x200")
                app=Frame(root)
                app.pack()
                c=float(c)
                f=c*9/5+32
                labell=(Label(app,text=str(f)+" F"))
                labell.pack()
                ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",width=5,command=x)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,width=50,bg='white',)
        entry1.pack()
        
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO TEMPERATURE CONVERSION: \n THIS CONVERTS FAHRENHEIT TO CELSIUS\n WRITE THE DATA IN FAHRENHEIT \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            f=entry1.get()
            f=float(f)
            c=(f-32)*(5/9)
            labell=Label(app,text=str(c)+" C")
            labell.pack()
            ft=entry1.get()
           
            
        s1=Button(app,text="OK",width=5,command=x)
        s1.pack(side=RIGHT)
        a3()
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO TEMPERATURE CONVERSION: \n THIS CONVERTS CELSIUS TO KELVIN \n WRITE THE DATA IN CELSIUS \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            k=c+273.15
            labell=Label(app,text=str(k)+" K")
            labell.pack()
            ft=entry1.get()
             

        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
        
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO TEMPERATURE CONVERSION: \n THIS CONVERTS KELVIN TO CELSIUS \n WRITE THE DATA IN KELVIN \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c-273.15
            labell=Label(app,text=str(f)+" C")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
       
    
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO TEMPERATURE CONVERSION: \n THIS CONVERTS FAHRENHEIT TO KELVIN  \n WRITE THE DATA IN FAHRENHEIT \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=((c-32)*5/9)+273.3
            labell=Label(app,text=str(f)+" K")
            labell.pack()
            ft=entry1.get()
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO LENGTH CONVERSION: \n THIS CONVERTS KELVIN TO FAHRENHEIT \n WRITE THE DATA IN KELVIN \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=(c-273.3)*9/5+32
            labell=Label(app,text=str(f)+" F")
            labell.pack()
            ft=entry1.get()
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text="WELCOME TO \nTEMPERATURE\n CONVERSION ")
    lable1.pack()
    
    
    b1=Button(app,text="celsius to fahrenheit",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="celsius  to kelvin",width=25,height=2,fg="indigo",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="fahrenheit to celsius",width=25,height=2,fg="red",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="fahrenheit to kelvin",width=25,height=2,fg="violet",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="kelvin to fahrenheit",width=25,height=2,fg="orange",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="kelvin to celsius",width=25,height=2,fg="blue",bg='white',command=a6)
    b6.pack()
def l():
    def a1():
        
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO LENGTH CONVERSION: \n THIS CONVERTS KILOMETRE TO METRE \n WRITE THE DATA IN KILOMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO LENGTH CONVERSION: \n THIS CONVERTS KILOMETRE TO CENTIMETRE \n WRITE THE DATA IN KILOMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000*100
            labell=Label(app,text=str(f)+" Cm")
            labell.pack()
            ft=entry1.get()
           
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO LENGTH CONVERSION: \n THIS CONVERTS METRE TO CENTIMETRE \n WRITE THE DATA IN METRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*100
            labell=Label(app,text=str(f)+" Cm")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
        
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO LENGTH CONVERSION: \n THIS CONVERTS METRE TO MILLIMETRE \n WRITE THE DATA IN METRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Milli Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
       
    
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text="WELCOME TO LENGTH CONVERSION : \n THIS CONVERTS CENTIMETRE TO MILLIMETRE \n WRITE THE DATA IN CENTIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*10
            labell=Label(app,text=str(f)+" Milli Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
 
        
        
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text="WELCOME TO length CONVERSION: \n THIS CONVERTS MILLIMETRE TO CENTIMETRE \n WRITE THE DATA IN MILLIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c/10
            labell=Label(app,text=str(f)+" Cm")
            labell.pack()
            ft=entry1.get()
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
 
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text="WELCOME TO \n LENGTH \n CONVERSION ")
    lable1.pack()
    
    
    b1=Button(app,text="K.M to metre",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="K.M to Cm",width=25,height=2,fg="red",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="Metre to Cm",width=25,height=2,fg="violet",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="Metre to mm",width=25,height=2,fg="indigo",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="mm to Cm",width=25,height=2,fg="blue",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="Cm to MM",width=25,height=2,fg="orange",bg='white',command=a6)
    b6.pack()

def mass():
    def a1():
        
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION : \n THIS CONVERTS KILOGRAMS TO GRAMS \n WRITE THE DATA IN KILOGRAMS \n******************\n ENTER NUMBER BELOW ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Gram")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION: \n THIS CONVERTS KILOGRAMS TO MILLI GRAMS \n WRITE THE DATA IN KILOGRAMS \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000000
            labell=Label(app,text=str(f)+" Milli Gram")
            labell.pack()
            ft=entry1.get()
           
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION: \n THIS CONVERTS GRAMS TO MILLIGRAMS \n WRITE THE DATA IN GRAMS \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Milli Gram")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
        
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION: \n THIS CONVERTS MILLIGRAM TO GRAM \n WRITE THE DATA IN MILLIGRAM \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Grm")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
       
    
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION: \n THIS CONVERTS MILLIGRAM TO KILOGRAM \n WRITE THE DATA IN MILLIGRAM \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c/1000000
            labell=Label(app,text=str(f)+" Kg")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
 
        
        
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO MASS CONVERSION: \n THIS CONVERTS GRAM TO KILOGRAM \n WRITE THE DATA IN GRAM \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c/1000
            labell=Label(app,text=str(f)+" Kg")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text=":WELCOME TO \n MASS \n CONVERSION :  ")
    lable1.pack()
    
    
    b1=Button(app,text="K.G to Grams",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="K.G to M.Gram ",width=25,height=2,fg="orange",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="Gram to M.Gram",width=25,height=2,fg="red",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="M.gram to Gram",width=25,height=2,fg="violet",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="gram to KG",width=25,height=2,fg="blue",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="M.Gram to KG",width=25,height=2,fg="indigo",bg='white',command=a6)
    b6.pack()

def area():
    def a1():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE CENTIMETRE TO SQUARE FOOT \n WRITE THE DATA IN SQUARE CENTIMETRE \n******************\n ENTER NUMBER BELOW ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.001076391
            labell=Label(app,text=str(f)+" Square Foot")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE CENTIMETRE TO SQUARE INCH \n WRITE THE DATA IN SQUARE CENTIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.15500031
            labell=Label(app,text=str(f)+" Square Inch")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE CENTIMETRE TO SQUARE METRE \n WRITE THE DATA IN SQUARE CENTIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.0001
            labell=Label(app,text=str(f)+" Square Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE FOOT TO SQUARE INCH \n WRITE THE DATA IN SQUARE FOOT \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*144
            labell=Label(app,text=str(f)+" Square Inch")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE  FOOT TO SQUARE METRE \n WRITE THE DATA IN SQUARE  FOOT \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.09290304
            labell=Label(app,text=str(f)+" Square Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO AREA CONVERSION: \n THIS CONVERTS SQUARE INCH TO SQUARE METRE \n WRITE THE DATA IN SQUARE INCH \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.00064516
            labell=Label(app,text=str(f)+" Square Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
            
    
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text="WELCOME TO \n AREA \n CONVERSION ")
    lable1.pack()
    
    
    b1=Button(app,text="square cm to square foot",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="square cm to square inch ",width=25,height=2,fg="indigo",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="square cm to square metre",width=25,height=2,fg="red",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="square foot to square inch",width=25,height=2,fg="orange",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="square foot to square metre",width=25,height=2,fg="violet",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="square inch to square metre",width=25,height=2,fg="blue",bg='white',command=a6)
    b6.pack()
def volume():
    def a1():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS LITRE TO CUBIC CENTIMETRE \n WRITE THE DATA IN LITRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1000
            labell=Label(app,text=str(f)+" Cubic Centimetre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        

    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS LITRE  TO CUBIC METRE \n WRITE THE DATA IN LITRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.001
            labell=Label(app,text=str(f)+" Cubic Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS LITRE TO CUBIC INCH \n WRITE THE DATA IN LITRE \n******************\n ENTER NUMBER BELOW ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*61.0237440947
            labell=Label(app,text=str(f)+" Cubic Inch")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS CUBIC CENTIMETRE TO CUBIC METRE\n WRITE THE DATA IN CUBIC CENTIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.000001
            labell=Label(app,text=str(f)+" Cubic Metre")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS CUBIC CENTIMETRE  TO CUBIC INCH \n WRITE THE DATA IN CUBIC CENTIMETRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*0.0610237441
            labell=Label(app,text=str(f)+" Cubic Inch")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO VOLUME CONVERSION: \n THIS CONVERTS CUBIC METRE TO CUBIC INCH \n WRITE THE DATA IN CUBIC METRE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*61023.744094732
            labell=Label(app,text=str(f)+" Cubic Inch")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
        
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text="WELCOME TO \n VOLUME \n CONVERSION ")
    lable1.pack()
    
    
    b1=Button(app,text="litre to cubic centimetre",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="litre to cubic metre ",width=25,height=2,fg="blue",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="litre to cubic inch",width=25,height=2,fg="violet",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="cubic centimetre to cubic metre",width=25,height=2,fg="orange",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="cubic cm to cubic inch",width=25,height=2,fg="red",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="cubic metre to cubic inch",width=25,height=2,fg="indigo",bg='white',command=a6)
    b6.pack()
def data():
    def a1():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO DATA CONVERSION: \n THIS CONVERTS MEGABYTE TO KILOBYTE \n WRITE THE DATA IN MEGABYTE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1024
            labell=Label(app,text=str(f)+" KB")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    def a2():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO DATA CONVERSION: \n THIS CONVERTS MEGABYTE TO BYTE \n WRITE THE DATA IN MEGABYTE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1024*1024
            labell=Label(app,text=str(f)+" Byte")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    def a3():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO DATA CONVERSION: \n THIS CONVERTS MEGABYTE TO BIT \n WRITE THE DATA IN MEGABYTE \n******************\n ENTER NUMBER BELOW ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1024*1024*8
            labell=Label(app,text=str(f)+" Byte")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    def a4():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO DATA CONVERSION: \n THIS CONVERTS KILOBYTE TO BYTE \n WRITE THE DATA IN KILOBYTE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1024
            labell=Label(app,text=str(f)+" Byte")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    def a5():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=": WELCOME TO DATA CONVERSION : \n THIS CONVERTS KILOBYTE TO BIT \n WRITE THE DATA IN KILOBYTE \n******************\n ENTER NUMBER BELOW  ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*1024*8
            labell=Label(app,text=str(f)+" Bit")
            labell.pack()
            ft=entry1.get()
           
            
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    def a6():
        
        root=Tk()
        root.title("Conversion")
        root.geometry("800x300")
        app=Frame(root)
        app.pack()
        lable1=Label(app,text=":WELCOME TO DATA CONVERSION: \n THIS CONVERTS BYTE TO BIT \n WRITE THE DATA IN BYTE \n******************\n ENTER NUMBER BELOW ")
        lable1.pack()
        def x():
            c=entry1.get()
            c=float(c)
            f=c*8
            labell=Label(app,text=str(f)+" Bit")
            labell.pack()
            ft=entry1.get()
            
        s1=Button(app,text="OK",command=x,width=5)
        s1.pack(side=RIGHT)
        entry1=Entry(app,bg='white',width=50)
        entry1.pack()
    root=Tk()
    root.title("Conversion")
    root.geometry("1000x500")
    app=Frame(root)
    app.pack()
    lable1=Label(app,text="WELCOME TO \n  DATA \n CONVERSION ")
    lable1.pack()
    b1=Button(app,text="megabyte to kilobyte ",width=25,height=2,fg="green",bg='white',command=a1)
    b1.pack()
    b2=Button(app,text="megabyte to byte ",width=25,height=2,fg="violet",bg='white',command=a2)
    b2.pack()
    b3=Button(app,text="megabyte to bit",width=25,height=2,fg="red",bg='white',command=a3)
    b3.pack()
    b4=Button(app,text="kilobyte to byte",width=25,height=2,fg="purple",bg='white',command=a4)
    b4.pack()
    b5=Button(app,text="kilobyte to bit",width=25,height=2,fg="orange",bg='white',command=a5)
    b5.pack()
    b6=Button(app,text="byte to bit",width=25,height=2,fg="blue",bg='white',command=a6)
    b6.pack()
from tkinter import*
root=Tk()
root.title("Conversion")
root.geometry("3000x1000")
app=Frame(root)
app.pack()
lable1=Label(app,text="\n\n\n\n\n\n\nWELCOME \nTO\n UNIT CONVERSION\n PROGRAM \n\n\n\n CLICK YOUR CHOICE BELLOW\n\n\n\n\n\n",anchor=CENTER).pack()
b1=Button(app,text="temperature",width=10,height=7,fg="green",bg='white')
b1["command"]=a
b1.pack(side=RIGHT)
b2=Button(app,text="length",width=10,height=7,bg='white',fg='red',command=l)
b2.pack(side=RIGHT)
b3=Button(app,text="mass",width=10,height=7,fg="blue",bg='white', command=mass)
b3.pack(side=RIGHT)
b4=Button(app,text="area",width=10,height=7,fg="violet",bg='white', command=area)
b4.pack(side=RIGHT)
b4=Button(app,text="volume",width=10,height=7,fg="orange",bg='white', command=volume)
b4.pack(side=RIGHT)
b4=Button(app,text="data",width=10,height=7,fg="purple",bg='white', command=data)
b4.pack(side=RIGHT)

root.mainloop()

