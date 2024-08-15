root_word_='Able','Disablement', 'Able', 'Mable', 'Disable', 'Bagel'
other_words='Disablement', 'Able', 'Mable', 'Disable', 'Bagel'

def single_root_words(root_word,*other_words):
    same_words = []
    for i in range (len(other_words)):
        if other_words[i].lower() in root_word.lower() or root_word.lower() in other_words[i].lower():
            same_words.append (other_words[i])
    print ('Ваш метод:','root_word=',root_word,same_words)

def single_root_words_(root_word,*other_words):
    same_words=[]
    for k in range (len(other_words)):
        if any (i in other_words[k].upper () for i in [root_word]) > 0:
            same_words.append (other_words[k])
        elif any (i in root_word for i in [other_words[k].upper()]) > 0:
            same_words.append (other_words[k])
    print( 'Мой метод:''root_word=',root_word,same_words)
for i in range(len(root_word_)):
    root_word=root_word_[i]
    single_root_words(root_word,*other_words)
    single_root_words_ (root_word.upper (), *other_words)