from bintreeFile import Bintree

swedish_bintree = Bintree()
with open("../Laboration 4 & 5/svenska.txt", "r", encoding ="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        if ordet in swedish_bintree:
            pass
        else:
            swedish_bintree.put(ordet)

english_bintree = Bintree()
with open("engelska.txt", "r") as engelskfil:
    for lines in engelskfil:
        for words in lines.split(" "):
            new = (words.replace(",","").replace(".","").replace('"',"").
                  replace("!","").replace("'s","").replace("-",""))
            all_eng_words = new.strip().lower()
            if all_eng_words in english_bintree:
                pass
            else:
                english_bintree.put(all_eng_words)
                if all_eng_words in swedish_bintree:
                    print(all_eng_words)


