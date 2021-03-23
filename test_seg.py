# encoding=utf-8
import jieba
from collections import Counter
import re

def count_words(path):
    with open(path, encoding='utf-8') as file:
        # 只保留中文、大小写字母和阿拉伯数字
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        #all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = re.sub(reg, '', file.read())
        #all_words = file.read()
        all_words = jieba.cut(all_words)
        
        word_sum = 0
        word_counts = Counter()
        for word in all_words:
            if(len(word) >= 2):
                word_counts[word] += 1
            word_sum += 1
        print('\nTotal Words:', len(word_counts)) #2个字以上的去重后的数量

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])

            
if __name__ == '__main__':
    count_words('三国演义.txt')