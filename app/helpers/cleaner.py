def json_cleaner_category(json_translate: dict):
    for json in json_translate:
        json['name'] = json['name'].strip().lower()

    return json_translate


def json_cleaner_faqs(json_translate: dict):
    for json in json_translate:
        json['question'] = json['question'].strip().lower()
        json['answer'] = json['answer'].strip()

    return json_translate
