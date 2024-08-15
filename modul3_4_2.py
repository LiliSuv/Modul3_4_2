

root_word='Able'
other_words='Disablement', 'Able', 'Mable', 'Disable', 'Bagel'

def single_root_words(root_word,*other_words):
    same_words = []
    for i in range (len(other_words)):
        if other_words[i].lower() in root_word.lower() or root_word.lower() in other_words[i].lower():
            same_words.append (other_words[i])
    print (same_words)
single_root_words(root_word,*other_words)


