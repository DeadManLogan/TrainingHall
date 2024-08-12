def lyrics_1(animals, sounds):
    for i in range(len(animals)):
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
        print(f"And on that farm he had a {animals[i]}, Ee-igh, Ee-igh, Oh!")
        print(f"With a {sounds[i]}, {sounds[i]} here and a {sounds[i]}, {sounds[i]} there.")
        print(f"Here a {sounds[i]}, there a {sounds[i]}, everywhere a {sounds[i]}, {sounds[i]}.")
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")

def exercise_1():
    animals = ['cow', 'dog', 'cat', 'frog', 'bee']
    sounds = ['moo', 'woof', 'meow', 'croak', 'buzzes']
    lyrics_1(animals, sounds)

def lyrics_2(activities):
    for i in range(len(activities)):
        print(f"""The ants go marching {i+1} by {i+1}, hurrah, hurrah
The ants go marching {i+1} by {i+1}, hurrah, hurrah
The ants go marching {i+1} by {i+1},
The little one stops to {activities[i]}
And they all go marching down to the ground
To get out of the rain, BOOM! BOOM! BOOM!
""")

def exercise_2():
    activities = ["suck his thumb", "tie his shoe", "climb a tree", "shut the door", "take a dive", 
                  "pick up sticks", "pray to heaven", "roller skate", "check the time", "shout 'The End'"]
    lyrics_2(activities)


exercise_2()