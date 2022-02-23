from dependency_injector import containers, providers

from fastapi_di_sample.my_db_client import MyDbClient

from . import services


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])

    # config = providers.Configuration(yaml_files=["config.yml"])

    my_client = providers.ThreadSafeSingleton(MyDbClient)

    my_service = providers.Factory(
        services.MyService,
        client=my_client,
    )
