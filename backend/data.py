import datetime
import json
import pandas as pd


def parse_time(str_repr):
    return datetime.datetime.strptime(str_repr, "%d/%b/%Y:%H:%M:%S %z")


def read_data(file):
    data = []
    with open(file) as f:
        while True:
            line = f.readline()
            if not line:
                break
            try:
                raw_data = json.loads(line)
                if raw_data['total_blocks'] == '-':
                    pass
                raw_data['current_block'] = int(raw_data['current_block'])
                raw_data['total_blocks'] = int(raw_data['total_blocks'])
                raw_data['tags'] = raw_data['story_tags'].split(",")
                raw_data['time'] = parse_time(raw_data['time'])
                data.append(raw_data)
            except:
                pass

    pdf = pd.DataFrame(data)
    pdf['read_percentage'] = (pdf['current_block']/pdf['total_blocks'])*100
    return pdf


def clean_data(df):
    required = [
        'category',
        'country_code',
        'current_block',
        'total_blocks',
        'time',
        'tags',
        'dev_source',
        'story_id',
    ]

    for i in df.keys():
        if i not in required:
            del df[i]
