class calculoDesviacion:
    #precondiciones + postcondiciones de los casos de uso
    #atributos: Encapsulacion
    __numero1 = 0.0
    __numero2 = 0.0
    __numero3 = 0.0
    __numero4 = 0.0
    __numero5 = 0.0
    __promedio = 0.0
    __desviacion = 0.0

    #metodos: 1 metodo por cada caso de uso
    #def nombreCasoUso, parametros (precondiciones separadas con " ,")):

    def calcularPromedio(self,numero1,numero2,numero3,numero4,numero5,promedio):
        self.__numero1 = numero1 
        self.__numero2 = numero2
        self.__numero3 = numero3
        self.__numero4 = numero4
        self.__numero5 = numero5
        self.__promedio = sum([numero1,numero2,numero3,numero4, numero5 / 5])
    def calcularDesviacion(self,numero1,numero2,numero3,numero4,numero5,desviacion):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
        self.__numero4 = numero4
        self.__numero5 = numero5
        self.desviacion = (numero1, numero2, numero3, numero4, numero5 / 4 ** 0.5)