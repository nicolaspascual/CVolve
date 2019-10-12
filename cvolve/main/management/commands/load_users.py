import datetime
import json
from glob import glob
from os.path import join

from django.core.management.base import BaseCommand

from cvolve.main.models import (User, UserEducation, UserExperience,
                                UserProjects, UserSkill)


def parse_date(string):
    if len(string) > 0:
        return datetime.datetime.strptime(string, '%d/%m/%Y')
    else:
        return None


def load_users_from_json(base_dir):
    for file_path in glob(join(base_dir, '*.json')):
        with open(file_path, 'r') as f:
            user_json = json.load(f)

            user = User.objects.create_user(
                username=user_json['username'],
                password=user_json['password'],
                name=user_json['name'],
                surnames=user_json['surnames'],
                mail=user_json['mail'],
                phone=user_json['phone'],
                summary=user_json['summary'],
                languages=', '.join(user_json['languages'])
            ).save()

            for skill in user_json['skills']:
                UserSkill(
                    name=skill,
                    user=User.objects.get(username=user_json['username'])
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


class Command(BaseCommand):
    help = 'Loads users from folder with jsons'

    def add_arguments(self, parser):
        parser.add_argument('base_path', type=str)

    def handle(self, **options):
        load_users_from_json(options['base_path'])
