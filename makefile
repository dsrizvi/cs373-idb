IMAGE_APP := seriesz_app
IMAGE_LB := seriesz_lb
IMAGE_DB := seriesz_db
DOCKER_HUB_USERNAME := dsrizvi

docker-build-push:
	@echo "Source docker.env in carina access file first..."
	@echo "Building all images..."

	docker login

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_APP} flask/app
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_APP}

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_LB} flask/db
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_LB}

	docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_LB} flask/lb
	docker push ${DOCKER_HUB_USERNAME}/${IMAGE_LB}


docker-run:
	 docker-compose --file flask/docker-compose-prod.yml up -d
