
import celery

import structlog
LOGGER = structlog.get_logger()


@celery.task
def log_signal(method, path, headers, payload):
    LOGGER.info('debug captured', method=method, path=path, headers=headers, payload=payload)
