# make a loop going to 999. temp>90,70,50,32, are the number in this program
temp=0
while temp<999:
              temp=int(input("Please enter current temperature"))
              if temp>90:
                  print("Wear Shorts")
              elif temp>70:
                  print("Short sleeves are fine")
              elif temp>50:
                  print("Wear a jacket")
              elif temp>32:
                  print("Wear a heavy coat")
            
              else : print("Stay Inside")
    
