import logging

logger = logging.getLogger(__name__)

def log_with_context(message, context=None, log_level='info', logger_handler=None, **kwargs):
    context = context if context is not None else {}
    if logger_handler is None:
        logger_handler = logger
    log_function = __get_log_function(logger_handler, log_level)

    log_context_prefix = __get_log_context_prefix(context)
    if log_context_prefix:
        log_function(f"{log_context_prefix} {message}", **kwargs)
    else:
        log_function(message, **kwargs)


def __get_log_context_prefix(context):
    log_context_prefix = ""
    if context:
        for k, v in context.items():
            if v is not None:
                log_context_prefix += f"[{k}:{v}]"
    return log_context_prefix


def __get_log_function(logger_handler, log_level):
    switcher = {
        'info': logger_handler.info,
        'warning': logger_handler.warning,
        'error': logger_handler.error
    }
    return switcher.get(log_level, logger_handler.info)
