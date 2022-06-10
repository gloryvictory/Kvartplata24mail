import os
import json


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
