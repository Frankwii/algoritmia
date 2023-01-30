**Problema 1**

Se tiene un tablero de (N+1)x(M+1) casillas en el que solo 
determinadas casillas (conocidas) son transitables. Se empieza en el punto
(0,0) y se quiere llegar al punto (N,M), moviéndose una distancia
<=K cada vez y pasando solo por casillas transitables.
Las casillas (0,0) y (N,M) siempre son transitables.

Cada vez que se llega se elimina una casilla
transitable, en un orden conocido. El problema consiste en determinar
cuál fue la primera casilla transitable que se eliminó
de manera que antes de eliminarla habia camino,
pero después no.

Se lee un fichero con casos de prueba en el que se indican
los parámetros (N,M y K) y las casillas transitables
en el orden en el que se eliminan. Como salida, para cada caso
de prueba se imprimen las coordenadas de la casilla correspondiente.

**Resolución**

Leemos el tablero y colocamos en la entrada (i, j)-ésima de la matriz
un 0 si la casilla no es transitable y un 1 si lo es.

La función *buscar_camino* recibe un tablero y determina si existe algun camino valido entre los puntos
(0, 0) y (N, M). Para hacerlo, se utiliza un algoritmo de búsqueda en profundidad: se sitúa en una casilla transitable (x, y) (la
primera vez, (0, 0)), y mira todas las casillas transitables - que, inicialmente, tienen valor asignado
1 - a distancia no mayor a K. Marca estos puntos con un 2, para no volver a mirarlos despues, y
los añade a una pila. Cuando se centra en un punto, lo elimina de la pila y mira sus vecinos (las
casillas transitables a distancia no mayor a K). Cuando acaba, se centra en el siguiente elemento
de la pila. Si en algun momento llega a la casilla (N, M), para la ejecución y devuelve *True*. Si
la pila se vacía y no ha llegado a (N, M), quiere decir que no hay casillas transitables a las que
se pueda llegar desde el (0, 0) y no se hayan mirado ya; por tanto, no puede llegar a (N, M), y
devuelve *False*. Cuando se ha determinado si había o no un camino, se restablecen los valores
2 a 1. 

El método *busqueda_ultima_transitable* busca, en la lista de las casillas transitables (distintas
de (0, 0) y (N, M)), el índice en esa lista de la casilla transitable que hizo que dejara de haber
camino al ser eliminada. Esta búsqueda se hace de manera dicotómica: se centra en el punto
medio de los extremos y elimina del tablero todas las casillas transitables anteriores al centro.
Después, llama a *buscar_camino*, y descarta la mitad de la lista correspondiente, según si había
o no camino.

Para el programa principal, inicializamos el tablero con las casillas correspondientes, primero todas vacías. A continuación, colocamos casillas transitables donde corresponde. Seguidamente, miramos si hay camino;
si no lo hay, el programa devuelve NUNCA SE PUDO, mientras que si existe el camino, llama a
*busqueda_ultima_transitable*, y devuelve las coordenadas de la casilla correspondiente. Por tanto, el programa tiene
el mismo coste que *busqueda_ultima_transitable*.

**Coste computacional**

El método *buscar_camino* tiene un coste computacional de O(n), donde n es el número de casillas transitables,
pues como mucho se centra una vez en cada casilla transitable.

En el método *busqueda_ultima_transitable*, el número de veces que nos centramos en
una casilla es de orden O(log(n)), y comprobar si había camino tiene un coste de O(n).
Por tanto, esta función (y por ende el programa principal) tiene un coste de O(nlog(n)).