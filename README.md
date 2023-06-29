Guia para probar la aplicacion:

Nota: 
    Se deja una BD con datos, para facilitar las pruebas. El usuario y clave es root.
    Si se desea cambiar u probar otro ir a http://127.0.0.1:5000/admin/ usar dichas credenciales y cambiar

Para levantar el servicio ejecutar: docker-compose up
La documentacion se hallara en: http://127.0.0.1:5000/redoc/ y http://127.0.0.1:5000/swagger/

Para crear las distintas configuraciones de cepas, usar el endpoint http://127.0.0.1:5000/strain/strains/ 
Un ejemplo del json: {
    "days_of_maturation":1,
    "life_expectancy": 1,
    "reproduction_rate": 1,
    "user": 1
}

Para obteber el resultado de bacterias por dias, usar el endpoint: http://127.0.0.1:5000/strain/count_replication/
Un ejemplo del json:{
    "strain": 1,
    "days": 60,
    "bacteria": [2, 3, 3, 1, 2]
}
