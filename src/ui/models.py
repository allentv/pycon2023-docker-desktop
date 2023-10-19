from datetime import datetime as dt

import humanize


def process_image_info(images_info: list):
    # Create the Docker image information to be displayed in a table
    result = list()
    for image_info in images_info:
        commit = image_info.short_id.replace("sha256:", "")
        name, tag = image_info.tags[0].split(":")
        created = dt.strptime(image_info.attrs["Created"].split("T")[0], "%Y-%m-%d")
        size = round(int(image_info.attrs["Size"]) / 1024 / 1024, 2)
        result.append(
            [
                name,
                commit,
                tag,
                f"{size} MB",
                humanize.naturaldelta(dt.now() - created),
            ]
        )

    return result
