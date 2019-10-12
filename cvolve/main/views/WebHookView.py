from django.contrib import auth
from django.views import View
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cvolve.main.models.user_projects import UserProjects
from cvolve.main.models.user_education import UserEducation
from cvolve.main.models.user_experience import UserExperience
import json

class WebHookView(View):

    @csrf_exempt
    def post(self, request):
        jsondata = json.loads(request.body)
        data = jsondata['form_response']['answers']

        with open('answers.json', 'w') as json_file:
            json.dump(data, json_file)

        self.extract_user_data(data, request.user)
        index = self.extract_user_experience(data, request.user, 5)
        index = self.extract_user_education(data, request.user, index)
        # index = self.extract_user_skills(data, request.user, index)
        index = self.extract_user_projects(data, request.user, index + 1)

        return HttpResponse(jsondata)

    def extract_user_data(self, data, user):
        info = {
            'name': data[0]['text'],
            'surnames': data[1]['text'],
            'mail': data[2]['text'],
            'phone': data[3]['phone_number'],
            'languages': data[4]['text']
        }
        # for attr, val in info.items():
        #     setattr(user, attr, val)
        # user.save()
        with open('user_data.json', 'w') as json_file:
            json.dump(info, json_file)

    def extract_user_experience(self, data, user, index):
        results = []
        print(data[index])
        index += 1
        if data[index - 1]['boolean']:
            for i in range(1,5):
                info = {
                    'role': data[index]['text'],
                    'company': data[index + 1]['text'],
                    'start_date': data[index + 2]['date'],
                    'end_date': data[index + 3]['date'],
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
        with open('user_experience.json', 'w') as json_file:
            # m = UserExperience(**element)
            # m.save()
            json.dump(results, json_file)
        return index

    def extract_user_education(self, data, user, index):
        results = []
        index += 1
        if data[index - 1]['boolean']:
            for i in range(1,5):
                info = {
                    'title': data[index]['text'],
                    'institution': data[index + 1]['text'],
                    'start_date': data[index + 2]['date'],
                    'end_date': data[index + 3]['date'],
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
                    
        
        
        # for element in results:
        #     m = UserEducation(**element)
        #     m.save()
        with open('user_education.json', 'w') as json_file:
            # m = UserExperience(**element)
            # m.save()
            json.dump(results, json_file)
        return index

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
                index += 5
                if i == 4:
                    break
                elif not data[index]['boolean']:
                    index += 1
                    break
                else:
                    index += 1
        with open('user_projects.json', 'w') as json_file:
            # m = UserExperience(**element)
            # m.save()
            json.dump(results, json_file)
        return index


