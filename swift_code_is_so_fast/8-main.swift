let strings = ["We", "Heart", "Swift"]

let string = strings.enumerate().reduce("",combine:{$0 + $1.element + ($1.index < strings.endIndex-1 ? " " : "") })

print(string)