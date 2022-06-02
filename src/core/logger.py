import logging
from logging.handlers import RotatingFileHandler
import os
import config as cfg

#
# def get_logger():
#     logging.basicConfig(filename=cfg.FILE_LOG, format=cfg.FILE_LOG_FORMAT, level=logging.info)
#     logger = logging.getLogger(cfg.LOGGER_NAME)
#     # handler = RotatingFileHandler(cfg.FILE_LOG, maxBytes=cfg.FILE_LOG_MAX_BYTES, backupCount=cfg.FILE_LOG_BACKUP_COUNT)
#     # logger.addHandler(handler)
#     return logger

def get_logger():
    for handler in logging.root.handlers[:]:  # Remove all handlers associated with the root logger object.
        logging.root.removeHandler(handler)
    #dir_out = get_output_directory()
    #file_log = str(os.path.join(dir_out, cfg.file_log))  # from cfg.file
    file_log = cfg.FILE_LOG
    if os.path.isfile(file_log):     # Если выходной LOG файл существует - удаляем его
        os.remove(file_log)
    logger = logging.basicConfig(filename=file_log, format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO,
                        filemode='w')  #
    logging.info(file_log)

    # handler = RotatingFileHandler(cfg.FILE_LOG, maxBytes=cfg.FILE_LOG_MAX_BYTES, backupCount=cfg.FILE_LOG_BACKUP_COUNT)
    # logger.addHandler(handler)

    return logger

