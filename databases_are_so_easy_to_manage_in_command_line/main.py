import sys
import peewee
import json
from playhouse.shortcuts import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from peewee import *
from peewee import fn
from models import *

commands = ['create','print','insert','delete','print_batch_by_school','print_student_by_batch','print_student_by_school','print_family','age_average','change_batch','print_all','note_average_by_student','note_average_by_batch','note_average_by_school', 'top_batch','top_school','export_json','import_json']
args = sys.argv
modelnames=['school','batch','user','student','exercise']

def create_tables():
    my_models_db.connect()
    my_models_db.create_tables([School, Batch, User, Student,Exercise])

def print_table():
    if args[2] in modelnames:
        if args[2] == 'school':
            schools = School.select()
            for school in schools:
                print str(school)
        if args[2] == 'batch':
            batches = Batch.select()
            for batch in batches:
                print str(batch)
        if args[2] == 'student':
            students = Student.select()
            for student in students:
                print str(student)
        if args[2] == 'exercise':
            exercise = Exercise.select()
            for exercise in Exercises:
                print str(exercise)

def insert_tables():
    try:
        with my_models_db.transaction():
            if args[2] in modelnames:
                if args[2] == 'school':
                    school = School.create(name=args[3])
                    print "New school: "+str(school)
                if args[2] == 'batch':
                    batch = Batch.create(school=args[3],name=args[4])
                    print "New batch: "+ str(batch)
                if args[2] == 'student':
                    if len(args) == 7:
                        student = Student.create(batch = int(args[3]),first_name = args[6],last_name=args[5],age = int(args[4]))
                    else:
                        student = Student.create(batch = int(args[3]),last_name=args[5],age = int(args[4]))                            
                    print "New Student "+str(student)
                if args[2] == "exercise":
                    exercise =  Exercise.create(student=args[3], subject=args[4], note=args[5])
                    print "New Exercise: %s" % str(exercise)
    except peewee.IntegrityError:
        print 'error'

def delete_By_Id() :
    if args[2] in modelnames:
        if args[2] == "school":
            query = School.select().where(Schools.id == args[3])
            if query.exists():
                target = query.get()
                School.delete().where(School.id == args[3]).execute()
                print "Delete: " + str(target)
            else:
                print "Nothing to delete"
        elif args[2] == "batch":
            query = Batch.select().where(Batch.id == args[3])
            if query.exists():
                target = query.get()
                Batch.delete().where(Batch.id == args[3]).execute()
                print "Delete: " + str(target)
            else:
                print "Nothing to delete"
        elif args[2] == "student":
            query = Student.select().where(Student.id == args[3])
            if query.exists():
                target = query.get()
                Student.delete().where(Student.id == args[3]).execute()
                print "Delete: " + str(target)
            else:
                print "Nothing to delete"
        elif args[2] == "exercise":
            query = Exercise.select().where(Exercise.id == args[3])
            if query.exists():
                target = query.get()
                Exercise.delete().where(Exercise.id == args[3]).execute()
                print "Delete: " + str(target)
            else:
                print "Nothing to delete"

def print_batch_by_school():
    query = School.select().where(School.id == args[2])
    if query.exists():
        school = query.get()
        batch = Batch.select().where(Batch.school_id == school.id).get()
        print str(batch)
    else:
        print "School not found"
    
def print_students_by_batch():
    query = Batch.select().where(Batch.id == args[2])
    if query.exists():
        batch = query.get()
        students = Student.select().where(Student.batch_id == batch.id).execute()
        for student in students:
            print str(student)
    else:
        print "Batch not found"
    
def print_students_by_school():
    query = School.select().where(School.id == args[2])
    if query.exists():
        school = query.get()
        students = Student.select().join(Batch, on=(Student.batch_id == Batch.id)).join(School, on=(School.id,Batch.school_id)).where(School.id==school.id).execute()
        for student in students:
            print str(student)
    else:
        print "School not found"

def print_family():
    students = Student.select().where(Student.last_name==args[2]).execute()
    for student in students:
            print str(student)

def age_average():
    if len(args) == 3:
        batch = Batch.select().where(Batch.id == args[2]).get()
        age = Student.select(fn.Avg(Student.age)).where(Student.batch_id == batch.id).scalar()
        print str(age)
    else:
        age = Student.select(fn.Avg(Student.age)).scalar()
        print str(int(age))


def change_batch():
    try:
        student =  Student.get(Student.id == args[2])
        batch = Batch.get(Batch.id == args[3])
        if Student.select().where(Student.id == args[2], Student.batch == args[3]).exists():
            print "%s already in %s" % (str(student),str(batch))
        else:
            print "%s had been move to %s" % (str(student),str( batch))
            student.batch = args[3]
            student.save()        
    except Student.DoesNotExist:
        print 'Student not found'
    except Batch.DoesNotExist:
        print 'Batch not found'

def print_all():
    schools = School.select()
    for school in schools:
        print school
        batches = Batch.select().where(Batch.school == school.id)
        for batch in batches:
            print "\t", batch
            students = Student.select().join(Batch).where(Batch.school == school.id, Student.batch == batch.id)
            for student in students:
                print "\t\t", student
                exercises = Exercise.select().where(Exercise.student == student.id)
                for exercise in exercises:
                    print "\t\t\t", exercise


