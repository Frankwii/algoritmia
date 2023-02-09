import abc
from enum import Enum


class TipoEnchufe(Enum):
    A = 0
    B = 1
    C = 2


class Aparcamiento:
    """Cada objeto de la clase Aparcamiento ºes, en esencia, una lista de objetos Planta"""

    listaAparcamientos = []

    @staticmethod
    def killaparcamientoindice(idx=0):
        Aparcamiento.listaAparcamientos.pop(idx)

    @staticmethod
    def killaparcamientonombre(nombre):
        Aparcamiento.listaAparcamientos.remove(nombre)

    @staticmethod
    def plazastotales():
        res = 0
        for aparcamiento in Aparcamiento.listaAparcamientos:
            res += aparcamiento.plazasTotales
        return res

    @staticmethod
    def plazaslibresporaparcamiento():
        return [aparcamiento.plazasLibres for aparcamiento in Aparcamiento.listaAparcamientos] # list comprehensions rock

    @staticmethod
    def plazaslibrestotales():
        return sum(Aparcamiento.plazaslibresporaparcamiento())

    def __init__(self, listaPlantas):

        self.listaPlantas = listaPlantas

        plazasLibres = 0
        plazasOcupadas = 0

        for planta in self.listaPlantas:
            plazasLibres += planta.plazasLibres
            plazasOcupadas += planta.plazasOcupadas

        self.plazasOcupadas = plazasOcupadas
        self.plazasLibres = plazasLibres
        self.plazasTotales = plazasLibres + plazasOcupadas
        Aparcamiento.listaAparcamientos.append(self)

    def getplazas(self):
        plazasLibres = 0
        plazasOcupadas = 0

        for planta in self.listaPlantas:
            plazasLibres += planta.plazasLibres
            plazasOcupadas += planta.plazasOcupadas

        self.plazasOcupadas = plazasOcupadas
        self.plazasLibres = plazasLibres
        self.plazasTotales = plazasLibres + plazasOcupadas

    def aparcarcoche(self, idxplanta, nplaza, coche):
        boolean = self.listaPlantas[idxplanta].aparcarcoche(nplaza, coche)
        if boolean:
            self.plazasLibres -= 1
            self.plazasOcupadas += 1

    def sacarcoche(self, idxplanta, nplaza):
        boolean = self.listaPlantas[idxplanta].sacarcoche(nplaza)
        if boolean:
            self.plazasLibres += 1
            self.plazasOcupadas -= 1


class Planta:
    """Cada objeto de la clase Planta es esencialmente una lista. Los elementos de esta lista son objetos
    Coche si hay un coche aparcado y None en caso contrario."""

    def __init__(self, listaPlazas=None):
        if listaPlazas is None:
            listaPlazas = []

        self.listaPlazas = listaPlazas
        self.plazasOcupadas = 0
        self.plazasLibres = 0
        self.listaCoches = []

        i = 0
        for coche in self.listaPlazas:
            i += 1
            if not (coche is None):
                self.listaCoches.append((coche, i))
                self.plazasOcupadas += 1
            else:
                self.plazasLibres += 1

        self.plazasTotales = self.plazasLibres + self.plazasOcupadas

    def plazaocupada(self, nplaza):
        if self.listaPlazas[nplaza] is None:
            return False
        else:
            return True

    def aparcarcoche(self, nplaza, coche):
        if self.plazaocupada(nplaza):
            return False  # Control de errores: si no se ha podido ejecutar devuelve False; True en caso contrario
        else:
            coche.aparcar()
            self.listaPlazas[nplaza] = coche
            self.plazasLibres -= 1
            self.plazasOcupadas += 1
            return True

    def sacarcoche(self, nplaza):

        if self.plazaocupada(nplaza):
            self.listaPlazas[nplaza].arrancar()  # self.listaPlazas[nplaza] es el coche aparcado alli
            self.listaPlazas[nplaza] = None
            self.plazasLibres += 1
            self.plazasOcupadas -= 1
            return True

        else:
            return False


