//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Sravanthi Rani Sinha on 5/27/16.
//  Copyright © 2016 Sravanthi Rani Sinha. All rights reserved.
//

import Foundation


class EntitiesHelper{
    
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    static func getSchools() -> [Entity]!{
        if self.listOfSchool.isEmpty{
            self.listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
        return self.listOfSchool
    }
    
    static func getTechCompanies() -> [Entity]!
    {
        if self.listOfTechCompany.isEmpty{
            self.listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            self.listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            self.listOfSchool.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            self.listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
           self.listOfSchool.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            self.listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
        return self.listOfTechCompany
    }
    
    
    
    
}