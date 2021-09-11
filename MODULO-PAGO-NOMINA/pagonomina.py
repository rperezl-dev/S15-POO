from datetime import date


class Empleado:
    contadorId = 0

    def __init__(self, nomb="", suel=0, direc="", ced="", telefono="", fecha_ingr=0):
        self.__id = Empleado.contadorId
        self.nombre = nomb
        self.sueldo = suel
        self.dirección = direc
        self.cedula = ced
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingr
        Empleado.contadorId += 1
        # PagoHora=self.sueldo/self.horas

    def mostrarEmpleado(self):
        print(" Nombre= {:20} Sueldo:$ {}\n Direccion: {:17} Cedula {}\n Telefono: {:18} Fecha de Ingreso:{}\n".format(
            self.nombre, self.sueldo, self.dirección, self.cedula, self.telefono, self.fecha_ingreso))


class Administrativo(Empleado):
    def __init__(self, nomb="", suel=0, direc="", ced="", telefono="", fecha_ingr=0, comision=False):
        super().__init__(nomb, suel, direc, ced, telefono, fecha_ingr)
        self.comision = comision

    def mostrarAdministrativo(self):
        print(" Comision={}".format(self.comision))


class Obrero(Empleado):
    def __init__(self, nomb="", suel=0, direc="", ced="", telefono="", fecha_ingr=0, sindicato=False,
                 contratocol=False):
        super().__init__(nomb, suel, direc, ced, telefono, fecha_ingr)
        self.sindicato = sindicato
        self.contratoColectivo = contratocol

    def mostrarObrero(self):
        print("Sindicato={:10} Contrato colectivo= {}".format(self.sindicato, self.contratoColectivo))


class Departamento:
    contadorId = 0

    def __init__(self, empl="", desc=""):
        self.__id = Departamento.contadorId
        self.empleado = empl
        self.descripcion = desc
        Departamento.contadorId += 1

    def mostrarDepartamento(self):
        print(" Id:{}\n Descripcion: {} ".format(self.__id, self.descripcion))


class Empresa:
    contadorId = 0

    def __init__(self, empleado='', nomb="", ruc="", direccion="", telefono="", razonso="", depart=""):
        self.__id = Empresa.contadorId
        self.departamento = Departamento(empleado, depart)
        self.empleado = empleado
        self.nombre = nomb
        self.ruc = ruc
        self.direccion = direccion
        self.telefono = telefono
        self.razonSocial = razonso
        Empresa.contadorId += 1

    def mostrarEmpresa(self):
        print(" Id:{}\n Nombre:{}\n Ruc:{:23}  Direccion: {}\n Telefono: {:18} Razon Social: {}".format(self.__id,
                                                                                                        self.nombre,
                                                                                                        self.ruc,
                                                                                                        self.direccion,
                                                                                                        self.telefono,
                                                                                                        self.razonSocial))


class SobreTiempo:
    contadorId = 0

    def __init__(self, Horarecargo=0, Horaext=0, empleado='', fecha="", estado=False):
        self.__id = SobreTiempo.contadorId
        self.Horarecargo = Horarecargo
        self.Horaextra = Horaext
        self.empleado = empleado
        self.fecha = fecha
        self.estado = estado
        SobreTiempo.contadorId += 1

    def calcSobretiempo(self, sueldo=0, horaRec=0, horaExtr=0):
        valor_hora = sueldo / 240
        calculos = valor_hora * (horaRec * 0.5 + horaExtr * 2)
        return round(calculos, 2)

    def mostrarSobreTiempo(self):
        print(" Id:{}\n Horas recargo{}\n Horas extras:{}\n Fecha:{}\n estado: {}".format(self.__id, self.Horarecargo,
                                                                                          self.Horaextra, self.fecha,
                                                                                          self.estado))


class Prestamo:
    ContadorId = 0

    def __init__(self, fecha="", valorpres=0, numpagos=0, empleado='', estado=False):
        self.__id = Prestamo.ContadorId
        self.fecha = fecha
        self.valorprest = valorpres
        self.numpagos = numpagos
        self.empleado = empleado
        self.cuotas = self.calcCuota()  # Llamo al metodo para obtener valor del calculo.
        self.saldo = round((self.numpagos * self.cuotas), 2)
        self.estado = estado

        Prestamo.ContadorId += 1

    def calcCuota(self):
        if self.numpagos != 0:
            return round((self.valorprest / self.numpagos), 2)
        else:
            return 0

    def mostrarPrestamo(self):
        print(
            " Id:{}\n Fecha:{}\n Valor de prestamo: $ {}\n Numero de pagos:{}\n Cuotas de:$ {}\n Saldo:{}\n Estado:{}\n".format(
                self.__id, self.fecha, self.valorprest, self.numpagos, self.cuotas, self.saldo, self.estado))


