class Ticket_Booking:
    
    def begin(self,movie,ticket,userid):
        self.movie=movie
        self.ticket=ticket
        self.userid=userid
        t.book(movie,ticket)
    
    def book(self,movie,ticket):
        if movie=='movie1':
            cost=50*ticket
            print(cost)
        
        elif movie=='movie2':
            cost=100*ticket
            print(cost)
        
        else:
            cost=150*ticket
            print(cost)
        print('Combo available')
        c=input("Combo you opt; yes or no")
        if c=='yes':
          print('needed combo')
          t.combo(cost)
          print("------------------------------------------------------")
        
        else:
          print('No Combo selected')
          print("-------------------------------------------------------")
          t.printDetails()

        
    
    def combo(self,cost):
      print("\n\n-------------------------------------------------------")
      print("Choose the combo: \n1.food pack:170 \n2. PopCorn:30 \n3. cool drinks:20")
      print("-------------------------------------------------------------")
      b=str(input('Enter your choice:'))
      if b == 'Food pack':
        totalcost=cost+170
        print("Total Cost:",totalcost)
        
      elif b=='PopCorn':
        totalcost=cost+30
        print("Total Cost:",totalcost)
        
      else:
        totalcost=cost+20
        print("Total Cost:",totalcost)

      t.BookDetails(b)
        
    def printDetails(self):
     print({userid:{movie:ticket}})


    def BookDetails(self,b):
      self.b=b
      print("Booked Details\n")  
      dict1={}
      dict1[userid]=({movie,ticket,self.b})
      print(dict1)
      t.tavail()

    def tavail(self):
       tavail=['1.movie1','2.movie2','3.movie']
       s={'1.movie1':20, '2.movie2':20,'3.movie3':20}
       sel=tavail[movie-1]
       s[sel]-=ticket
       print(s)

       
t=Ticket_Booking()
print('------------TICKET BOOKING-------------')
userid=str(input('Enter your id:'))
s={'1.movie1':20, '2.movie2':20,'3.movie3':20}
print('Available Movies:',s)
movie=int(input("Enter movie you want to book:"))
ticket=int(input("Number of tickets needed:"))  
print('---------------------------------------------------------')


t.begin(movie,ticket,userid)


OUTPUT-->
------------TICKET BOOKING-------------
Enter your id:shifana@gmail.com
Available Movies: {'1.movie1': 20, '2.movie2': 20, '3.movie3': 20}
Enter movie you want to book:1
Number of tickets needed:3
---------------------------------------------------------
450
Combo available
Combo you opt; yes or noyes
needed combo


-------------------------------------------------------
Choose the combo: 
1.food pack:170 
2. PopCorn:30 
3. cool drinks:20
-------------------------------------------------------------
Enter your choice:Food pack
Total Cost: 620
Booked Details

{'shifana@gmail.com': {1, 3, 'Food pack'}}
{'1.movie1': 17, '2.movie2': 20, '3.movie3': 20}
------------------------------------------------------
