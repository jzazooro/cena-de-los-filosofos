
import tkinter
import sys
ventana=tkinter.Tk()
canvas=tkinter.Canvas(bg="black", width=800, height=600)
    
canvas.create_rectangle(100, 50, 200, 100, fill="black")
canvas.create_rectangle(25, 125, 125, 175, fill="green")
canvas.create_rectangle(50, 200, 150, 250, fill="blue")
canvas.create_rectangle(275, 175, 175, 225, fill="red")
canvas.create_rectangle(200, 160, 300, 110, fill="pink")
canvas.create_text(150, 75, text="Filosofo 1")
canvas.create_text(75, 150, text="Filosofo 2")
canvas.create_text(100, 225, text="Filosofo 3")
canvas.create_text(225, 200, text="Filosofo 4")
canvas.create_text(250, 135, text="Filosofo 5")
    
canvas.create_rectangle(60, 80, 80, 100, fill="black")
canvas.create_rectangle(20, 200, 40, 220, fill="green")
canvas.create_rectangle(220, 80, 240, 100, fill="blue")
canvas.create_rectangle(290, 180, 310, 200, fill="red")
canvas.create_rectangle(170, 240, 190, 260, fill="pink")
    
canvas.pack()
    
ejecutar=tkinter.Button(canvas, text="Ejecutar")
ejecutar.place(x=100, y=300)
    
salir=tkinter.Button(canvas, text="Salir", command=sys.exit)
salir.place(x=200, y=300)
    
ventana.mainloop
