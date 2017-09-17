from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .cal_umadko import *
# Create your views here.

def index(request):
    return render(request, "umadko/index.html", {})

def register(request):

    return render(request, "umadko/register.html", {})

def form_ht(request):

    try:
        if request.method == "POST":
            name = request.POST["name"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            request.session["name"] = name
            request.session["password"] = password
            request.session["username"] = username
            print("Got these values: ", name, username, email, password)
        else:
            pass
    except Exception as e:
        html = "<html><body>Error occured %s.</body></html>" % e
        return HttpResponse(html)

    return render(request, "umadko/form.html", {"name":name})

def dashboard(request):

    try:
        if request.method == "POST":
            name = request.session["name"]
            password = request.session["password"]
            username = request.session["username"]
            email = request.POST["email"]
            dob = request.POST["DOB"]
            gender = request.POST["optionsRadios"]
            resume = request.FILES["resume"]
            tech = request.POST["techskills"]
            os = request.POST["os"]
            gpa = request.POST["gpa"]
            visa = request.POST["visa"]
            work_ex = request.POST["workex"]
            uni_name = request.POST["uni_name"]
            contact = request.POST["contact"]

            id = gen_id(request.session["name"].encode('utf-8'))

            request.session["id"] = id

            stud = Student(id=id,name=name,username= username, password = password, email_id = email,
                           gender=gender,contact=contact,dob=dob,uni_name=uni_name,visa_status = visa,
                           gpa=gpa,exp=work_ex,umadko=1234,resume=resume)
            stud.save()
    except Exception as e:
        html = "<html><body>Error occured %s.</body></html>" % e
        #return render(request,"umadko/dashboard.html",{})
        return HttpResponse(html)

    return render(request,"umadko/dashboard.html",{'name':request.session["name"]})


def gen_id(name):

    import hashlib
    hash_object = hashlib.sha512(name)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def chartindex(request):

    return render(request,"umadko/chart.html",{})

def tab_panel(request):

    return render(request,"umadko/tab-panel.html",{})

def table_func(request):

    return render(request,"umadko/table.html",{})


def submit_func(request):
    try:
        if request.method == "POST":
            tech1 = request.POST["tech1"]
            tech2 = request.POST["tech2"]
            tech3 = request.POST["tech3"]
            tech4 = request.POST["tech4"]
            tech5 = request.POST["tech5"]
            pro1 = request.POST["pro1"]
            pro2 = request.POST["pro2"]
            pro3 = request.POST["pro3"]
            pro4 = request.POST["pro4"]
            pro5 = request.POST["pro5"]
            review_id = request.POST["review_id"]
            stu_id = request.session["id"]
            c = cal_umadko()
            c.cal_from_reviews( su_id=stu_id, skill=tech1, score=float(pro1), reviewer_id=review_id, comment="Best")
            c.cal_from_reviews(su_id=stu_id, skill=tech2, score=float(pro2), reviewer_id=review_id, comment="Best")
            c.cal_from_reviews(su_id=stu_id, skill=tech3, score=float(pro3), reviewer_id=review_id, comment="Best")
            c.cal_from_reviews(su_id=stu_id, skill=tech4, score=float(pro4), reviewer_id=review_id, comment="Best")
            c.cal_from_reviews(su_id=stu_id, skill=tech5, score=float(pro5), reviewer_id=review_id, comment="Best")
            score = c.cal_umadko(stu_id)


    except Exception as e:
        html = "<html><body>Error occured %s.</body></html>" % e
        # return render(request,"umadko/dashboard.html",{})
        return HttpResponse(html)

    return render(request,"umadko/chart.html",{'score':score, 'name':request.session["name"]})

def skills_func(request):

    return render(request,"umadko/skills.html",{})



