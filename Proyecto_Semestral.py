import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import make_interp_spline
from matplotlib import pyplot as plt
from scipy import signal
import tkinter
from tkinter import*

OPTIONS = [
"Chile",
"Mexico",
"El Salvador",
"Canada",
"Peru"
] #etc

root=Tk()
root.title("Contagio de VIH por pais")
root.geometry('350x100')
root.config(bg="azure")

variable = StringVar(root)
variable.set("Seleccione una opcion") # default value

w = OptionMenu(root, variable, *OPTIONS)
w.pack()


ch=0
ci=0
ca=0
ce=0
cu=0
def validar():
  #en los if dices que tomas el valor global de la variable que esta en la otra funcion
  global ch
  global ci
  global ca
  global ce
  global cu
  

#para estos if lo que hace esque entra en la funcion y se condiciona para que solo lo haga una vez y no este abriendo varias ventanas

  if ((variable.get()=='Chile')and(ch==0)):
#Aqui aplicamos el plt.close para cerrar el plt en caso de estar abierto, si no lo esta, igual el programa correo normal     
        plt.close()
        primero()

  elif ch==1:
             global otra_ventana
             
             

            
  if ((variable.get()=='Mexico')and(ci==0)):
         plt.close()
         segundo()
         
  elif ci==1:
             global otra_ventana2
     
                   
          
  if ((variable.get()=='El Salvador')and(ca==0)):
         plt.close()
         tercero()

  elif ca==1:
             global otra_ventana3
     
            
          
  if ((variable.get()=='Canada')and(ce==0)):
         plt.close()
         cuarto()

  elif ce==1:
             global otra_ventana4
     
                      
          
  if ((variable.get()=='Peru')and(cu==0)):
         plt.close()
         quinto()    
        
  elif cu==1:
             global otra_ventana5
     
             
          
def primero():



    global otra_ventana
    otra_ventana = tkinter.Toplevel(root)
    otra_ventana.title("Contagio de VIH en Chile")
    otra_ventana.geometry('650x600')
    otra_ventana.config(bg="azure")
    global ch
    ch= ch+1
    
    lbl1 = Label(otra_ventana,fg="red",bg="azure")
    lbl2 = Label(otra_ventana,fg="blue",bg="azure")
    lbl3 = Label(otra_ventana,fg="green",bg="azure")
    lbl4 = Label(otra_ventana,fg="black",bg="azure")
    lbl5 = Label(otra_ventana,fg="black",bg="azure")
    lbl6 = Label(otra_ventana,fg="black",bg="azure")
    lbl7 = Label(otra_ventana,fg="orangered2",bg="azure")
    lbl8 = Label(otra_ventana,fg="orangered2",bg="azure")


    
    lbl1.configure(text=data)
    lbl2.configure(text=x)
    lbl3.configure(text=y)
    lbl4.configure(text=text1)
    lbl5.configure(text=text2)
    lbl6.configure(text=text3)


    plt.plot(x,y)
    plt.ylabel('Casos de Contagio')
    plt.xlabel('Años')
    plt.show
    
    coeficientes=np.polyfit(x,y,1)
    polinomio=np.poly1d(coeficientes)
    poli= str(polinomio)
    f=interp1d(y,x,1)
    
    
    lbl7.configure(text="Polinomio que describe la ecuacion="+poli)
    lbl8.configure(text="Resultado de interpolacion implementada con 5,200 en y, da como resultado en x= " +"\n"+str(f(5200)))
    
    lbl1.grid(column=100, row=300)
    lbl2.grid(column=100, row=700)
    lbl3.grid(column=100, row=1200)
    lbl4.grid(column=100, row=10)
    lbl5.grid(column=100, row=490)
    lbl6.grid(column=100, row=900)
    lbl7.grid(column=100, row=1500)
    lbl8.grid(column=100, row=1700)

   
    
    T=np.array(x)
    power=np.array(y)
    xnew = np.linspace(T.min(),T.max(),300) 
    spl = make_interp_spline(T, power, k=3)
    power_smooth = spl(xnew)
    plt.plot(xnew,power_smooth) 
    plt.title("VIH-CHILE")
    plt.show()
    
    

