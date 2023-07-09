from typing import List

from glanceclient.v2 import client
from keystoneauth1 import session as keystone_session


def glance_client(session: keystone_session.Session) -> client.Client:
    return client.Client(
        session=session,
        endpoint="public",
        timeout=2,
    )


def supported_images(glance: client.Client, tag: str) -> List[str]:
    return [image.id for image in glance.images.list(filters={"tag": [tag]})]
