import sys
import peewee
from models import *

commands = ['create','print','insert','delete']
args = sys.argv
modelnames=['school','batch','user','student']


if len(args)<2:
    print 'Please enter an action'
elif args[1] not in commands:
    print 'Undefined action '+args[1]
else:
    if args[1]=='create':
        my_models_db.connect()
        my_models_db.create_tables([School, Batch, User, Student])

    elif args[1]=='print' and len(args) == 3 :
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

    elif args[1] == 'insert' and len(args) >= 3:
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
        except peewee.IntegrityError:
            print 'error'
    
    elif args[1] == 'delete' and len(args) >= 3:
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
    




