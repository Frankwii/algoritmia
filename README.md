*Problema 1*

Se tiene un tablero de (N+1)x(M+1) casillas en el que solo 
determinadas casillas (conocidas) son transitables. Se empieza en el punto
(0,0) y se quiere llegar al punto (N,M), moviendose una distancia
<=K cada vez y pasando solo por casillas transitables.
Las casillas (0,0) y (N,M) siempre son transitables.

Cada vez que se llega se elimina una casilla
transitable, en un orden conocido. El problema consiste en determinar
cual fue la primera casilla transitable que se elimino
de manera que antes de eliminarla habia camino
pero despues no.

Se lee un fichero con casos de prueba en el que se indican
los parametros (N,M y K) y las casillas transitables
en el orden en el que se eliminan. Como salida, para cada caso
de prueba se imprimen las coordenadas de la casilla correspondiente.

*Resolucion*

Leemos el tablero y colocamos en la entrada (i, j)-esima de la matriz
un 0 si la casilla no es transitable y un 1 si lo es.

La funcion *buscar_camino* recibe un tablero y determina si existe algun camino valido entre los puntos
(0, 0) y (N, M). Para hacerlo, se utiliza un algoritmo de busqueda en profundidad: se situa en una casilla transitable (x, y) (la
primera vez, (0, 0)), y mira todas las casillas transitables - que, inicialmente, tienen valor asignado
1 - a distancia no mayor a K. Marca estos puntos con un 2, para no volver a mirarlos despues, y
los anade a una pila. Cuando se centra en un punto, lo elimina de la pila y mira sus vecinos (las
casillas transitables a distancia no mayor a K). Cuando acaba, se centra en el siguiente elemento
de la pila. Si en algun momento llega a la casilla (N, M), para la ejecucion y devuelve *True*. Si
la pila se vacia y no ha llegado a (N, M), quiere decir que no hay casillas transitables a las que
se pueda llegar desde el (0, 0) y no se hayan mirado ya; por tanto, no puede llegar a (N, M), y
devuelve *False*. Cuando se ha determinado si habıa o no un camino, se restablecen los valores
2 a 1. 

Este metodo tiene un coste computacional de O(n). donde n es el numero de casillas transitables.

El metodo *busqueda_ultima_transitable* busca, en la lista de las casillas transitables (distintas
de (0, 0) y (N, M)), el indice en esa lista de la casilla transitable que hizo que dejara de haber
camino al ser eliminada. Esta busqueda se hace de manera dicotomica: se centra en el punto
medio de los extremos y elimina del tablero todas las casillas transitables anteriores al centro.
Despues, llama a *buscar_camino*, y descarta la mitad de la lista correspondiente, segun si habıa
o no camino. El numero de veces que nos centramos en una casilla es de orden O(log(n)), y comprobar si habıa camino tiene un coste de O(n). Por tanto, esta funcion tiene un coste de O(nlog(n)).

Para el programa principal, inicializamos el tablero con las casillas correspondientes, primero todas vacıas. A continuacion, colocamos la posidonia. Seguidamente, miramos si hay camino;
si lo no hay, el programa devuelve NUNCA SE PUDO, mientras que si existe el camino, llama a
busqueda ultima posidonia, y devuelve las coordenadas de la casilla de posidonia correspondiente. Por tanto, el programa tiene un coste de O(nlog(n)).