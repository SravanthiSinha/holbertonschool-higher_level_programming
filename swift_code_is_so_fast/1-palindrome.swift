func is_palindrome(s: String) -> (Bool){
    
    let reversed = String(s.characters.reverse())
    
    if s == reversed{
        return true
    }
    else{
        return false
    }
    
}
