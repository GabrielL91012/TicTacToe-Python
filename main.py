counter = 0
coordinates = ["[1,1]", "[1,2]", "[1,3]", "[2,1]", "[2,2]", "[2,3]", "[3,1]", "[3,2]", "[3,3]"]
chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
start = input("Welcome to Tic Tac Toe! You can play by typing in coordinates for where you wish to place your symbol (e. g. [1,1] is top left. [1,3] is top right). 3 in a row wins! Type in the words \"enter\" to begin! \n")
if start != "enter":
  print("Incorrect response. Shutting down")
  
else:
  print(chart)
  while (coordinates[0] == coordinates[1] and coordinates[1] == coordinates[2]) or (coordinates[3] == coordinates[4] and coordinates[4] == coordinates[5]) or (coordinates[6] == coordinates[7] and coordinates[7] == coordinates[8]) or (coordinates[0] == coordinates[4] and coordinates[4] == coordinates[8]) or (coordinates[2] == coordinates[4] and coordinates[4] == coordinates[6]) or counter != 9:
    
    p1 = ""
    while p1 not in coordinates:
      p1 = input("Player 1 please enter coordinates")
      if p1 == coordinates[0]:
        if(coordinates[0] == "X" or coordinates[0] == "O"):
          print("This spot is already taken")
        else:
          coordinates[0] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[1]:
        if(coordinates[1] == "X" or coordinates[1] == "O"):
          print("This spot is already taken")
        else:
          coordinates[1] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[2]:
        if(coordinates[2] == "X" or coordinates[2] == "O"):
          print("This spot is already taken")
        else:
          coordinates[2] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          print(coordinates)
          counter += 1
          break
      
      elif p1 == coordinates[3]:
        if(coordinates[3] == "X" or coordinates[3] == "O"):
          print("This spot is already taken")
        else:
          coordinates[3] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[4]:
        if(coordinates[4] == "X" or coordinates[4] == "O"):
          print("This spot is already taken")
        else:
          coordinates[4] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[5]:
        if(coordinates[5] == "X" or coordinates[5] == "O"):
          print("This spot is already taken")
        else:
          coordinates[5] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[6]:
        if(coordinates[6] == "X" or coordinates[6] == "O"):
          print("This spot is already taken")
        else:
          coordinates[6] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[7]:
        if(coordinates[7] == "X" or coordinates[7] == "O"):
          print("This spot is already taken")
        else:
          coordinates[7] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p1 == coordinates[8]:
        if(coordinates[8] == "X" or coordinates[8] == "O"):
          print("This spot is already taken")
        else:
          coordinates[8] = "X"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      else:
        print("Incorrect Input.")
      
    if(counter == 9):
        break
    elif (coordinates[0] == "X" and coordinates[1] == "X" and coordinates[2] == "X") or (coordinates[3] == "X" and coordinates[4] == "X" and coordinates[5] == "X") or (coordinates[6] == "X" and coordinates[7] == "X" and coordinates[8] == "X") or (coordinates[0] == "X" and coordinates[4] == "X" and coordinates[8] == "X") or (coordinates[2] == "X" and coordinates[4] == "X" and coordinates[6] == "X"):
          print("Player 1 wins!")
          break
    else:
        p2 = ""
        
      
  
    p2 = ""
    while p2 not in coordinates: 
      p2 = input("Player 2 please enter coordinates")
      if p2 == coordinates[0]:
        if(coordinates[0] == "X" or coordinates[0] == "O"):
          print("This spot is already taken")
        else:
          coordinates[0] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break
      
      elif p2 == coordinates[1]:
    
        if(coordinates[1] == "X" or coordinates[1] == "O"):
          print("This spot is already taken")
        else:
          coordinates[1] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break

      
      elif p2 == coordinates[2]:
        if(coordinates[2] == "X" or coordinates[2] == "O"):
          print("This spot is already taken")
        else:
          coordinates[2] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break

      
      elif p2 == coordinates[3]:
        if(coordinates[3] == "X" or coordinates[3] == "O"):
          print("This spot is already taken")
        else:
          coordinates[3] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break

      
      elif p2 == coordinates[4]:
        if(coordinates[4] == "X" or coordinates[4] == "O"):
          print("This spot is already taken")
        else:
          coordinates[4] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break

      
      elif p2 == coordinates[5]:
        if(coordinates[5] == "X"or coordinates[5] == "O"):
          print("This spot is already taken")
        else:
          coordinates[5] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          counter += 1
          break

      
      elif p2 == coordinates[6]:
        if(coordinates[6] == "X" or coordinates[6] == "O"):
          print("This spot is already taken")
        else:
          coordinates[6] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
        print(chart)
        counter += 1
        break

      
      elif p2 == coordinates[7]:
        if(coordinates[7] == "X" or coordinates[7] == "O"):
          print("This spot is already taken")
        else:
          coordinates[7] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)
          break

      
      elif p2 == coordinates[8]:
        if(coordinates[8] == "X" or coordinates[8] == "O"):
          print("This spot is already taken")
        else:
          coordinates[8] = "O"
          chart = coordinates[0] + " " + coordinates[1] +  " " +coordinates[2] + "\n" + coordinates[3] +  " " + coordinates[4] +  " " + coordinates[5] + "\n" + coordinates[6] +  " " + coordinates[7] +  " " + coordinates[8]
          print(chart)

          break
      else:
        print("Incorrect Input. Ending")

    if counter == 9:
      print("Tie")
    elif (coordinates[0] == "O" and coordinates[1] == "O" and coordinates[2] == "O") or (coordinates[3] == "O" and coordinates[4] == "O" and coordinates[5] == "O") or (coordinates[6] == "O" and coordinates[7] == "O" and coordinates[8] == "O") or (coordinates[0] == "O" and coordinates[4] == "O" and coordinates[8] == "O") or (coordinates[2] == "O" and coordinates[4] == "O" and coordinates[6] == "O"):
      print("Player 2 wins!")
      break
    else:
      print("")
    