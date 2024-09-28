import logging

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='\033[1;36m%(asctime)s\033[0m - \033[1;32m%(levelname)s\033[0m - \033[1;33m%(message)s\033[0m'
    )

