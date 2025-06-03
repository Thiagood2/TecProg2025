/* Calcular el Factorial de un numero con entrada factorial(X, total) */
% Reglas

positivo(X):- X >= 0.
factorial(0, 1).

factorial(Num, Res):-  
            positivo(Num),          % Chequeo que el numero sea positivo
            Num1 is Num - 1,        % Voy descontando el valor del numero hasta 0, que es mi caso base
            factorial(Num1, Res1),  % Vuelvo a llamar a factorial con los nuevos valores
            Res is Num * Res1.      % Va a ir sumando cada instancia de Res


