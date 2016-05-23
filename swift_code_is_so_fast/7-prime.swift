//
//  7-prime.swift
//  
//
//  Created by Sravanthi Rani Sinha on 5/23/16.
//
//

func is_prime(number: Int) -> (Bool)
{
    for i in 2...number/2 {
       if(number%i == 0){
            return false
        }
    }
    return true
}
