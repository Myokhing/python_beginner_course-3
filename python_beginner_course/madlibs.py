# string concatenation (aka how to put strings together)
#suppose we want to create a string that says "subscribe to ---"
youtuber = "Ashin Indavudha" #some string variable
# a few way to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person:")
madlib = f"Computer programming is so {adj}! It makes me so excited all time because \ i love to {verb1}. stay hydrated and {verb2} like are {famous_person}!"
print(madlib)