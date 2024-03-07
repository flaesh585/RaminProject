questions = ("height", "favourite_color", "favourite_actor", "university")
dictionary = dict()

# collecting information to the dictionary
for i in range(len(questions)):
    print("Input your ", questions[i])
    dictionary[questions[i]] = input()

#Output information of dictionary
for i in range(len(dictionary)):
    print(questions[i], " - ", dictionary[questions[i]])