def segundo():

   
    global otra_ventana2
    otra_ventana2 = tkinter.Toplevel(root)
    otra_ventana2.title("Contagio de VIH en Mexico")
    otra_ventana2.geometry('650x600')
    otra_ventana2.config(bg="azure")
    global ci
    ci= ci+1
    
    var1 = Label(otra_ventana2,fg="red",bg="azure")
    var2 = Label(otra_ventana2,fg="blue",bg="azure")
    var3 = Label(otra_ventana2,fg="green",bg="azure")
    var4 = Label(otra_ventana2,fg="black",bg="azure")
    var5 = Label(otra_ventana2,fg="black",bg="azure")
    var6 = Label(otra_ventana2,fg="black",bg="azure")
    var7 = Label(otra_ventana2,fg="orangered2",bg="azure")
    var8 = Label(otra_ventana2,fg="orangered2",bg="azure")


    
    var1.configure(text=data2)
    var2.configure(text=j)
    var3.configure(text=i)
    var4.configure(text=text1)
    var5.configure(text=text2)
    var6.configure(text=text3)


    plt.plot(j,i)
    plt.ylabel('Casos de Contagio')
    plt.xlabel('Años')
    plt.show
    
    coeficientes2=np.polyfit(j,i,1)
    polinomio2=np.poly1d(coeficientes2)
    poli2= str(polinomio2)
    f2=interp1d(i,j,1)


    
    var7.configure(text="Polinomio que describe la ecuacion="+poli2)
    var8.configure(text="Resultado de interpolacion implementada con 8,000 en y, da como resultado en x= " +"\n"+str(f2(8000)))
    
    var1.grid(column=100, row=300)
    var2.grid(column=100, row=700)
    var3.grid(column=100, row=1200)
    var4.grid(column=100, row=10)
    var5.grid(column=100, row=490)
    var6.grid(column=100, row=900)
    var7.grid(column=100, row=1500)
    var8.grid(column=100, row=1600)

      
    T2=np.array(j)
    power2=np.array(i)
    xnew2 = np.linspace(T2.min(),T2.max(),300) 
    spl2 = make_interp_spline(T2, power2, k=3)
    power_smooth2 = spl2(xnew2)
    plt.plot(xnew2,power_smooth2) 
    plt.title("VIH-MEXICO")
    plt.show()
    

def tercero():

    global otra_ventana3
    otra_ventana3 = tkinter.Toplevel(root)
    otra_ventana3.title("Contagio de VIH en El Salvador")
    otra_ventana3.geometry('650x600')
    otra_ventana3.config(bg="azure")
    global ca
    ca= ca+1
    
    vari1 = Label(otra_ventana3,fg="red",bg="azure")
    vari2 = Label(otra_ventana3,fg="blue",bg="azure")
    vari3 = Label(otra_ventana3,fg="green",bg="azure")
    vari4 = Label(otra_ventana3,fg="black",bg="azure")
    vari5 = Label(otra_ventana3,fg="black",bg="azure")
    vari6 = Label(otra_ventana3,fg="black",bg="azure")
    vari7 = Label(otra_ventana3,fg="orangered2",bg="azure")
    vari8 = Label(otra_ventana3,fg="orangered2",bg="azure")


    
    vari1.configure(text=data3)
    vari2.configure(text=a)
    vari3.configure(text=b)
    vari4.configure(text=text1)
    vari5.configure(text=text2)
    vari6.configure(text=text3)


    
    plt.plot(a,b)
    plt.ylabel('Casos de Contagio')
    plt.xlabel('Años')
    plt.show

