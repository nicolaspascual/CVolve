import json
from cvolve.main.models import JobOffer
from glob import glob
from os.path import join

def to_float_or_none(string):
    try:
        return float(string)
    except:
        return None

def to_int_or_none(string):
    try:
        return int(string)
    except:
        return None

def extract_duration(duration_str):
    splitted = duration_str.split()
    if len(splitted) == 2:
        return to_int_or_none(splitted[0]), splitted[1]
    else:
        return None, None


def load_job_offers_from_json(base_dir):
    for file_path in glob(join(base_dir, '*.json')):
        with open(file_path, 'r') as f:
            job_offer_json = json.load(f)
        JobOffer(
            title = job_offer_json['title'],
            description = job_offer_json['description'],

            responsibilities = '\n'.join(job_offer_json['responsibilities']),
            minimum_requirements = '\n'.join(job_offer_json['minimum_requirements']),
            preferred_requirements = '\n'.join(job_offer_json['preferred_requirements']),

            type = job_offer_json['type'],
            compensation = to_float_or_none(job_offer_json['compensation']),
            duration = extract_duration(job_offer_json['duration'])[0],
            duration_unit = extract_duration(job_offer_json['duration'])[1],

            company = job_offer_json['company'],
            department = job_offer_json['department'],

            city = job_offer_json['location']['city'],
            state = job_offer_json['location']['state'],
            country = job_offer_json['location']['country'],
        ).save()
