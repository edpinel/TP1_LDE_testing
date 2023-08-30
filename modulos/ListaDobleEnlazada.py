class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None

    def obtenerDato(self):
        return self.dato

    def obtenerAnterior(self):
        return self.anterior

    def obtenerSiguiente(self):
        return self.siguiente

    def asignarDato(self,nuevodato):
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def asignarAnterior(self,nuevoanterior):
        self.anterior = nuevoanterior

class ListaDoblementeEnlazada():

    def __init__(self):
        self.cabeza = None
        self.largo = 0
        self.cola = None
    
    def __len__(self):
        return self.largo

    def esta_vacia(self): #Devuelve True si la lista está vacía.
        return self.cabeza == None

    def tamanio(self): #Devuelve el número de ítems de la lista.
        return self.largo

    def agregar_al_final(self,item): #Agrega un nuevo ítem al final de la lista.
        nodoRecorrido = self.cabeza #Para recorrer los datos
        nuevoNodo = Nodo (item)
        self.largo += 1 #va antes de agregar el nodo para darle su "espacio"

        if nodoRecorrido==None:
            self.cabeza=nuevoNodo
            self.cola=self.cabeza

        else:
            while nodoRecorrido.siguiente != None :
                nodoRecorrido=nodoRecorrido.siguiente
            
            nodoRecorrido.siguiente=nuevoNodo
            nuevoNodo.anterior=nodoRecorrido
            self.cola=nuevoNodo

    def agregar_al_inicio(self,item): #Agrega un nuevo ítem al inicio de la lista.
        nodoRecorrido = self.cabeza  # Para recorrer los datos
        nuevoNodo = Nodo(item)
        self.largo += 1  # va antes de agregar el nodo para darle su "espacio"

        if nodoRecorrido==None:
            self.cabeza=nuevoNodo
            self.cola=self.cabeza

        else:
            nodoRecorrido.anterior = nuevoNodo
            nuevoNodo.siguiente = nodoRecorrido
            self.cabeza = nuevoNodo


    #La siguiente función agrega un nuevo ítem a la lista en "posicion"."posicion" es un entero que indica la posición en la lista donde se va a insertar el nuevo elemento. Si la posición no se pasa como argumento, el ítem debe añadirse al final de la lista.
    def insertar(self, item, posicion=None):
        nuevoNodo = Nodo(item) #Creamos un nuevo objeto de tipo Nodo con el elemento proporcionado y lo almacenamos en la variable nuevoNodo.

        #if nodoRecorrido==None:
            #self.cabeza=nuevoNodo
            #posicion=1

        if posicion is None or posicion >= self.largo: #Aquí verificamos si no se proporciona una posición o si la posición proporcionada está fuera del rango actual de la lista.
            self.agregar_al_final(item)  # Agregar al final si no se especifica la posición o si está fuera de rango
            return

        nodoRecorrido = self.cabeza #Inicializamos el nodo de recorrido con el "nodo cabeza"
        posicion_actual = 0 #Inicializamos una variable para realizar un seguimiento de la posición actual mientras recorremos la lista.

        while posicion_actual < posicion: #Usamos un bucle while para avanzar en la lista hasta que alcancemos la posición deseada.
            nodoRecorrido = nodoRecorrido.obtenerSiguiente() #Actualizamos el nodo de recorrido al siguiente nodo en la lista.
            posicion_actual += 1

        anterior = nodoRecorrido.obtenerAnterior() #Obtenemos el nodo anterior al nodo de recorrido.

        nuevoNodo.asignarAnterior(anterior) #Asignamos el nodo anterior al nuevo nodo.
        nuevoNodo.asignarSiguiente(nodoRecorrido) #Asignamos el nodo siguiente al nuevo nodo.
        anterior.asignarSiguiente(nuevoNodo) #Actualizamos el enlace del nodo anterior para que apunte al nuevo nodo.
        nodoRecorrido.asignarAnterior(nuevoNodo) #Actualizamos el enlace del nodo de recorrido para que apunte al nuevo nodo.
        self.largo += 1

    def extraer(self,posicion): #elimina y devuelve el ítem en "posición". Si no se indica el parámetro posición, se elimina y devuelve el último elemento de la lista.
        nodoRecorrido=self.cabeza
        
        posicionActual=0

        while(posicion > posicionActual):
            nodoRecorrido=nodoRecorrido.obtenerSiguiente()
            posicionActual+=1

        dato_anterior=nodoRecorrido.anterior
        dato_anterior.siguiente = nodoRecorrido.siguiente

        dato_siguiente=nodoRecorrido.siguiente
        dato_siguiente.anterior = nodoRecorrido.anterior

        nodoAExtraer = nodoRecorrido
        nodoAExtraer.siguiente = None
        nodoAExtraer.anterior = None

        self.largo=self.largo-1

        return nodoAExtraer.dato


    def copiar(self): #Realiza una copia de la lista elemento a elemento y devuelve la copia
        nodoRecorrido = self.cabeza
        listaCopia = ListaDoblementeEnlazada()
        while nodoRecorrido != None:
            nuevoNodo = Nodo(nodoRecorrido.dato)
            listaCopia.agregar_al_final(nuevoNodo.dato)
            nodoRecorrido=nodoRecorrido.obtenerSiguiente()
        return listaCopia
    
    def invertir(self): #Invierte el orden de los elementos de la lista.
        nodoRecorrido = self.cabeza
        posicionInicial = 0

        self.cabeza.anterior=None

        while(posicionInicial<self.largo and nodoRecorrido != None):
            nodoAuxiliar = nodoRecorrido.anterior
            nodoRecorrido.anterior=nodoRecorrido.siguiente
            nodoRecorrido.siguiente=nodoAuxiliar

            posicionInicial+=1
            nodoRecorrido=nodoRecorrido.anterior
    
    def ordenar(self): #Ordena los elementos de la lista de "menor a mayor".

        for _ in range(1,self.largo-1):
            nodoRecorrido = self.cabeza

            while nodoRecorrido is not None and nodoRecorrido.obtenerSiguiente.dato < nodoRecorrido.dato:
                nodoActual=nodoRecorrido
                nodoRecorrido.asignarDato(nodoRecorrido.obtenerSiguiente.dato)

                nodoRecorrido.obtenerSiguiente=nodoActual
    
    def concatenar(self,Lista): #Recibe una lista como argumento y retorna la lista actual con la lista pasada como parámetro concatenada al final de la primera. Esta operación también debe ser posible utilizando el operador de suma ‘+’. Aclaración: No se deben modificar las listas.
        nuevaListaConcatenada = self
        
        nodoaAgregar = Lista.cabeza

        while nodoaAgregar is not None:

            nuevaListaConcatenada.agregar_al_final(nodoaAgregar.obtenerDato())
            nodoaAgregar=nodoaAgregar.obtenerSiguiente()

        return nuevaListaConcatenada
    
    def __add__ (self,Lista):

        nuevaListaConcatenada = self.copiar()
        nuevaListaConcatenada.concatenar(Lista)
        return nuevaListaConcatenada