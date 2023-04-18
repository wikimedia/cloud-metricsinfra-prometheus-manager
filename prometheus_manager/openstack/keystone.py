import yaml
from keystoneauth1 import session as keystone_session
from keystoneauth1.identity import v3
from keystoneclient.v3 import client


def session(file_path: str) -> keystone_session.Session:
    with open(file_path, "r") as f:
        account_data = yaml.safe_load(f)

    auth = v3.Password(
        auth_url=account_data["OS_AUTH_URL"],
        password=account_data["OS_PASSWORD"],
        username=account_data["OS_USERNAME"],
        project_id=account_data["OS_PROJECT_ID"],
        user_domain_name=account_data["OS_USER_DOMAIN_ID"],
        project_domain_name=account_data["OS_PROJECT_DOMAIN_ID"],
    )

    return keystone_session.Session(
        auth=auth,
        user_agent="prometheus-manager",
    )


def keystone_client(file_path: str) -> client.Client:
    return client.Client(
        session=session(file_path),
        interface="public",
        timeout=2,
    )


def all_projects(keystone: client.Client, domain_id: str):
    """Get a list of all project names."""
    return [p.name for p in keystone.projects.list(enabled=True, domain=domain_id)]
