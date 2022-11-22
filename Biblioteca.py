from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

import datetime
tiempo =datetime.datetime.now()
#print(tiempo)

hora = datetime.datetime.now().hour
minu = datetime.datetime.now().minute
seg = datetime.datetime.now().second

listalibro=[]
listaautor=[]

print(" BIBLIOTECA OXFOR \n    Bienvenido ")
class Usuario:
    print( "\nIngrese los siguientes datos \n ")
    def __init__(self):
        self.nombre = input("ingrese su nombre: ")
        self.apellido = input("ingrese su apellido: ")
        self.edad = int(input("ingrese su edad: "))
        self.cedula = int(input("ingrese su cedula: "))
        self.direccion = input("Ingrese su direccion: ")

    def mostrar(self):
        print(self.nombre, self.apellido, self.edad, self.cedula)

class Libro:
    #print("\n En que libro esta interesado? \n")
    def __init__(self):
        print("\n En que libro esta interesado? \n")
        self.titulo = input("Digite el Titulo del libro: ")
        self.autor = input("Digite el nombre del autor: ")

    def mos(self):
        print("\tTitulo: ",self.titulo)

    def ww(self):
        print("\tAutor: ",self.autor)


class Persona(Libro,Usuario):
    def __init__(self):
        self.__ISBN = ""
        self.__Paginas = ""
        self.__Edicion = ""
        self.__Editorial = ""
        self.__Ciudad = ""
        self.__Pais = ""

    def GetISBN(self):
        return self.__ISBN

    def SetISBN(self, isbn):
        self.__ISBN = isbn

    def GetPaginas(self):
        return self.__Paginas

    def SetPaginas(self, paginas):
        self.__Paginas = paginas

    def GetEdicion(self):
        return self.__Edicion

    def SetEdicion(self, edicion):
        self.__Edicion = edicion

    def GetEditorial(self):
        return self.__Editorial

    def SetEditorial(self, editorial):
        self.__Editorial = editorial

    def GetCiudad(self):
        return self.__Ciudad

    def SetCiudad(self, ciudad):
        self.__Ciudad = ciudad

    def GetPais(self):
        return self.__Pais

    def SetPais(self, pais):
        self.__Pais = pais
    
    def Mostrarr(self):
        
        f=Libro()
        print("Informe: ")
        f.mos()
        #print("Titulo: ",self.titulo)
        print("\t", self.GetEdicion())
        f.ww()
        print("\tISBN: ", self.GetISBN())
        print("\tCiudad: ", self.GetCiudad())
        print("\tPais: ", self.GetPais())
        print("\tEditorial: ", self.GetEditorial())
        print("\tPaginas: ", self.GetPaginas())


class Fecha(Persona,Libro,Usuario):
    def __init__(self):
        self.__Dia = ""
        self.__Mes = ""
        self.__Año = ""

    def GetDia(self):
        return self.__Dia

    def SetDia(self, dia):
        self.__Dia = dia

    def GetMes(self):
        return self.__Mes

    def SetMes(self, mes):
        self.__Mes = mes

    def GetAño(self):
        return self.__Año

    def SetAño(self, año):
        self.__Año = año

    def Mo(self):
        print("\tFecha: ",self.GetDia(),self.GetMes(),self.GetAño())
        print ("")
        #print("\tPaginas: ", self.GetPaginas())

usu=Usuario()

#li=Libro() 

persona=Persona()
persona.SetISBN("  0-13-031997-X")
persona.SetPaginas(" 784 páginas ")
persona.SetEdicion(" 3a. edición ")
persona.SetEditorial("Reyes,Bogota-D.C")
persona.SetCiudad("Prentice-Hall")
persona.SetPais("New Jersey (USA)")
persona.Mostrarr()

fecha=Fecha()
fecha.SetDia("13")
fecha.SetMes("Noviembre")
fecha.SetAño("2005")
fecha.Mo()

class Prestar(Fecha):
    while True:
        op=int(input("Desea prestar algun libro: \n\t1=SI \n\t2=NO\n"))
        if op == 1:
            v=int(input("\nCuantos libros desea prestar?\n "))
            print (v)
            for i in range(v):
                li=input("Digite el nombre del libro: ")
                ti=input("Digite el autor del libro: ")
                listalibro.append(li)
                listaautor.append(ti)
                print(listalibro)
                print(listaautor)

            print("\nDebes regresar lo prestado en 3 meses\n")
            #print("Fecha: {}/{}/{}".format(tiempo.day,tiempo.month,tiempo.year))
            #print("Hora: {}:{}:{}".format(tiempo.hour,tiempo.minute,tiempo.second))

            ahora = datetime.datetime.utcnow()
            tomorrow = ahora + datetime.timedelta(days=90)
            
            print("\tFecha de entrega: {}/{}/{}".format(ahora.day,ahora.month,ahora.year))
            print("\tFecha de devolucion: {}/{}/{}".format(tomorrow.day,tomorrow.month,tomorrow.year))
            for todo in listalibro:
                print("\tLibro: ",todo)
            print("\nSi te pasas de la fecha estipulada se cobrara una multa de 50.000$\n")
            

                
        else:
            print("Imprimiendo su recibo...")
            break

    def Qr(self):
        w, h = letter
        c = canvas.Canvas("factu.pdf", pagesize=letter)
        c.setFont("Helvetica",12)
        c.drawString(190,h-10," BIBLIOTECA OXFOR")
        c.drawString(187,h-25,"  NIT: 3234567-5")
        c.drawString(147,h-40,"-------------------------")
        c.drawString(167,h-55,"  Agente Retenedor de ICA")
        c.drawString(180,h-70,"  TEL:  3142769220")
        c.drawString(180,h-85,"Biblioteca_Oxfor.com.co")
        c.drawString(157,h-100,"  NEIVA HUILA ")
        c.drawString(158,h-115,"      DG 23 65 18 LC 123")

        c.save()
    


prestar=Prestar()
prestar.Qr()
 



