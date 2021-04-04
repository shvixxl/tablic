"""Logging module."""

import sys
import logging

from loguru import logger

from app.config import settings


class InterceptHandler(logging.Handler):
    """
    Logging handler for intercepting standard logging messages
    toward Loguru sinks.
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def init_logger():
    """Configures and returns logger."""
    logger.remove()
    logger.add(
        sys.stdout,
        level=settings.LOGGING_LEVEL,
        format=settings.LOGGING_FORMAT,
        colorize=True,
        backtrace=True,
        enqueue=True,
    )
    logger.add(
        settings.LOGGING_PATH,
        level=settings.LOGGING_LEVEL,
        format='{message}',
        serialize=True,
        backtrace=True,
        enqueue=True,
        rotation=settings.LOGGING_ROTATION,
        retention=settings.LOGGING_RETENTION,
        compression=settings.LOGGING_COMPRESSION,
    )

    handler = InterceptHandler()
    for name in ['uvicorn', 'uvicorn.access', 'uvicorn.error', 'fastapi']:
        log = logging.getLogger(name)
        log.handlers.clear()
        log.propagate = True

    logging.basicConfig(handlers=[handler], level=0)

    return logger.bind(request_id=None, method=None)
