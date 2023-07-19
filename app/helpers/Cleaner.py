class Cleaner:

    def json_cleaner(basic_json_translate):
        for json in basic_json_translate:
            json['name'] = json['name'].strip().lower()

        return basic_json_translate