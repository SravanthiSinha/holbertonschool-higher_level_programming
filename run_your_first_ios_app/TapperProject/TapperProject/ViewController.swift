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
    

        
    @IBAction func clickPlayButton(sender: UIButton) {
    
        let num = Int(textfield_number?.text ?? "")
        
        if num != nil {
            if num >= 0 {
            print("Let's do "+String(num)+" taps")
            }
        }
    
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

