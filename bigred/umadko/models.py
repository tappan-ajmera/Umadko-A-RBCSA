from mongoengine import *


class Student(Document):
    id =StringField(primary_key=True)
    email_id = EmailField()
    name = StringField()
    gender = StringField()
    contact = StringField()
    dob = DateTimeField()
    uni_name = StringField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    visa_status = StringField()
    gpa = FloatField()
    exp = IntField()
    umadko = FloatField()
    resume = FileField()
    username = StringField()
    password = StringField()

class Skills(Document):
    stud_id = StringField(required=True)
    skill_name = StringField(primary_key=True,unique_with=('stud_id'))
    skill_score=FloatField()
    number_of_reviewers=IntField()

class Skill_reviews(Document):
    stud_id = StringField(required=True)
    skill_name = StringField(required=True)
    reviewer_id=StringField(primary_key=True,unique_with=('skill_name','stud_id'))
    score_reviewer=FloatField()
    reviewer_comment=StringField()

class Recruiter(Document):
    id = StringField(primary_key=True)
    email = EmailField()
    name = StringField()
    gender = StringField()
    dob = DateTimeField()
    contact = StringField()
    company = StringField()
    designation = StringField()
    umadko = FloatField()

class Professor(Document):
    id = StringField(primary_key=True)
    email = EmailField()
    name = StringField()
    gender = StringField()
    dob = DateTimeField()
    contact = StringField()
    umadko = FloatField()
    university = StringField()
    designation = StringField()




# from django.db import models

# Create your models here.


























'''
class Student(Document):
    id = StringField(primary_key=True)
    username = StringField()
    password = StringField()
    email_id = EmailField()
    name = StringField()
    gender = StringField()
    contact = StringField()
    dob = StringField()
    uni_name = StringField()
    visa_status = StringField()
    gpa = FloatField()
    exp = IntField()
    umadko = FloatField()
    resume = FileField()


class Skills(Document):
    stud_id = StringField()
    skill_name = StringField()
    skill_score=FloatField()
    number_of_reviewers=IntField()

class Skill_reviews(Document):
    stud_id = StringField()
    skills = DictField()
    reviewer_id=StringField()
    score_reviewer=FloatField()
    reviewer_comment=StringField()

class Recruiter(Document):
    id = StringField()
    email = EmailField()
    name = StringField()
    gender = StringField()
    dob = DateTimeField()
    contact = StringField()
    company = StringField()
    designation = StringField()
    umadko = FloatField()

class Professor(Document):
    id = StringField()
    email = EmailField()
    name = StringField()
    gender = StringField()
    dob = StringField()
    contact = StringField()
    umadko = FloatField()
    university = StringField()
    designation = StringField()

'''
