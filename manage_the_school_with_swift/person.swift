//
//
//
//  Created by Sravanthi Rani Sinha on 5/24/16.
//
//


/*Describes a Person*/
class Person: CustomStringConvertible{
    
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
    
    var description: String{
        return fullName()
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
    
    func studentsAgeAverge() -> Int{
        
        let mentors = listStudents()
        let avg = mentors.reduce(0) {
            return $0 + $1.age/mentors.count
        }
        return avg
    }
   
    

    func mentorsAgeAverge() -> Int{
        
       let mentors = listMentors()
       let avg = mentors.reduce(0) {
            return $0 + $1.age/mentors.count
        }
        return avg
    }
    
    func average(subject: Subject) -> Float{
        
        var list_exercise_subjects :[Exercise] = []
        
        for person in listStudents(){
            if let student = person as? Student{
                for e in student.list_exercises{
                    if e.subject == subject{
                        list_exercise_subjects.append(e)
                    }
                }
            }
        }
      
        
        let avg = list_exercise_subjects.reduce(0) {
            return $0 + Float($1.note)/Float(list_exercise_subjects.count)
        }
        return avg
    }
    
    func averageAll() -> Float{
        var list_exercise_subjects :[Exercise] = []
        
        for person in listStudents(){
            if let student = person as? Student{
                for e in student.list_exercises{
                    list_exercise_subjects.append(e)
                }
            }
        }
        
        let avg = list_exercise_subjects.reduce(0) {
            return $0 + Float($1.note)/Float(list_exercise_subjects.count)
        }
        return avg
    }

}


enum Subject: String{
    
   case Math, English, French, History
    
}

class Exercise{
    
    var subject:Subject
    var note :Int
    
    init(subject: Subject){
      self.subject = subject
       self.note=0
    }
    
    func setNote(note: Int){
        
        if note < 0{
            self.note = 0
        }
        else if note > 10 {
            self.note = 10
        }
        else
        {
        self.note = note
        }
    }
    
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
    
    var list_exercises :[Exercise]
    
    override init(first_name: String, last_name: String, age: Int){
         self.list_exercises=[]
        super.init(first_name:first_name, last_name:last_name, age:age)
       
    }
    
    func isStudent() -> Bool{
        return true
    }
    
    
    func addNewNote(subject: Subject,_ note: Int){
       let e = Exercise(subject: subject)
        e.setNote(note)
       list_exercises.append(e)
    }
    
    func average(subject: Subject) -> Float{
        
        var list_exercise_subjects :[Exercise] = []
       
        for e in list_exercises{
            if e.subject == subject {
            list_exercise_subjects.append(e)
            }
        }
        
        let avg = list_exercise_subjects.reduce(0) {
            return $0 + Float($1.note)/Float(list_exercise_subjects.count)
        }
        return avg
    }
    
   func averageAll() -> Float{
        let avg = list_exercises.reduce(0) {
            return $0 + Float($1.note)/Float(list_exercises.count)
        }
        return avg
    }
}