#polinomio que describe la grafica de forma lineal
    
    coeficientes3=np.polyfit(a,b,1)
    polinomio3=np.poly1d(coeficientes3)
    poli3= str(polinomio3)
    f3=interp1d(b,a,1)


    
    vari7.configure(text="Polinomio que describe la ecuacion="+poli3)
    
#Aqui lo que se muestra esque cuando es f3(5200) debe dar en el eje de las y el valor que corresponde
    vari8.configure(text="Resultado de interpolacion implementada con 1,223 en y, da como resultado en x= " +"\n"+str(f3(1223)))
    
    vari1.grid(column=100, row=300)
    vari2.grid(column=100, row=700)
    vari3.grid(column=100, row=1200)
    vari4.grid(column=100, row=10)
    vari5.grid(column=100, row=490)
    vari6.grid(column=100, row=900)
    vari7.grid(column=100, row=1500)
    vari8.grid(column=100, row=1600)

      
    T3=np.array(a)
    power3=np.array(b)
    xnew3 = np.linspace(T3.min(),T3.max(),300) 
    spl3 = make_interp_spline(T3, power3, k=3)
    power_smooth3 = spl3(xnew3)
    plt.plot(xnew3,power_smooth3) 
    plt.title("VIH-EL SALVADOR")
    plt.show()

   


def cuarto():

    global otra_ventana4
    otra_ventana4 = tkinter.Toplevel(root)
    otra_ventana4.title("Contagio de VIH en Canada")
    otra_ventana4.geometry('650x600')
    otra_ventana4.config(bg="azure")
    global ce
    ce= ce+1
    
    varia1 = Label(otra_ventana4,fg="red",bg="azure")
    varia2 = Label(otra_ventana4,fg="blue",bg="azure")
    varia3 = Label(otra_ventana4,fg="green",bg="azure")
    varia4 = Label(otra_ventana4,fg="black",bg="azure")
    varia5 = Label(otra_ventana4,fg="black",bg="azure")
    varia6 = Label(otra_ventana4,fg="black",bg="azure")
    varia7 = Label(otra_ventana4,fg="orangered2",bg="azure")
    varia8 = Label(otra_ventana4,fg="orangered2",bg="azure")


    
    varia1.configure(text=data4)
    varia2.configure(text=h)
    varia3.configure(text=m)
    varia4.configure(text=text1)
    varia5.configure(text=text2)
    varia6.configure(text=text3)


    plt.plot(h,m)
    plt.ylabel('Casos de Contagio')
    plt.xlabel('Años')
    plt.show

    coeficientes4=np.polyfit(h,m,1)
    polinomio4=np.poly1d(coeficientes4)
    poli4= str(polinomio4)
    f4=interp1d(m,h,1)


    
    varia7.configure(text="Polinomio que describe la ecuacion="+poli4)

    varia8.configure(text="Resultado de interpolacion implementada con 2,561 en y, da como resultado en x= " +"\n"+str(f4(2561)))
    
    varia1.grid(column=100, row=300)
    varia2.grid(column=100, row=700)
    varia3.grid(column=100, row=1200)
    varia4.grid(column=100, row=10)
    varia5.grid(column=100, row=490)
    varia6.grid(column=100, row=900)
    varia7.grid(column=100, row=1500)
    varia8.grid(column=100, row=1600)

      
    T4=np.array(h)
    power4=np.array(m)
    xnew4 = np.linspace(T4.min(),T4.max(),300) 
    spl4 = make_interp_spline(T4, power4, k=3)
    power_smooth4 = spl4(xnew4)
    plt.plot(xnew4,power_smooth4) 
    plt.title("VIH-CANADA")
    plt.show()
   

