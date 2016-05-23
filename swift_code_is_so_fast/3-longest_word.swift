func longest_word(text: String) -> (String)
{
    var len:Int = 0
    var index:Int = 0
    
    var words = text.characters.split{$0 == " "}.map(String.init)
    
    for i in 0 ... (words.count-1) {
        
        if len < words[i].characters.count {
           index = i
           len = words[i].characters.count
        }
    }
    return words[index]
}
