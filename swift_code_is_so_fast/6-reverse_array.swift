//
//  6-reverse_array.swift
//  
//
//  Created by Sravanthi Rani Sinha on 5/23/16.
//
//
func swapTwoInts(inout a: Int,  inout _ b: Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}

func reverse_array(a: [Int]) -> ([Int]){
  /*  for i in 0...(a.count - 1 )/2{
        swapTwoInts(&a[i],&a[a.count-i])
        i+ = 1
    }*/
    return a.reverse()
}
