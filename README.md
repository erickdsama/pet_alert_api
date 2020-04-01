# Template of FLASK & PSQL with docker

**requirements**

- docker: https://docs.docker.com/install/

- docker-compose: https://docs.docker.com/compose/install/

First your need clone your project.

insisde of project directory run:

`docker-compose up`


url web is http://0.0.0.0:5000

to see the log web

`docker logs -f  web_flask`

to see the log psql

`docker logs -f  psql_flask`
