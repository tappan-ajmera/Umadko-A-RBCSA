from mongoengine import *
from .models import *

class cal_umadko:

    def add_student_info_demo(self):
        s = Student(id='11111',email_id = 'Jay@gmail.com',name = 'Jay',gender = 'Male',
                    contact='8464747',visa_status = 'F1')
        s.save()
        sk=Skills(stud_id='11111',skill_name = 'Java',skill_score=2.1,number_of_reviewers=0)
        sk.save()

    def fetch_data(self):
        for s in Student.objects:
            print(s.id)

    def cal_from_reviews(self,su_id,skill,score,reviewer_id,comment):
        flag=True
        sk=Skill_reviews(stud_id=su_id,skill_name=skill,score_reviewer=score,reviewer_id=reviewer_id,reviewer_comment=comment)
        sk.save()
        print(sk.reviewer_comment)
        print(sk.reviewer_id)
        for s in Skills.objects:
            if s.stud_id == su_id and s.skill_name == skill:
                temp_score=((s.skill_score*s.number_of_reviewers)+score)/(s.number_of_reviewers+1)
                s.skill_score=temp_score
                s.number_of_reviewers=s.number_of_reviewers+1
                s.save()
                print(s.number_of_reviewers)
                print(s.skill_score)
                flag=False
                break

        if flag:
            s_new=Skills(stud_id = su_id,skill_name = skill,skill_score=score,number_of_reviewers=1)
            print(s_new.stud_id)
            s_new.save()

    def cal_umadko(self,su_id):
        sum=0
        inc=0
        for s in Skills.objects(stud_id=su_id):
            print("TYpe of sum: " , type(sum))
            print("TYpe of : ", type(s.skill_score))
            sum=sum+s.skill_score
            inc+=1
        res=sum/inc
        res = round(res,3)
        for s in Student.objects(id=su_id):
            s.umadko=res
            s.save()
        print(res)
        return res

'''

def main():
    c=cal_umadko()
    #c.add_student_info_demo()
    c.fetch_data()
    c.cal_from_reviews('11111','Java',8,'55555',"Comment1")
    c.cal_from_reviews('11111', 'Python', 3, '55556', "Comment2")
    c.cal_from_reviews('11111', 'Python', 3, '55557', "Comment3")
    c.cal_umadko('11111')

if __name__=='__main__':
    main()

'''