ls = ['yo']
with open('yazkora.txt', 'r') as inp:
    with open('answer.txt', 'w') as out:
        text = inp.read().replace("\n", " ")
        sentences = text.split(".")
        for sentence in sentences:
            adj = str()
            words = sentence.split(' ')
            for word in words:
                if word[(len(word) - 2):len(word)] in ls:
                    adj += word + " "
            out.write(adj + "\n")
inp.close()
out.close()
