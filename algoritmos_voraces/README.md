**Problema**

Una foca va a un restaurante de cangrejos con buffet libre. 
Los cangrejos le van llegando en una cinta en un orden que no puede elegir ni conoce, y
tiene que írselos comiendo todos, colocando las cáscaras vacías.
La foca quiere ir apilando las cáscaras de manera que nunca quede una cáscara encima de
otra más pequeña. Si no puede colocar una cáscara encima de ninguna torre por ser 
demasiado grande, crea otra torre.

El objetivo es determinar el mínimo número de torres que necesita la foca.

Se recibe un fichero donde se indica, en cada caso de prueba, el número de cangrejos
que se va a comer (siempre entre 1 y 500000) y el tamaño de los caparazones en el
orden en el que le van llegando. Como salida, se debe imprimir el número objetivo.

**Resolución**

Las condiciones del problema decantan al uso de un algoritmo voraz, pues las decisiones
deben tomarse con la información disponible en cada instante (los caparazones van
llegando en un orden desconocido y no se puede cambiar).

Cuando llega un caparazón nuevo, tenemos que decidir en qué torre colocarlo. Para esto,
solo nos interesa el tamaño caparazón que se encuentra por encima en cada torre. De
entre los caparazones en las que lo puede colocar, lo pondrá siempre en la que tenga 
el menor tamaño posible. Si no hay ninguna en la que lo pueda colocar, creará una 
torre nueva.

Para implementar esta idea, guardamos en una lista de orden ascendente los representantes
de cada torre (los caparazones de encima de cada torre). Así, el problema se reduce a
encontrar, mediante una búsqueda dicotómica, el primer representante con un tamaño mayor
al del nuevo caparazón. El caparazón recién llegado pasará a ser el representante de
la torre en la que se encuentre, o en caso de no existir, de una nueva torre, que
ocupará la última posición en la lista. De esta manera, se mantiene la lista ordenada
para el siguiente caparazón. Al final, simplemente imprimimos la longitud de la lista.

Para no tener que ir ampliando la lista cada vez que se tenga que crear una torre, 
inicializamos una lista de longitud 500000 en la que iremos guardando los
representantes de cada torre, e iremos reutilizando entre los distintos casos de prueba.

**Coste computacional**

Para determinar la posición de un caparazón se realiza una búsqueda dicotómica entre
las torres, que tiene un coste de O(log(m)), donde m es el número de torres. En el peor
de los casos, los caparazones llegan en orden creciente, y se debe crear una torre
nueva torre cada vez. En ese caso, el coste computacional es del orden de

                                O(log(1) + log(2) + ... + log(n))=O(nlog(n))

