import tkinter
import nmap
import csv

#'148.234.5.206'

def pin():
    text2 = cajatexto.get()
    print("Espere un momento.....")
    print("Los puertos son: ")
    host = text2
    begin = 78
    end = 80
    target = host
    scan= nmap.PortScanner()

    for i in range(begin,end+1):
        res = scan.scan(target,str(i))
        res = res['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {res}.')
        print("Complete...................")

ventana = tkinter.Tk()
ventana.geometry("400x300")
presentacion = tkinter.Label(ventana, text = "Python con interfaz grafica")
presentacion.pack()

cajatexto = tkinter.Entry(ventana, font = "25")
cajatexto.pack()
cartel =  tkinter.Label(ventana, text = "Hola Ingresa tu ip: ")
cartel.pack()
boton1 = tkinter.Button(ventana, text ="Responder", command = pin)
boton1.pack()
abierta = pin 

ventana.mainloop()