class Coche(metaclass=abc.ABCMeta):
    __listaCoches = []
    __listaCochesCirculacion = []
    __listaCochesAparcados = []

    @staticmethod
    def killcocheindice(idx=0):
        Coche.__listaCoches.pop(idx)

    @staticmethod
    def killcochenombre(nombre):
        Coche.__listaCoches.remove(nombre)

    @staticmethod
    def cochesmaspotente():
        """Devuelve una lista con los coches que tengan potencia maxima"""
        if len(Coche.__listaCoches) == 0:
            return None
        potenciamax = 0
        cochesmax = []
        for coche in Coche.__listaCoches:
            if coche.potencia == potenciamax:
                cochesmax.append(coche)
            elif coche.potencia > potenciamax:
                cochesmax = [coche] # "reiniciamos" la lista para que solo contenga el maximo; si luego encontramos otro igual se añadira
            potenciamax = cochesmax[0].potencia
        return cochesmax

    @staticmethod
    def getlistacoches():
        return Coche.__listaCoches

    @staticmethod
    def getlistacochescirculacion():
        return Coche.__listaCochesCirculacion

    @staticmethod
    def getlistacochesaparcados():
        return Coche.__listaCochesAparcados

    @staticmethod
    def potenciatotalencirculacion():
        """Calcula la suma de las potencias de todos los coches en circulacion"""
        res = 0
        for coche in Coche.__listaCochesCirculacion:
            res += coche.potencia
        return res

    @staticmethod
    def mediaaparcados():
        media = 0
        for coche in Coche.getlistacochesaparcados():
            media += coche.potencia

        return media / len(Coche.getlistacochesaparcados())

    @staticmethod
    def varianzaaparcados():
        var = 0
        E = Coche.mediaaparcados()
        for coche in Coche.getlistacochesaparcados():
            var += (coche.potencia - E) ** 2

        return var / len(Coche.getlistacochesaparcados())

    @staticmethod
    def mediacirculacion():
        media = 0
        for coche in Coche.getlistacochescirculacion():
            media += coche.potencia

        return media / len(Coche.getlistacochescirculacion())

    @staticmethod
    def varianzacirculacion():
        var = 0
        E = Coche.mediacirculacion()
        for coche in Coche.getlistacochescirculacion():
            var += (coche.potencia - E) ** 2

        return var / len(Coche.getlistacochescirculacion())

    @staticmethod
    def conteotiposdecoche():
        """Cuenta el numero de coches de cada tipo que hay y devuelve una lista [nºgas,nºdie,nºhib,nºele]"""
        gas = die = hib = ele = 0

        for coche in Coche.getlistacoches():
            if isinstance(coche, CocheGasolina):
                gas += 1
            elif isinstance(coche, CocheDiesel):
                die += 1
            elif isinstance(coche, CocheHibrido):
                hib += 1
            elif isinstance(coche, CocheElectrico):
                ele += 1

        return [gas, die, hib, ele]

    def __init__(self, color="blanco", potencia=0, marca="FIAT", modelo="500", matricula="AAA0000"):
        self.color = color
        self.potencia = potencia
        self.marca = marca
        self.modelo = modelo
        self.matricula = matricula
        self.__circula = True  # Por defecto, al inicializar un coche, este estara siempre circulando
        Coche.__listaCoches.append(self)
        if self.__circula:
            Coche.__listaCochesCirculacion.append(self)
        else:
            Coche.__listaCochesAparcados.append(self)

    def aparcar(self):
        self.__circula = False
        Coche.__listaCochesCirculacion.remove(self)
        Coche.__listaCochesAparcados.append(self)

    def arrancar(self):
        self.__circula = True
        Coche.__listaCochesAparcados.remove(self)
        Coche.__listaCochesCirculacion.append(self)

    def getcircula(self):
        return self.__circula

    def __str__(self):
        return self.matricula

    def __repr__(self):
        return self.matricula


class CocheHibrido(Coche):

    def __init__(self, color="blanco", potencia=0, marca="FIAT", modelo="500", matricula="AAA0000",
                 capacidadBateria=0):
        super().__init__(color, potencia, marca, modelo, matricula)
        self.capacidadBateria = capacidadBateria


class CocheElectrico(Coche):

    def __init__(self, color="blanco", potencia=0, marca="FIAT", modelo="500", matricula="AAA0000",
                 capacidadBateria=0, tipoEnchufe=TipoEnchufe.A):
        super().__init__(color, potencia, marca, modelo, matricula)
        self.capacidadBateria = capacidadBateria
        self.tipoEnchufe = tipoEnchufe


class CocheGasolina(Coche):
    pass


class CocheDiesel(Coche):
    pass
