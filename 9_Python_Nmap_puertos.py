import tkinter
import nmap
import csv

def abierta(pin):
    host = pin
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
etiqueta = tkinter.Label(ventana, text = "Introduce el IP: ", padx = 40, pady = 50)
presentacion.pack(side= tkinter.BOTTOM)
etiqueta.pack()

cajatexto = tkinter.Entry(ventana, font = "25")
cajatexto.pack()

def saludo():
    print("Espera un momento.....")
    cajatexto.get
boton1 = tkinter.Button(ventana, text ="Responder", command = saludo)
boton1.pack()
pin = saludo()
abierta(pin)
ventana.mainloop()


