up:
	docker compose up

down:
	docker compose down -v

remove:
	docker image rm face-feature-recognition-model
	docker image rm face-feature-recognition-web

reload_web:
	docker compose down web
	docker image rm face-feature-recognition-web

reload_model:
	docker compose down model
	docker image rm face-feature-recognition-model