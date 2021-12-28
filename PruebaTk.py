from tkinter import Frame, Tk
ventana0 = Tk()
ventana0.title("Prueba") #titulo de la ventana
ventana0.iconbitmap("C:/Users/edgar/Desktop/RecursosCodigos/IconoPrueba.ico")#Definir el icono de la ventana
ventana0.geometry("720x720")#Tamaño de la ventana
ventana0.config(bg="#F8B9FF")#Color de fondo

pagina=Frame(ventana0, width=400, height=300, background="#ED79FA")
pagina.pack()
pagina2=Frame(ventana0, width=400, height=300, background="#79A6FA")
pagina2.pack()#Muestra la pagina
pagina2.pack_forget#Deja de mostrar la pagina

#Todo el codigo TKinter antes del mainloop
ventana0.mainloop()