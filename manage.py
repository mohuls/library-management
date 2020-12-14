import db
from termcolor import colored

def library():
  print(colored("""->    (1) Show all the book catalog
->    (2) Browse all the books     
->    (3) Manage checkouts         """, "green", attrs=['reverse', 'bold']))

  choice = int(input("Enter your choice: "))
  if(choice == 1):
    catalog = 'non'
    db.zizzle.execute("SHOW TABLES LIKE 'catalog'")
    for x in db.zizzle:
      catalog = x[0]
    if(catalog == 'catalog'):
      print(colored("\nAll the books catalog:", "red", attrs=["bold", "reverse"]))
      sql = "SELECT * FROM catalog"
      db.zizzle.execute(sql)
      res = db.zizzle.fetchall()

      print(colored("id   name          total books", "cyan", attrs=["bold"]))
      print(colored("-------------------------------\n", "cyan", attrs=["bold"]))
      for x in res:
        print(colored(str(x[0]) + "   " + x[1] + "          " + str(x[2]) + " ", "green"))
      
      choice = input(colored("\nWant to create a new Catalog? (Y/n): ", "green", attrs=["bold", "reverse"]))
      if(choice == 'Y' or choice == 'y'):
        name = input("Enter catalog name: ")
        
        sql = "INSERT INTO catalog (name, total) VALUES (%s, %s)"
        val = (name, 0)
        db.zizzle.execute(sql, val)
        db.mydb.commit()
        print(colored("\nCatalog " + name + " was created!\n", "green", attrs=["bold"]))
        library()
      else:
        library()
    else:
      choice = input(colored("No book catalog was found. Want to create one? (Y/n): ", 'red', attrs=['bold', 'reverse']))
      if(choice == 'Y' or choice == 'y'):
        db.zizzle.execute("CREATE TABLE catalog (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, total INT NOT NULL)")
    
        name = input("Enter catalog name: ")
        sql = "INSERT INTO catalog (name, total) VALUES (%s, %s)"
        val = (name, 0)
        db.zizzle.execute(sql, val)
        db.mydb.commit()
        print(colored("\nCatalog " + name + " was created!", "green", attrs=["bold"]))
        library()
      else:
        library()
  elif(choice == 2):
    books = 'non'
    db.zizzle.execute("SHOW TABLES LIKE 'books'")
    for x in db.zizzle:
      books = x[0]
    if(books == 'books'):
      print(colored("\nAll the books:", "red", attrs=["bold", "reverse"]))
      sql = "SELECT * FROM books"
      db.zizzle.execute(sql)
      res = db.zizzle.fetchall()

      print(colored("id   name          catalog           checkout", "cyan", attrs=["bold"]))
      print(colored("--------------------------------------------\n", "cyan", attrs=["bold"]))
      for x in res:
        print(colored(str(x[0]) + "   " + x[1] + "         " + x[2] + "           " + str(x[3]), "green"))
        
      choice = input(colored("\nWant to add new one? (Y/n): ", 'red', attrs=['bold', 'reverse']))
      if(choice == 'Y' or choice == 'y'):
        name = input("Enter book name: ")
        print(colored("\nSelect a book catalog:", "red", attrs=["bold", "reverse"]))
        sql = "SELECT * FROM catalog"
        db.zizzle.execute(sql)
        res = db.zizzle.fetchall()
        print(colored("id   name          total books", "cyan", attrs=["bold"]))
        print(colored("-------------------------------\n", "cyan", attrs=["bold"]))
        for x in res:
          print(colored(str(x[0]) + "   " + x[1] + "          " + str(x[2]) + " ", "green"))
        
        catalog = int(input("Enter a catalog id: "))
        sql = "SELECT * FROM catalog WHERE id = '{}'".format(str(catalog))
        db.zizzle.execute(sql)
        cat = db.zizzle.fetchone()[0]

        sql1 = "SELECT name FROM catalog WHERE id = " + str(cat)
        db.zizzle.execute(sql1)
        cats = db.zizzle.fetchone()[0]
        if(cat == int(catalog)):
          sql = "INSERT INTO books(name, catalog, checkout) VALUES (%s, %s, %s)"
          val = (name, cats, 0)
          db.zizzle.execute(sql, val)
          db.mydb.commit()
          print(colored("\nBook " + name + " was added successfully in " + cats, "green", attrs=["bold"]))
          library()
        else:
          print(colored("\nThe book catalog with id " + str(catalog) + " not found", 'red', attrs=['bold']))
          library()
      else:
        print("\n")
        library()
    else:
      choice = input(colored("\nNo books was found. Want to add one? (Y/n): ", 'red', attrs=['bold', 'reverse']))
      if(choice == 'Y' or choice == 'y'):
        name = input("Enter book name: ")
        print(colored("\nSelect a book catalog:", "red", attrs=["bold", "reverse"]))
        sql = "SELECT * FROM catalog"
        db.zizzle.execute(sql)
        res = db.zizzle.fetchall()
        print(colored("id   name          total books", "cyan", attrs=["bold"]))
        print(colored("-------------------------------\n", "cyan", attrs=["bold"]))
        for x in res:
          print(colored(str(x[0]) + "   " + x[1] + "          " + str(x[2]) + " ", "green"))
        
        catalog = int(input("Enter a catalog id: "))
        sql = "SELECT * FROM catalog WHERE id = '{}'".format(str(catalog))
        db.zizzle.execute(sql)
        cat = db.zizzle.fetchone()[0]

        sql1 = "SELECT name FROM catalog WHERE id = " + str(cat)
        db.zizzle.execute(sql1)
        cats = db.zizzle.fetchone()[0]
        if(cat == int(catalog)):
          db.zizzle.execute("CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, catalog VARCHAR(255) NOT NULL, checkout INT NOT NULL)")
          sql = "INSERT INTO books(name, catalog, checkout) VALUES (%s, %s, %s)"
          val = (name, cats, 0)
          db.zizzle.execute(sql, val)
          db.mydb.commit()
          print(colored("\nBook " + name + " was added successfully in " + cats, "green", attrs=["bold"]))
          library()
        else:
          print(colored("\nThe book catalog with id " + str(catalog) + " not found", 'red', attrs=['bold']))
          library()
      else:
        library()
  elif(choice == 3):
    print("Checkouts!!")
    library()
  else:
    print(colored("Wrong input!", 'red', attrs=['bold']))
    library()

def student():
  print("Student")