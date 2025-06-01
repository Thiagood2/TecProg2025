% Hechos

entrada(ensalada).
entrada(empanadas fritas).
entrada(mani y pochoclos).

plato_principal(milanesas con papas).
plato_principal(pollo con arroz).
plato_principal(asado con pure).

postre(helado).
postre(ensalada de frutas).
postre(flan con dulce de leche).

carta(X,Y,Z):- entrada(X), plato_principal(Y), postre(Z).


/* En total, nos arrojara 27 combinaciones posibles ya que por cada Entrada, existen 9 combinaciones, Total = 3*9 */

