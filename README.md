# Chocobo's Sanctuary

## Parte 1

Bienvenido al santuario de Chocobo, donde las majestuosas aves pasean libres!

Actualmente tenemos una aplicación llamada Safari, que se encarga del agendamiento de vehículos blindados y equipados con protección anti-ave. El desarrollador encargado de mantenerla se ha "enfermado" indefinidamente luego de un encuentro con una de las aves, por lo que te pedimos que si el proyecto no funciona o contiene malas prácticas intentes arreglarlo por tu cuenta, al menos los endpoints que vas a utilizar. Nos gusta seguir la regla del Boy Scout: "dejo el campamento más limpio que como lo encontré".

### Tu tarea en este proyecto es:

- Clonar el proyecto
- Eliminar los decoradores `@pytest.mark.skip` de los tests
- Implementar los tests que están con TO-DO
- Desarrollar las funcionalidades para que pase las pruebas ejecutando `docker-compose run --rm test`

### Requirements

- docker
- docker-compose

### Buils the project

`make build`

### Create migrations

`make migrations`

### Run migrations

`make migrate`

### Star or Stop the project

`make up-daemon or make stop`

### Migraciones fallan?

Google es tu amigo, y stackoverflow también.

#### Swagger

http://localhost:8000/api/schema/swagger-ui/


#### Mailhog

http://localhost:1025


## Parte 2

Hemos tenido problemas con nuestros vehículos, ha habido un aumento de casos en los que nuestros usuarios se quedan sin combustible en medio de su recorrido por nuestro parque. La distribución del parque y sus caminos fue hecha por una persona a quien le encantan los árboles de búsqueda binaria, por lo que un mapa se vería de la siguiente forma.
  
![mapa safari](https://i.imgur.com/noULk0A.png)
  
  
Notar que cada nodo puede tener 2 nodos "hijos": el de la izquierda con un valor inferior y el de la derecha con valor superior. Todos los puntos conectados a la izquierda de un nodo son inferiores a éste, y todos los conectados a la derecha son superiores. Básicamente comportándonse como un árbol binario de búsqueda.  
  
Cada punto marcado por una sombrilla y un símbolo de gasolinera es una zona de descanso.  
- Todas las zonas de descanso se identifican por el kilómetro en cual se encuentra.
- Las zonas de descanso tienen estaciones para cargar combustible con precios distintos.
- Los caminos se pueden considerar como líneas rectas para efectos de consumo de combustible.
- Todos los vehículos tienen rendimiento de combustible y tamaño de estanque distintos.
- Hay vehículos que no van a poder completar recorridos sin parar a cargar combustible.
- La implementación de esto se encuentra en el proyecto Safari, app 'adventure'.
  
## Tu tarea:
  
Necesitamos que desarrolles un script o una API separada del proyecto safari, en el lenguaje o framework que prefieras, que cumpla con las siguientes funciones:  
- Obtener la ruta de un punto A a un punto B cualquiera, listando las áreas de servicio por las cual se debería pasar.
- Calcular en qué puntos y cuánto combustible debe uno cargar para que una ruta completa (desde un punto A a un punto B cualquiera) sea lo más barata posible. Considerar lo siguiente
    - La función recibe: punto de inicio (int que corresponde al km), punto de término (int que corresponde al km) y patente del vehículo.
    - Debe retornar una lista con los puntos donde parar y cuántos litros cargar.
    - Un viaje puede comenzar y terminar en cualquier punto de descanso, sin devolverse por el mismo camino.
    - Todos los vehículos comienzan con el estanque lleno, no es necesario devolverlos llenos.
    - No todos los vehículos tienen el mismo rendimiento ni tamaño de estanque.
    - No todos los vehículos van a tener rendimiento y estanque suficiente como para realizar un recorrido completo sin cargar combustible.
    - No es necesario realizar carga completa del estanque cuando uno pasa por un punto de descanso, se puede cargar lo suficiente como para sólo llegar hasta el siguiente.
    - Todas las áreas de servicio tienen precios de combustible distintos.

# Para conocerte mejor

1. Cuáles crees que son los aspectos más importantes al momento de hacer Code Review
    - Chekear las nuevas dependencias que estan agregando para el feature que esta haciendo, tambien las variables
        de entorno que se agregan. Por Ejemplo: Actualmente en un proyecto usamos 3 archivos de variables DEV, STAGGING
        y PROD. Asi que para algunos features se tienen que agregar las varibles en los 3 archivos para que los pasos a QA o PROD se mas rapido.
2. Has trabajado con control de versiones? Cuál ha sido el flujo que has utilizado? Por favor explicar.
    - He usado Bitbucker, Github y Gitlab, pero con el que me siento más comodo es gitlab he realizado configuraciones,
        de git runners, hooks, pippelines. Siempre he trabajo bajo 3 ramas DEV, STAGING y PROD.
3. Cuál ha sido tu experiencia utilizando herramientas fuera de desarrollo del código mismo? (AWS, GCP, VPS, Docker, etc.)
    - He realizado configuraciones de Nginx nativo, y con docker he usado neginx proxy and letsencrypt. He aperturado tuneles para conecciones a DB. entre otras cosas. He usado docker para todos mis proyectos, y junto con un compañero, implementaciones una construcción del servicio por fases, lo cual lo hace muchos más rapido al contrsuir.
4. Tienes algún servicio en la nube favorito? Cuál y por qué?
    - Para proyectos personales he estado usando DigitalOcean con el S3 de AWS, por motivos de bajo costo, pero en     general AWS sus servicos sons muy buenos aunque aún no me considero un experto del tema.
5. Has tenido experiencia con microservicios? En caso de que la tengas, podrías explicar por qué en ese caso fue mejor un microservicio que otro tipo de arquitectura?
    - En Rextie que es una StarTup peruana de cambios de divisas usabamos la arquitectura de microservicios. En el cual
    teniamos un front en React, el backend era Django Rest Framework y diversos scripts que usabamos para la consulta de tipo de cambios de otros bancosa que Rextie te ofrece un tipo de cambio mejor que el ellos. En este caso fue mejor usar una arquitectura de microservicios ya que cada aplicación era independiente, podriamos estar trabajando de manera rapida y conjunta, nos ayuda mucho hacer integración continua.
