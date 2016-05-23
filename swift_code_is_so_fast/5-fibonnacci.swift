//
//  5-fibonnacci.swift
//  
//
//  Created by Sravanthi Rani Sinha on 5/23/16.
//
//

func fibonacci(number: Int) -> (Int){
    if number == 1 || number == 2{
        return 1
    }
    else{
        return fibonacci(number-1)+fibonacci(number-2)
    }
}


