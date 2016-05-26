//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit
import Social

class ViewController: UIViewController,UITextFieldDelegate {

   
    @IBOutlet weak var image_tapper: UIImageView!
   
    @IBOutlet weak var button_play: UIButton!
    
    
    @IBOutlet weak var textfield_number: UITextField!
    
    @IBOutlet weak var timer: UILabel!

    @IBOutlet weak var button_coin: UIButton!
    
    @IBOutlet weak var tweetBurron: UIButton!

    @IBOutlet weak var label_taps: UILabel!
    
    var taps_done :Int =  0
    var taps_requested:Int = 0
  
    var startTime:NSTimeInterval = 0
    var endTime:NSTimeInterval = 0
    
    func initGame(){
        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true
        label_taps.hidden = false
        button_coin.hidden = false
        taps_done =  0
        label_taps.text = "0 Taps"
        timer.hidden = true
        tweetBurron.hidden = true
        startTimer()
    }
    
    func startTimer(){
        startTime = NSDate.timeIntervalSinceReferenceDate()
    }
    
    func endTimer(){
        endTime = NSDate.timeIntervalSinceReferenceDate()
    }
    
    func updateTimer(){
        var elapsedTime: NSTimeInterval = endTime - startTime
        
        //calculate the minutes in elapsed time.
        
        let minutes = UInt8(elapsedTime / 60.0)
        
        elapsedTime -= (NSTimeInterval(minutes) * 60)
        
        //calculate the seconds in elapsed time.
        
        let seconds = UInt8(elapsedTime)
        
        elapsedTime -= NSTimeInterval(seconds)
        
        //find out the fraction of milliseconds to be displayed.
        
        let fraction = UInt8(elapsedTime * 100)
        
        //add the leading zero for minutes, seconds and millseconds and store them as string constants
        
        let strMinutes = String(format: "%02d", minutes)
        let strSeconds = String(format: "%02d", seconds)
        let strFraction = String(format: "%02d", fraction)
        
        //concatenate minuets, seconds and milliseconds as assign it to the UILabel
        
        timer.text = "\(strMinutes):\(strSeconds):\(strFraction)"
        saveScore("\(strMinutes):\(strSeconds):\(strFraction)")
        
    }
    
    func saveScore(timervalue :String)
    {
      let filePath =  getDocumentsDirectory().stringByAppendingPathComponent("best_taps_score.txt")
        
        do {
            try timervalue.writeToFile(filePath, atomically: true, encoding: NSUTF8StringEncoding)
        } catch {
            print("write error")
        }
    }
    
    func getDocumentsDirectory() -> NSString {
        let paths = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)
        let documentsDirectory = paths[0]
        return documentsDirectory
    }
    
    func resetGame(){
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
        label_taps.hidden = true
        button_coin.hidden = true
        taps_requested = 0
        textfield_number.text = ""
        timer.text = ""
        timer.hidden = false
        tweetBurron.hidden = false
        endTimer()
        updateTimer()
    }
    
    func setTimerVlaue()
    {
        let filePath =  getDocumentsDirectory().stringByAppendingPathComponent("best_taps_score.txt")
        do{
            let timervalue = try NSString(contentsOfFile: filePath, encoding: NSASCIIStringEncoding)
            timer.text = timervalue as String
        
        } catch{
            print("read error")
        }
    }
    
    @IBAction func clickPlayButton(sender: UIButton) {
    
        let num = Int(textfield_number?.text ?? "")
        
        if num != nil {
            if num >= 0 {
            print("Let's do "+String(num)+" taps")
                taps_requested = num!
                initGame()
            }
        }
        
    }
 
    @IBAction func clickCoinButton(sender: UIButton) {
    
       if taps_done >= taps_requested{
             resetGame()
        }
        taps_done += 1
        label_taps.text = String(taps_done)+" taps"
        print("Tap!")

    }
    
    
    @IBAction func tweetPressed(sender: UIButton) {
     
        if SLComposeViewController.isAvailableForServiceType(SLServiceTypeTwitter) {
            
            let twitterShare:SLComposeViewController = SLComposeViewController(forServiceType: SLServiceTypeTwitter)
            
            let tweet = "My best time is "+timer.text! + " CheckOut the Tapper app created by @SravanthiSinha"
            twitterShare.setInitialText(tweet)
            
            self.presentViewController(twitterShare, animated: true, completion: nil)
            
        }
        else {
            let alert = UIAlertController(title: "Twitter Login Required", message: "Go to Settings -> twitter & login", preferredStyle: UIAlertControllerStyle.Alert)
            
            let okAction = UIAlertAction(title: "I Understood", style: UIAlertActionStyle.Default, handler: nil)
            
            alert.addAction(okAction)
            
            self.presentViewController(alert, animated: true, completion: nil)
            
        }
        
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        textfield_number.delegate = self
        setTimerVlaue()
    }
    
    func textFieldShouldReturn(textField: UITextField) -> Bool
    {
        textfield_number.resignFirstResponder()
        return true
    }
   
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
 }

