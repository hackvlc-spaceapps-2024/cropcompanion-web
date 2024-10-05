up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

create_app:
	docker compose run --rm back ./manage.py startapp ${i}

scaffold_django:
	docker compose run --rm django_scaffolder django-admin startproject back