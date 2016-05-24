//
//
//
//  Created by Sravanthi Rani Sinha on 5/24/16.
//
//


/*Describes a Person*/
class Person{
    
    var first_name : String
    var last_name : String
    var age : Int
    
    init(first_name: String, last_name: String, age: Int){
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    
    /*return the first_name and last_name joined by a space*/
    func fullName()-> String {
        return self.first_name+" "+self.last_name
    }
    
}


class School{
    
    var name:String
    var list_persons:[Person]
    
    init(name: String)
    {
        self.name = name
        self.list_persons = []
    }
    
    func addStudent(p: Person) -> Bool {
        
        if p is Student
        {
            list_persons.append(p)
            return true
        }
        else{
            return false
        }
    }
    
    func addMentor(p: Person) -> Bool {
        
        if p is Mentor
        {
            list_persons.append(p)
            return true
        }
        else{
            return false
        }
        
    }
    
    func listStudents() -> [Person]{
        var list_students :[Person] = []
        
        for person in list_persons{
            if person is Student{
                list_students.append(person)
            }
        }
       return list_students.sort({$0.age > $1.age})
    }
    
    func listMentors() -> [Person]{
        var list_mentors :[Person] = []
        
        for person in list_persons{
            if person is Mentor{
                list_mentors.append(person)
            }
        }
        return list_mentors.sort({$0.age > $1.age})
    }
    
    func listMentorsBySubject(subject:Subject) -> [Person]{
        var list_mentors_subjects :[Person] = []
        
        for person in list_persons{
            if person is Mentor{
               if let mentor = person as? Mentor
                {
                    if mentor.subject == subject {
                    list_mentors_subjects.append(person)
                    }
                }
            }
        }
        return list_mentors_subjects.sort({$0.age > $1.age})
    }
    

    
    
}

enum Subject: String{
    
   case Math, English, French, History
    
}


protocol Classify {
    func isStudent() -> Bool
}

class Mentor: Person, Classify {
    
    let subject:Subject
 
    
    init(first_name: String, last_name: String, age: Int, subject:Subject=Subject.Math){
       self.subject = subject
        super.init(first_name:first_name, last_name:last_name, age:age)
    }
    
    
    func isStudent() -> Bool{
        return false
    }
    
    func stringSubject() ->String{
        
        switch subject {
            
        case .Math:
            return "Math"
        case .English:
            return "English"
        case .French:
            return "French"
        case .History:
            return "History"
       
        }
        
    }
}


class Student: Person, Classify {
    
    func isStudent() -> Bool{
        return true
    }
    
}







