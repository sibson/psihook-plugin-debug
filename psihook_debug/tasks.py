
import celery

import structlog
LOGGER = structlog.get_logger()


@celery.task
def log_signal(path, headers, payload):
    LOGGER.info('signaled', path=path, headers=headers, payload=payload)
