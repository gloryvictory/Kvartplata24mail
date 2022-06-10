import logging
import os
import json
import config as cfg


def file_save_email_json(dirname_full_out='', p_email=''):
    file_email_json = os.path.join(
        dirname_full_out, "email.json")
    if not os.path.isfile(file_email_json):
        with open(file_email_json, 'w', encoding='utf-8') as f:
            json.dump(p_email, f,
                      ensure_ascii=False, indent=4)


# "info.txt"
def file_save_json(dirname_full_out='', person_json=[], file_name=''):
    str_out_json = os.path.join(dirname_full_out, file_name)
    with open(str_out_json, 'a', encoding='utf-8') as f:
        json.dump(person_json, f,
                  ensure_ascii=False, indent=4)


def set_logger():
    for handler in logging.root.handlers[:]:  # Remove all handlers associated with the root logger object.
        logging.root.removeHandler(handler)
    # dir_out = get_output_directory()
    # file_log = str(os.path.join(dir_out, cfg.file_log))  # from cfg.file
    file_log = cfg.FILE_LOG
    if os.path.isfile(file_log):  # Если выходной LOG файл существует - удаляем его
        os.remove(file_log)
    logging.basicConfig(filename=file_log, format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO,
                        filemode='w')
    logging.info(file_log)
