build:
	docker build -t capstone_project . -f /home/autodoc/PycharmProjects/cloud-platforms_azure/.devcontainer/Dockerfile

run:
	docker run -p 8084:84 -it capstone_project bash
