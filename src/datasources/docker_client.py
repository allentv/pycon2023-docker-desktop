from functools import lru_cache

import docker


class DockerManager:
    def __init__(self) -> None:
        self.client = get_client()

    def get_containers(self) -> list:
        return self.client.containers.list()

    def get_images(self) -> list:
        return self.client.images.list()

    def get_volumes(self) -> list:
        return self.client.volumes.list()

    def pull_images(self, name) -> None:
        assert len(name) > 0
        tag = name.split(":")[1] if ":" in name else "latest"
        self.client.api.pull(name, tag)

    def run_container(self, image_name) -> None:
        assert len(image_name) > 0
        container = self.client.api.create_container(image_name, "sleep 120")
        self.client.api.start(container.get("Id"))


@lru_cache
def get_client() -> docker.DockerClient:
    return docker.from_env()
