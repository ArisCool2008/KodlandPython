meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
}
word = input("enter weird word")
if word in meme_dict():
    print(meme_dict[word])
else:
    print("i dont know that word")
