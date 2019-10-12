from django.contrib.auth.models import User as DjangoUser
from django.db import models

class User(DjangoUser):

    name = models.CharField('Name', max_length=50)
    surnames = models.CharField('Surnames', max_length=150)
    mail = models.CharField('Mail', max_length=50)
    phone = models.CharField('Phone', max_length=50)
    summary = models.TextField('Summary')
    skills = models.TextField('Skills')  # Separated by new lines
    languages = models.TextField('Languages')  # Separated by new lines

    @property
    def experience(self):
        return self.userexperience_set.all()

    @property
    def projects(self):
        return self.userprojects_set.all()

    @property
    def education(self):
        return self.usereducation_set.all()

    def to_comparable_text(self):
        return ' '.join([
            self.summary, self.skills, self.languages,
            ' '.join(exp.to_comparable_text() for exp in self.experience),
            ' '.join(proj.to_comparable_text() for proj in self.projects),
            ' '.join(ed.to_comparable_text() for ed in self.projects)
        ])
