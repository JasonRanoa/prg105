# Programming Practice 2.2 MadLibs
"""
Copy your initial program from Programming Practice 2.1 into a new
.py file. Modify the file to accept input from the user, assign the
input to a minimum of 8 variables, and use the variables in the output.
You are essentially creating a mad-libs game.
"""

# Program written by Julius Ranoa

print("Programming Practice 2.2 Madlibs")
print("Please enter words as prompted.")
vehicle = input("\tType of vehicle: ")
part_of_day = input("\tA part of a day: ")
virtue = input("\tVirtue: ")
emotion = input("\tEmotion: ")
sensory_organ = input("\tSensory organ: ")
character_type = input("\tCharacter type: ")
body_part = input("\tBody part: ")
hand_gesture = input("\tHand gesture: ")

print("Here are some song lyrics with a few words replaced.")
print("")

print("{}, Cover by Jonathan Young".format(hand_gesture))
print("Original by Kenshi Yonezu")
print("Selected Lyrics")
print()

print("Verse 1", "-" * 10)
print("Well, it's strange my {} is rememberin'".format(body_part))
print("How the {} flying overhead".format(vehicle))
print("Looks so effortless, but I cannot guess")
print("Why it lingers in my mind")
print("{} after this, I'm a crying mess".format(part_of_day))
print("And to be stronger now, my only wish")
print("So I can finally have the {}".format(virtue))
print("So I can reach on up to the sky")
print()

print("Chorus", "-" * 10)
print("I hear a voice a' calling, telling me to risk it")
print("Asking if I have been going the distance")
print("Singing with a {} that I cannot deny".format(emotion))
print("My {} are swollen with the tears that I've been crying"
      .format(sensory_organ))
print("But, to the rest of the world, ever smiling")
print("Singing for the courage that I'm dying to show!")
print("With my {} up when I say goodbye".format(hand_gesture))
print("Write a story of a {}!".format(character_type))
print()