def note_average_by_student():
    if len(args) != 3:
        return

    try:
        student = Student.get(Student.id == args[2])
    except Student.DoesNotExist:
        print "Student not found"
        return

    subjects = Exercise.select().where(Exercise.student == args[2]).group_by(Exercise.subject)
    for subject in subjects:
        avg = Exercise.select(fn.Avg(Exercise.note)).where(Exercise.student == args[2], Exercise.subject == subject.subject).scalar()
        print "%s: %g" % (subject.subject,avg )

def note_average_by_batch():
    if len(args) != 3:
        return

    try:
        tmp = Batch.get(Batch.id == args[2])
    except Batch.DoesNotExist:
        print "Batch not found"
        return

    subjects = Exercise.select(Exercise.subject).join(Student).where(Student.batch == args[2]).group_by(Exercise.subject)

    for subject in subjects:
        avg = Exercise.select(fn.Avg(Exercise.note)).join(Student, on=Exercise.student).where(Student.batch == args[2], Exercise.subject == subject.subject).scalar()
        print "%s: %g" % (subject.subject, avg)


def note_average_by_school():
    if len(args) != 3:
        return

    try:
        tmp = School.get(School.id == args[2])
    except School.DoesNotExist:
        print "School not found"
        return

    subjects = (Exercise.select(Exercise.subject).join(Student, on=Exercise.student).join(Batch, on=Student.batch).where(Batch.school == args[2])
        .group_by(Exercise.subject))

    for subject in subjects:
        avg = subject.select(fn.Avg(Exercise.note)).where(Exercise.subject == subject.subject).scalar()
        print "%s: %g" % (subject.subject, avg)
 
def top_batch():
    if len(args) == 3:
        try:
            batch = Batch.get(Batch.id == args[2])
            students =Student.select(Student).join(Exercise,on=Exercise.student).where(Student.batch == batch).group_by(Student.batch).having(Exercise.note == fn.MAX(Exercise.note))
            for student in students:
                print "%s" % (student)
        except Batch.DoesNotExist:
            print "Batch not found"
    elif len(args) == 4:
        try:
            batch = Batch.get(Batch.id == args[2])
            students =Student.select(Student).join(Exercise,on=Exercise.student).where(Student.batch == batch, Exercise.subject==args[3]).group_by(Student.batch).having(Exercise.note == fn.MAX(Exercise.note))
            for student in students:
                print "%s" % (student)
        except Batch.DoesNotExist:
            print "Batch not found"
            return
    
def top_school():
    if len(args) == 3:
        try:
            school = School.get(School.id == args[2])
            students =Student.select(Student).join(Batch,on=Student.batch).join(Exercise,on=Exercise.student).where(Batch.school == school).group_by(Batch.school).having(Exercise.note == fn.MAX(Exercise.note))
            for student in students:
                print "%s" % (student)
        except School.DoesNotExist:
            print "School not found"
    elif len(args) == 4:
        try:
            school = School.get(School.id == args[2])
            students =Student.select(Student).join(Batch,on=Student.batch).join(Exercise,on=Exercise.student).where(Batch.school == school, Exercise.subject==args[3]).group_by(Batch.school).having(Exercise.note == fn.MAX(Exercise.note))
            for student in students:
                print "%s" % (student)
        except School.DoesNotExist:
            print "School not found"
            return

def export_json():
    schools = School.select()
    sys.stdout.write('[')
    jsonschools =[]
    for school in schools:
        jsonschools.append(json.dumps(model_to_dict(school,recurse=True, backrefs=True,exclude=[Exercise.id,School.id,Student.id,Batch.id])))
    sys.stdout.write(",".join(jsonschools))
    print ']'

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True

def import_json():
    if is_json(args[2]):
        for x in json.loads(args[2]):
            school = dict_to_model(School,x,ignore_unknown=False)
            school.save()
            for batch in school.batches:
                batch.save()
                for student in batch.students:
                    student.save()
                    for exercise in student.exercises:
                        exercise.save()

    else:
        print 'Please set a JSON string'

    
if len(args)<2:
    print 'Please enter an action'
elif args[1] not in commands:
    print 'Undefined action '+args[1]
else:
    if args[1]=='create':
        create_tables()
    elif args[1]=='print' and len(args) == 3 :
        print_table()
    elif args[1] == 'insert' and len(args) >= 3:
        insert_tables()
    elif args[1] == 'delete' and len(args) >= 3:
        delete_By_Id()
    elif args[1] == 'print_batch_by_school':
        print_batch_by_school()
    elif args[1] == 'print_student_by_batch':
        print_students_by_batch()
    elif args[1] == 'print_student_by_school':
        print_students_by_school()
    elif args[1] == 'print_family':
        print_family()
    elif args[1] == 'age_average':
        age_average()
    elif args[1] == 'change_batch':
        change_batch()
    elif args[1] == 'print_all':
        print_all()
    elif args[1] == 'note_average_by_student':
        note_average_by_student()
    elif args[1] == 'note_average_by_batch':
        note_average_by_batch()
    elif args[1] == 'note_average_by_school':
        note_average_by_school()
    elif args[1] == 'top_batch':
        top_batch()
    elif args[1] == 'top_school':
        top_school() 
    elif args[1] == 'export_json':
        export_json()
    elif args[1] == 'import_json':
        import_json()
