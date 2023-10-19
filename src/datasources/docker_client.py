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


@lru_cache
def get_client() -> docker.DockerClient:
    return docker.from_env()
