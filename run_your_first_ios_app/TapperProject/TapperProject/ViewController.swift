//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

   
    @IBOutlet weak var image_tapper: UIImageView!
   
    @IBOutlet weak var button_play: UIButton!
    
    
    @IBOutlet weak var textfield_number: UITextField!
    

    @IBOutlet weak var button_coin: UIButton!
    

    @IBOutlet weak var label_taps: UILabel!
    
    var taps_done :Int =  0
    var taps_requested:Int = 0
    
    func initGame(){
        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true
        label_taps.hidden = false
        button_coin.hidden = false
        taps_done =  0
        label_taps.text = "0 Taps"
    }
    
    
    func resetGame(){
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
        label_taps.hidden = true
        button_coin.hidden = true
        taps_requested = 0
        textfield_number.text = ""
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
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
 }

