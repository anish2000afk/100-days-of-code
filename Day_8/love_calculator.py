def calculate_love_score(name1, name2):
    count1, count2 = 0, 0
    name = (name1 + name2).lower()
    for i in name:
        if i in "true":
            count1 += 1
    for i in name:
        if i in "love":
            count2 += 1
    print(str(count1) + str(count2))


calculate_love_score("Angela Yu", "Jack Bauer")
