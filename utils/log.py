import logging


def setup_custom_logger(logger_name: str = "root",
                        logger_level: int = logging.WARNING):
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s'
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)
    logger.addHandler(handler)

    return logger