def quinto():

    global otra_ventana5
    otra_ventana5 = tkinter.Toplevel(root)
    otra_ventana5.title("Contagio de VIH en Peru")
    otra_ventana5.geometry('650x600')
    otra_ventana5.config(bg="azure")
    global cu
    cu= cu+1

    
    variab1 = Label(otra_ventana5,fg="red",bg="azure")
    variab2 = Label(otra_ventana5,fg="blue",bg="azure")
    variab3 = Label(otra_ventana5,fg="green",bg="azure")
    variab4 = Label(otra_ventana5,fg="black",bg="azure")
    variab5 = Label(otra_ventana5,fg="black",bg="azure")
    variab6 = Label(otra_ventana5,fg="black",bg="azure")
    variab7 = Label(otra_ventana5,fg="orangered2",bg="azure")
    variab8 = Label(otra_ventana5,fg="orangered2",bg="azure")


    
    variab1.configure(text=data5)
    variab2.configure(text=f)
    variab3.configure(text=g)
    variab4.configure(text=text1)
    variab5.configure(text=text2)
    variab6.configure(text=text3)


    plt.plot(f,g)
    plt.ylabel('Casos de Contagio')
    plt.xlabel('Años')
    plt.show

    coeficientes5=np.polyfit(f,g,1)
    polinomio5=np.poly1d(coeficientes5)
    poli5= str(polinomio5)
    f5=interp1d(g,f,1)


    
    variab7.configure(text="Polinomio que describe la ecuacion="+poli5)

    variab8.configure(text="Resultado de interpolacion implementada con 5,911 en y, da como resultado en x= " +"\n"+str(f5(5911)))
    
    variab1.grid(column=100, row=300)
    variab2.grid(column=100, row=700)
    variab3.grid(column=100, row=1200)
    variab4.grid(column=100, row=10)
    variab5.grid(column=100, row=490)
    variab6.grid(column=100, row=900)
    variab7.grid(column=100, row=1500)
    variab8.grid(column=100, row=1600)

      
    T5=np.array(f)
    power5=np.array(g)
    xnew5 = np.linspace(T5.min(),T5.max(),300) 
    spl5 = make_interp_spline(T5, power5, k=3)
    power_smooth5 = spl5(xnew5)
    plt.plot(xnew5,power_smooth5) 
    plt.title("VIH-PERU")
    plt.show()
  






text1="Data del archivo"
text2="Columna X"
text3="Columna Y"


#Datos para Chile
data=pd.read_csv('C:/Users/stree/Documents/Lic. En Ing. de sistemas y computacion/Topicos Especiales I/Proyecto Semestral/Contagio_Chile.txt',header=1,delim_whitespace=True)
x=data.ix[:,0]
y=data.ix[:,1]


#Datos para Mexico

data2=pd.read_csv('C:/Users/stree/Documents/Lic. En Ing. de sistemas y computacion/Topicos Especiales I/Proyecto Semestral/Contagio_Mexico.txt',header=1,delim_whitespace=True)
j=data2.ix[:,0]
i=data2.ix[:,1]



#Datos para El.Salvador

data3=pd.read_csv('C:/Users/stree/Documents/Lic. En Ing. de sistemas y computacion/Topicos Especiales I/Proyecto Semestral/Contagio_El.Salvador.txt',header=1,delim_whitespace=True)
a=data3.ix[:,0]
b=data3.ix[:,1]


#Datos para Canada

data4=pd.read_csv('C:/Users/stree/Documents/Lic. En Ing. de sistemas y computacion/Topicos Especiales I/Proyecto Semestral/Contagio_Canada.txt',header=1,delim_whitespace=True)
h=data4.ix[:,0]
m=data4.ix[:,1]


#Datos para Peru

data5=pd.read_csv('C:/Users/stree/Documents/Lic. En Ing. de sistemas y computacion/Topicos Especiales I/Proyecto Semestral/Contagio_Peru.txt',header=1,delim_whitespace=True)
f=data5.ix[:,0]
g=data5.ix[:,1]


  

button = Button(root, text="OK", command=validar)

button.pack()



root.mainloop()



