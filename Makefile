help: ## Muestra esta ayuda
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?##"}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

build: ## Crea la imagen del proyecto
	docker-compose -f docker-compose.yml build

up-daemon: ## Inicia contenedores en background
	docker-compose -f docker-compose.yml up -d

up: ## Inicia contenedores en primer plano
	docker-compose -f docker-compose.yml up --remove-orphans

start: ## Inicia ejecución contenedores ya existentes
	docker-compose -f docker-compose.yml start

stop: ## Detiene ejecución de contenedores
	docker-compose -f docker-compose.yml stop

down: ## Elimina los contenedores
	docker-compose -f docker-compose.yml down -v

restart: ## Reinicia ejecución de contenedores
	docker-compose -f docker-compose.yml stop && docker-compose -f docker-compose.yml start

migrations: ## Crea migraciones en el proyecto
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py makemigrations"

migrate: ## Aplica migraciones en el proyecto
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py migrate"

superuser: ## Crea un super usuario
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py createsuperuser"

startapp: ## Crea un app de django
	docker-compose -f docker-compose.yml exec web /bin/bash -c "cd server/apps/; django-admin startapp $(app_name)"

test: ## Ejecuta pruebas unitarias de un app
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py test $(app_name)"

collectstatic: ## Recolecta archivos estáticos
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py collectstatic --noinput"

clear_cache: ## Limpia el caché
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py clear_cache"

showmigrations: ## Muestra las migraciones de un app
	docker-compose -f docker-compose.yml exec web /bin/bash -c "python manage.py showmigrations $(app_name)"

django-shell: ## Ejecutar shell de Django
	docker-compose -f docker-compose.yml run web /bin/bash -c "python manage.py shell"

shell-nginx: ## Conectarse al contenedor de nginx
	docker-compose -f docker-compose.yml exec nginx /bin/bash

shell-web: ## Conectarse al contenedor del proyecto
	docker-compose -f docker-compose.yml exec web /bin/bash

shell-db: ## Conectarse al contenedor de la base de datos
	docker-compose -f docker-compose.yml exec db /bin/bash

log-nginx: ## Mostrar logs del contenedor de nginx
	docker-compose -f docker-compose.yml logs nginx

log-web: ## Mostrar logs del contenedor del proyecto
	docker-compose -f docker-compose.yml logs web

log-db: ## Mostrar logs del contenedor de la base de datos
	docker-compose -f docker-compose.yml logs db

lint: ## Ejecutar pylint al código
	docker-compose -f docker-compose.yml exec web /bin/bash -c "pylint server --disable=fixme,no-name-in-module,import-error \
	--reports=n --load-plugins=pylint_django,pylint_celery --rcfile=.pylintrc --ignore=migrations,settings \
	--django-settings-module=server.settings.dev --exit-zero"

pytest: ## Ejecuta pruebas unitarias de un app
	docker-compose -f docker-compose.yml exec web /bin/bash -c "pytest -v"
