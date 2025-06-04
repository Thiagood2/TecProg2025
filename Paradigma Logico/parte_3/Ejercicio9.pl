/* Insertar Elemento en una Lista Ordenada */



insertar(Valor, [], [Valor]). % Si no hay elementos, insertamos el valor
insertar(Valor, [X|L1], [Valor, X| L1]):- Valor < X. % Si Valor < X, insertamos Valor y X, y luego el resto de L1 y cerramos.
insertar(Valor, [X|L1], [X | Resultado]):- insertar(Valor, L1, Resultado), !. % Si Valor es >= X, recorremos L1 insertando X en Resultado