class Deducciones:
    def __init__(self, iess=0, comision=0, antiguedad=0, ):
        self.iessempleado = iess
        # iess=self.iessempleado*(suel+hextra)

        self.comision = comision
        # comision*suel
        self.antiguedad = antiguedad
        # self.antiguedad(Fechaingreso - Fechaactual)/365*sueldo

    def calcComisEmpOfic(self, sueld=0):
        return round((self.comision * sueld), 2)

    def calcAntigEmpObre(self, fechNom=0, fechIngr=0, sueld=0):
        calcFechas = (fechNom - fechIngr).days
        calcFechas += 1
        calculo = self.antiguedad * calcFechas / 365 * sueld
        return round(calculo, 2)

    def iessEmpleado(self, sueld=0, sobretiempo=0):
        calculo = self.iessempleado * (sueld + sobretiempo)
        return round(calculo, 2)

    def mostrarDeducciones(self):
        print(" Aporte al Iess: %{}".format(self.iessempleado))
        print(" Comision: %{}\n Antiguedad: %{}".format(self.comision, self.antiguedad))


class Nomina:
    contadorId = 0

    def __init__(self, nombEmp="", empleado='', fecha="", sobretiempo='', comision=0, anti=0, iess=0, prestamo='',
                 ded=''):
        self.__id = Nomina.contadorId
        self.nombreEmpresa = nombEmp
        self.empleado = empleado
        self.deducciones = ded
        self.fecha = fecha
        self.sueldo = self.empleado.sueldo
        self.sobretiempo = sobretiempo
        self.comision = comision
        self.antiguedad = anti
        self.iess = iess
        self.prestamo = prestamo

        self.totalSobretiempo = self.sobretiempo.calcSobretiempo(self.sueldo, self.sobretiempo.Horarecargo,
                                                                 self.sobretiempo.Horaextra)
        self.comisEmplOfic = self.deducciones.calcComisEmpOfic(self.sueldo)
        self.anitgEmpObrero = self.deducciones.calcAntigEmpObre(self.fecha, self.empleado.fecha_ingreso, self.sueldo)
        self.iessEmpleado = self.deducciones.iessEmpleado(self.sueldo, self.totalSobretiempo)
        self.prestamoEmpleado = self.prestamo.cuotas
        self.totalIngreso = self.sueldo + self.totalSobretiempo + self.comisEmplOfic + self.anitgEmpObrero
        self.totDes = self.iessEmpleado + self.prestamoEmpleado
        self.liquidoRecibir = self.totalIngreso - self.totDes
        Nomina.contadorId += 1

    def mostrarNomina(self):
        print(
            " Id:{}\n fecha:{}\n sueldo:{}\n sobretiempo:{}\n comisionEmpOfic:{}\n antigEmpObrero:{}\n iessEmple:{}\n prestamoEmpl:{}\n totalIngreso:{}\n totalDescuento:{}\n liquidoRecibir:{}\n".format(
                self.__id, self.fecha,
                self.sueldo, self.totalSobretiempo, self.comisEmplOfic, self.anitgEmpObrero, self.iessEmpleado,
                self.prestamoEmpleado, self.totalIngreso, self.totDes, self.liquidoRecibir))


emplea = Administrativo("Ana Lopez", 730.67, "Milagro", "1207845691", "042721089", date(2019, 4, 1), True)
# emplea=Obrero("Luis Lopez",530.67,"Guayaquil","9045786274", "042758489", date(2019, 4, 1),False, False)
emp = Empresa(emplea, "Devies", "023746273645243", "Duran", "09384735466", "Mejorar empleo", "Administrativo")
sob = SobreTiempo(3, 2, emplea, date(2019, 4, 19), True)
pre = Prestamo(date(2019, 4, 25), 2000.50, 24, emplea, True)
ded = Deducciones(0.0945, 0.034, 0.2)
nom = Nomina(emp.nombre, emplea, date(2019, 4, 30), sob, ded.comision, ded.antiguedad, ded.iessempleado, pre, ded)

emp.mostrarEmpresa()
print()
emp.departamento.mostrarDepartamento()
print()
emplea.mostrarEmpleado()
print()
emplea.mostrarAdministrativo()
# emplea.mostrarObrero()
print()
sob.mostrarSobreTiempo()
print()
pre.mostrarPrestamo()
print()
ded.mostrarDeducciones()
print()
nom.mostrarNomina()