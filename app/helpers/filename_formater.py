from datetime import datetime


def format_filenames(*filenames):
    new_formated_names = []
    for filename in filenames:
        now = datetime.now().strftime('%Y%H%M%S')
        new_formated_name = now+filename
        new_formated_names.append(new_formated_name)
    return new_formated_names

