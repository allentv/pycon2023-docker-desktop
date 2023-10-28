from datetime import datetime as dt

import humanize


def process_date(date_data: str) -> str:
    created = dt.strptime(date_data.split("T")[0], "%Y-%m-%d")
    return humanize.naturaldelta(dt.now() - created) + " ago"


def process_image_info(images_info: list):
    # Create the Docker image information to be displayed in a table
    result = list()
    for image_info in images_info:
        commit = image_info.short_id.replace("sha256:", "")
        name, tag = image_info.tags[0].split(":")
        size = round(int(image_info.attrs["Size"]) / 1024 / 1024, 2)
        result.append(
            [
                name,
                commit,
                tag,
                f"{size} MB",
                process_date(image_info.attrs["Created"]),
            ]
        )

    return result


def process_container_info(containers_info: list):
    return [
        [
            container_info.name,
            container_info.image,
            container_info.status,
        ]
        for container_info in containers_info
    ]


def process_volume_info(volumes_info: list) -> list:
    return [
        [
            volume_info.attrs["Name"],
            process_date(volume_info.attrs["CreatedAt"]),
        ]
        for volume_info in volumes_info
    ]
