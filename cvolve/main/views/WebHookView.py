from django.contrib import auth
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cvolve.main.models.user_projects import UserProjects
from cvolve.main.models.user_education import UserEducation
from cvolve.main.models.user_experience import UserExperience
from cvolve.main.models.user_skill import UserSkill
from cvolve.main.models.user import User
import datetime
import json

class WebHookView(View):

    @csrf_exempt
    def post(self, request):
        jsondata = json.loads(request.body)
        data = jsondata['form_response']['answers']

        user_id = int(jsondata['form_response']['hidden']['id'])
        user = User.objects.get(user_ptr_id=user_id)

        self.extract_user_data(data, user)
        index = self.extract_user_experience(data, user, 5)
        index = self.extract_user_education(data, user, index)
        index = self.extract_user_skills(data, user, index)
        index = self.extract_user_projects(data, user, index)

        return redirect(reverse('main'))

    def extract_user_data(self, data, user):
        info = {
            'name': data[0]['text'],
            'surnames': data[1]['text'],
            'mail': data[2]['text'],
            'phone': data[3]['phone_number'],
            'languages': data[4]['text']
        }
        for attr, val in info.items():
            setattr(user, attr, val)
        user.save()

    def extract_user_experience(self, data, user, index):
        results = []
        index += 1
        if data[index - 1]['boolean']:
            for i in range(1,5):
                info = {
                    'role': data[index]['text'],
                    'company': data[index + 1]['text'],
                    'start_date': self.format_date(data[index + 2]['date']),
                    'end_date': self.format_date(data[index + 3]['date']),
                    'summary': data[index + 4]['text'],
                    }
                results.append(info)
                index += 5
                if i == 4:
                    break
                elif not data[index]['boolean']:
                    index += 1
                    break
                else:
                    index += 1
        for element in results:
            element['user'] = user
            m = UserExperience(**element)
            m.save()
        return index

    def extract_user_education(self, data, user, index):
        results = []
        index += 1
        if data[index - 1]['boolean']:
            for i in range(1,5):
                info = {
                    'title': data[index]['text'],
                    'institution': data[index + 1]['text'],
                    'start_date': self.format_date(data[index + 2]['date']),
                    'end_date': self.format_date(data[index + 3]['date']),
                    'summary': data[index + 4]['text'],
                    }
                results.append(info)
                index += 5
                if i == 4:
                    break
                elif not data[index]['boolean']:
                    index += 1
                    break
                else:
                    index += 1
                    
        
        
        for element in results:
            element['user'] = user
            m = UserEducation(**element)
            m.save()
        return index

    def extract_user_skills(self, data, user, index):
        for skill in data[index]['text'].split(','):
            m = UserSkill(name=skill.strip(), user=user)
            m.save()
        return (index + 1)

    def extract_user_projects(self, data, user, index):
        results = []
        increment = 0
        index += 1
        if data[index - 1]['boolean']:
            for i in range(1,5):
                info = {
                    'name': data[index]['text'],
                    'summary': data[index + 1]['text'],
                    }
                results.append(info)
                index += 2
                if i == 4:
                    break
                elif not data[index]['boolean']:
                    index += 1
                    break
                else:
                    index += 1

        for element in results:
            element['user'] = user
            m = UserProjects(**element)
            m.save()
        return index

    def format_date(self, initial_date):
        data = initial_date.split('-')
        return datetime.datetime(int(data[0]), int(data[1]), int(data[2]))


