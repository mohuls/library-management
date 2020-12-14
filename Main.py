import admin, student, manage
from termcolor import colored

greet = """╭━━━━╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱ ╭━━━╮╭╮╱╱╱╱╱╭╮  
╰━━╮━┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱ ┃╭━╮┣╯╰╮╱╱╱╱┃┃  
╱╱╭╯╭╋┳━━━┳━━━┫┃╭━━╮ ┃╰━━╋╮╭╋━━┳━┫┃╭╮
╱╭╯╭╯┣╋━━┃┣━━┃┃┃┃┃━┫ ╰━━╮┃┃┃┃╭╮┃╭┫╰╯╯
╭╯━╰━┫┃┃━━┫┃━━┫╰┫┃━┫ ┃╰━╯┃┃╰┫╭╮┃┃┃╭╮╮
╰━━━━┻┻━━━┻━━━┻━┻━━╯ ╰━━━╯╰━┻╯╰┻╯╰╯╰╯"""
print(colored(greet, 'green', attrs=['bold', 'reverse']))
print(colored("   Welcome to Zizzle Stark Library   \n", 'green', attrs=['bold', 'reverse']))

print(colored("(1) Library administration.", 'cyan', attrs=['bold']))
print(colored("(2) Student Portal.", 'cyan', attrs=['bold']))
choice = int(input("Enter your choice: "))

if(choice == 1):
  login = admin.login()
  if login == 1:
    manage.library()
elif(choice == 2):
  login = student.login()
  if login == 1:
    manage.student()
