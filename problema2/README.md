**Problema 2**

Dos jugadores juegan al 31 con algunas reglas adicionales:



Empiezan con un número aleatorio entre 0 y 30, y se turnan para pulsar los números de
una calculadora y sumarlos al total acumulado. El primer jugador en sobrepasar el 30
pierde. Para hacerlo más interesante, las teclas de la calculadora están cambiadas de 
sitio, y además solo pueden utilizar los números situados en la misma fila o columna
que el dígito marcado por su oponente en el turno anterior, aunque no se puede repetir
el número. Además, el número 0 no puede utilizarse. Por ejemplo, si las teclas están
colocadas de la siguiente manera, y el último dígito que pulsó el oponente fue un 1, 

                                                    3   7  |*1*
                                                   ------------
                                                    2   5  | 8
                                                    9   4  | 6
el oponente podría utilizar las teclas 3, 7, 8 y 6.

El objetivo del problema es determinar si el jugador al que le toca ir segundo gana o
pierde.

Se recibe un fichero con casos de prueba en los que se indica el valor visible en la
calculadora al recibir el turno, la última jugada del adversario y la posición de los
números.

**Resolución**

En primer lugar, se lee el fichero de entrada y se guarda la posición de los números en la 
una lista. Nos interesa saber desde qué números se puede acceder a qué números en la
siguiente jugada, pero para eso no necesitamos conocer exactamente los números;
simplemente su posición.

Para modelizar la posición de los números en la calculadora utilizamos un diccionario,
*jugadas_validas*, para guardar la posición (clave) y las posiciones a las que se
puede acceder desde ella (valor). Así, partiendo de la matriz cuyas entradas
son las posiciones en la lista ordenadas, por ejemplo,

                                                    3   7  |*1*
                                                   ------------
                                                    2   5  | 8
                                                    9   4  | 6
desde la posición i,j podemos acceder a toda la fila i-ésima y columa j-ésima, quitando
la propia posición i,j. A partir de esta posición se determina todo el diccionario.
Por ejemplo, jugadas_validas[0]=[1,2,3,6] y jugadas_validas[4]=[1,3,5,7].

Dada una entrada, para determinar si el segundo jugador gana o pierde se utiliza un 
algoritmo de *backtracking*: de manera recursiva y alternando de jugador en cada llamada,
se intenta realizar una jugada y se van explorando las posibles jugadas que siguen a esta. Si se llega a alguna en las que todas las posibles
jugadas del rival llevan a una posible victoria del segundo jugador, se devuelve True.
Si no, se devuelve False.

Además, para reutilizar información, para cada rama explorada guardaremos el resultado
obtenido, ya que habrá muchos casos en los que llegaremos al mismo punto de una
partida (por ejemplo, que la suma sea de 20 y que el rival acabe de jugar un 4). Así, nos 
ahorramos volver a explorar esa rama del árbol de soluciones. También nos sirve para
ambos jugadores: si una jugada es ganadora para uno, será perdedora para el otro, y vice versa.


**Coste computacional**

Es difícil determinar de manera exacta el coste computacional debido a la aleatoriedad
de las entradas y a la dificultad que suele suponer siempre calcular el coste de un
algoritmo de backtracking (es complicado medir exactamente las podas que se realizan).
Sin embargo, sí es sencillo dar una cota superior:

En cada llamada recursiva, hay como mucho 4 caminos distintos, así que basta acotar
el número de llamadas recursivas. En el peor de los casos, empezaremos desde 0, y la
secuencia de jugadas con menor suma posible es 1,2,1,2,1,2,... Se suman 3 puntos al 
contador cada 2 jugadas, así que a las 20 jugadas habremos llegado a 30, y a la siguiente
todas perderán. Entonces, como mucho podremos hacer 4**20 operaciones. Sin embargo,
nunca nos acercaremos a esta cota, ya que guardamos información precalculada y es imposible
que exploremos todo el árbol, pues una vez que sabemos que uno ganará ya no se explora
más esa rama.