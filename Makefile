dev:
	docker-compose up

test:
	pytest --cov=backend tests/

migrate:
	./scripts/migrate.sh

deploy:
	./scripts/deploy.sh