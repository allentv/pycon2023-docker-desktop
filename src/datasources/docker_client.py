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

    def pull_images(self, name):
        assert len(name) > 0
        tag = name.split(":")[1] if ":" in name else "latest"
        return self.client.api.pull(name, tag)


@lru_cache
def get_client() -> docker.DockerClient:
    return docker.from_env()
