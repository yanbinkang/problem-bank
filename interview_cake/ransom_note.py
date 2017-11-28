def can_make_ransom_note(ransom_note, magazine):
    if len(magazine) < len(ransom_note):
        return False

    if magazine == "" or ransom_note == "":
        return False

    ransom_list = ransom_note.split()
    magazine_list = magazine.split()
    ransom_dict = {}

    for word in ransom_list:
        if word in ransom_dict:
            ransom_dict[word] += 1
        else:
            ransom_dict[word] = 1

    i = 0
    while i < len(magazine_list):
        if magazine_list[i] in ransom_dict:
            if ransom_dict[magazine_list[i]] > 1:
                ransom_dict[magazine_list[i]] -= 1
            else:
                del ransom_dict[magazine_list[i]]
        i += 1

    if ransom_dict == {}:
        return True
    return False



magazine = "you better better hurry up or else you will see"
ransom_note = "you else up"

print can_make_ransom_note(ransom_note, magazine)
