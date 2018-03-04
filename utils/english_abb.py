# _author : litufu
# date : 2018/3/4

def english_to_abb(origin_words):
    # origin_words = input('请输入你要转换的单词:')
    del_letter = ['a','e','i','o','u',"'"]
    alter_letter = ['-',':','&']
    words = origin_words.split(' ')
    new_words = []
    for word in words:
        new_word = [word[0].lower(),]
        for letter in word[1:len(word)]:
            if letter not in del_letter:
                if letter in alter_letter:
                    letter = '_'
                new_word.append(letter)
        word = ''.join(new_word)
        new_words.append(word)
    newwords = '_'.join(new_words)

    return newwords


if __name__ == '__main__':
    while True:
        words = input('>>>')
        print(english_to_abb(words))


