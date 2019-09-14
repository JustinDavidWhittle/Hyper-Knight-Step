print("Hello!")

answer = input("Do you want to go on an adventure (type yes or no)? ")
if answer == "yes":
  print("Once upon a time...")
  #continue your story here using print and input statements
  planet = input("Give me a planet")
  print("Our story takes place in " + planet)
  answer = input("Do you want a Lightsaber or a Blaster (type Lightsaber or Blaster)? ")
  if answer == "Lightsaber":
    print("You meet an old man who gives you some blue prints")
    build = input("what Lightsaber type do you wish to bulid")
    print("You now have a " + build)


else answer == "Blaster":
  print("your a smuggler now")

print("The End")
else:
  print("Ok")
  
print("The end")