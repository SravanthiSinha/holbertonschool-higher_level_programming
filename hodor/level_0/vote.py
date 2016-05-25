import mechanize #sudo pip install python-mechanize

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

for x in range(0,1024):
    hsbot = br.open("http://173.246.108.142/level0.php")
    
    br.select_form(nr=0) #the sign up form in github is in third position(search and sign in

    br["id"] = '37' #username for github

    sign_up = br.submit()
    print x
