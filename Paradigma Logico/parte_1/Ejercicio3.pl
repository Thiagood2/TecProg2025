% Hechos

menu(['Bombones de jamon', 'Locro', 'Dulce de batata']).
menu(['Bombones de jamon', 'Locro', 'Alfajor nortenyo']).
menu(['Tarta de atun', 'Atados de repollo', 'Dulce de batata']).
menu(['Tarta de atun', 'Pollo romano con hierbas y vino', 'Flan']).
menu(['Volovanes de atun', 'Matambre con espinacas y parmesano', 'Torta moka']).
menu(['Bunuelos de bacalao', 'Locro', 'Alfajor nortenyo']).


/* Primer Consulta: 
(1) menu(X), -> nos arroja todos los menues completos en la variable X. 
(2) menu([X,Y,Z]) --> nos arroja todos los posibles platos de menues asignados a cada Variable. */

/* Segunda Consulta: 
(1) menu(X),member('Dulce de batata',X), --> nos arroja el menu completo donde contiene a Dulce de batata. 
(2) menu([X,Y,'Dulce de batata']) --> nos arroja cada plato del menu asignado a las variables X e Y en el cual contienen a Dulce de batata. */

/* Tercer Consulta:  menu(X),member('Locro', X), --> nos arroja el menu completo donde contiene a Locro. */
/* Cuarta Consulta:  menu([X,'Pato a la naranja',Y]), --> retorna false porque no hay ningun menu que contenga a dicho plato como principal. */
/* Quinta Consulta: menu(['Locro',X,Y]), --> Retorna false porque no hay ningun menu que contenga a Locro como entrada. */
