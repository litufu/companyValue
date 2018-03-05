# _author : litufu
# date : 2018/3/4

def english_to_abb(origin_words):
    '''

    :param origin_words: 输入的原始单词
    :return: 返回的英语缩写，用于字段或变量名称
    '''
    del_letter = ['a','e','i','o','u',"'"]
    alter_letter = ['-',':','&']
    words = origin_words.split(' ')
    #去除在del_letter中的字符,将alter_letter中的字符替换成下划线
    new_words = []
    for word in words:
        new_word = [word[0].lower(),]
        for letter in word[1:len(word)]:
            if letter not in del_letter:
                if letter in alter_letter:
                    letter = '_'
                new_word.append(letter)

        #去除响铃重复字母
        new_word2 = []
        for i in range(0,len(new_word)-1):
            if new_word[i] == new_word[i+1]:
                pass
            else:
                new_word2.append((new_word[i]))
        new_word2.append(new_word[len(new_word)-1])

        word = ''.join(new_word2)
        new_words.append(word)
    newwords = '_'.join(new_words)

    return newwords


if __name__ == '__main__':
    while True:
        words = input('>>>')
        print(english_to_abb(words))


