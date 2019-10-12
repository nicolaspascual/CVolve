import json
from cvolve.main.models import JobOffer, User, UserEducation, UserExperience, UserProjects
from glob import glob
from os.path import join
import datetime


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
            title=job_offer_json['title'],
            description=job_offer_json['description'],

            responsibilities='\n'.join(job_offer_json['responsibilities']),
            minimum_requirements='\n'.join(
                job_offer_json['minimum_requirements']),
            preferred_requirements='\n'.join(
                job_offer_json['preferred_requirements']),

            type=job_offer_json['type'],
            compensation=to_float_or_none(job_offer_json['compensation']),
            duration=extract_duration(job_offer_json['duration'])[0],
            duration_unit=extract_duration(job_offer_json['duration'])[1],

            company=job_offer_json['company'],
            department=job_offer_json['department'],

            city=job_offer_json['location']['city'],
            state=job_offer_json['location']['state'],
            country=job_offer_json['location']['country'],
        ).save()


def parse_date(string):
    if len(string) > 0:
        return datetime.datetime.strptime(string, '%d/%m/%Y')
    else:
        return None


def load_users_from_json(base_dir):
    for file_path in glob(join(base_dir, '*.json')):
        with open(file_path, 'r') as f:
            user_json = json.load(f)

            user = User(
                username=user_json['username'],
                password=user_json['password'],
                name=user_json['name'],
                surnames=user_json['surnames'],
                mail=user_json['mail'],
                phone=user_json['phone'],
                summary=user_json['summary'],
                skills='\n'.join(user_json['skills']),
                languages='\n'.join(user_json['languages'])
            ).save()

            for experience in user_json['experience']:
                UserExperience(
                    role=experience['role'],
                    company=experience['company'],
                    start_date=parse_date(experience['start_date']),
                    end_date=parse_date(experience['end_date']),
                    summary=experience['summary'],
                    user=User.objects.get(username=user_json['username'])
                ).save()

            for education in user_json['education']:
                UserEducation(
                    title=education['title'],
                    institution=education['institution'],
                    start_date=parse_date(education['start_date']),
                    end_date=parse_date(education['end_date']),
                    summary=education['summary'],
                    user=User.objects.get(username=user_json['username'])
                ).save()

            for project in user_json['projects']:
                UserProjects(
                    name=project['name'],
                    summary=project['summary'],
                    user=User.objects.get(username=user_json['username'])
                ).save()
