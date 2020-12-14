import db, random, requests
from termcolor import colored
def login():
  db.zizzle.execute("SHOW TABLES LIKE 'user'")
  user = 'non'
  for x in db.zizzle:
    user = x[0]
  if(user == 'user'):
    print(colored("->  (1) Login to your user account.      ", 'green', attrs=['bold', 'reverse']))
    print(colored("->  (2) Forget user username or password.", 'green', attrs=['bold', 'reverse']))
    print(colored("->  (3) Create new User Account.         ", 'green', attrs=['bold', 'reverse']))

    choice = int(input("Enter your choice: "))
    if(choice == 1):
      username = input("Enter username: ")
      password = input("Enter password: ")
      sql = "SELECT * FROM user WHERE username = '{}' AND password = '{}'".format(username, password)
      db.zizzle.execute(sql)
      try:
        if(db.zizzle.fetchone()[1] == username):
          print(colored("\nLogged in as " + username, 'green', attrs=['bold', 'reverse']))
          return 1
      except TypeError:
        print(colored("\nWrong username or password entered. Try again!", 'red', attrs=['bold']))
        login()
    elif(choice == 2):
      forget()
    elif(choice == 3):
      newuser()
    else:
      print(colored("\nWrong choice. Try again", 'red', attrs=['bold']))
      login()
  else:
    print(colored("User account doesnt exist. Do you want to create user account?", "green", attrs=['bold', 'reverse']))
    choice = input("Enter your choice (Y/n): ")
    if(choice == 'Y' or choice == 'y'):  
      username = input("Enter user username: ")
      password = input("Enter user password: ")
      mobile = input("Enter user mobile (Varification required): ")
      try:
        print(colored("\nSending OTP...", 'grey', attrs=['bold']))
        otp = random.randint(10000, 99999)
        sotp = str(otp)
        api = ("https://services.smsq.global/sms/api?action=send-sms&api_key=aEJOTkRrenlJSGFqcUNJQ0lkZkQ=&to=88" + mobile + "&from=Non%20Masking&sms=Your%20Zizzle%20Stark%20Verification%20Code:%20" + sotp)
        x = requests.get(api)
        if(x.status_code == 200):
          print(colored("Verification code was sent to your mobile!", 'green', attrs=['bold', 'reverse']))
          verify = int(input("Enter the OTP: "))
          if(otp==verify):
            db.zizzle.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, mobile VARCHAR(11) NOT NULL)")
            sql = "INSERT INTO user (username, password, mobile) VALUES (%s, %s, %s)"
            values = (username, password, mobile)
            db.zizzle.execute(sql, values)
            db.mydb.commit()
            print(colored("Successfully registered!", 'green', attrs=['bold']))
            login()
          else:
            print(colored("\nWrong OTP Entered. Try again!\n", 'red', attrs=['bold']))
            login()
        else:
          print(colored("\nSomething went wrong. Try again later!!\n", 'red', attrs=['bold']))
          login()
      except ConnectionError:
        print(colored("\nProblems with your network. Please ensure your network is ok and try again!\n", 'red', attrs=['bold']))
        login()
    else:
      print("Exiting...")

def newuser():
  print(colored("\n\nCreate new user", 'red'))
  print(colored("This feature is under development", 'red'))
  login()
def forget():
  print(colored("""\n  To restore your password, you need to enter your phone number.
  A 5 digit verification code will be sent to your varified number.                  
  Enter the varification number to change your login credintial.                     """, "white", attrs=['bold', 'reverse']))
  mobile = input("Enter your zizzle verified mobile: ")
  try:
    sql =  "SELECT * FROM user WHERE mobile = {}".format(mobile)
    db.zizzle.execute(sql)
    res = db.zizzle.fetchone()[3]
    try:
      print(colored("\nSending OTP...", 'grey', attrs=['bold']))
      otp = random.randint(10000, 99999)
      sotp = str(otp)
      api = ("https://services.smsq.global/sms/api?action=send-sms&api_key=aEJOTkRrenlJSGFqcUNJQ0lkZkQ=&to=88" + mobile + "&from=Non%20Masking&sms=Your%20Zizzle%20Stark%20Verification%20Code:%20" + sotp)
      x = requests.get(api)
      if(x.status_code == 200):
        print(colored("\nVerification code was sent to your mobile!", 'green', attrs=['bold', 'reverse']))
        verify = int(input("Enter the OTP: "))
        if(otp==verify):
          new_username = input("Enter new username: ")
          new_password = input("Enter new password: ")
          sql = "UPDATE user SET username = '{}', password = '{}' WHERE mobile = '{}'".format(new_username, new_password, mobile)
          db.zizzle.execute(sql)
          db.mydb.commit()
          print(colored("\nNew user and password has been set.\n", 'green', attrs=['bold']))
          login()
        else:
          print(colored("\nWrong OTP Entered. Try again!\n", 'red', attrs=['bold']))
          login()
      else:
        print(colored("\nSomething went wrong. Try again later!!\n", 'red', attrs=['bold']))
        login()
    except ConnectionError:
      print(colored("\nProblems with your network. Please ensure your network is ok and try again!\n", 'red', attrs=['bold']))
      login()
  except TypeError:
    print(colored("\nNo account found regarding the number " + mobile, 'red', attrs=['bold', 'reverse']))
    login()
