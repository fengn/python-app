# encoding=utf-8
import jieba
from collections import Counter

def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = file.read()
        all_words = jieba.cut(all_words)
        
        word_sum = 0
        word_counts = Counter()
        for word in all_words:
            if(len(word) >= 2):
                word_counts[word] += 1
            word_sum += 1
        print('\nTotal Words:', word_sum)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])

            
if __name__ == '__main__':
    count_words('三国演义.txt')