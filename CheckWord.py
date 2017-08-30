from collections import Counter
import jieba.analyse
import codecs
import jieba.posseg as pseg
import os

class CheckWord(object):
    def __init__(self, pos="all", dicts_path="./userdict", out_path="./datacount/"):
        """pos:part of speech"""
        self.pos = pos
        self.dicts_path = dicts_path
        self._load_dicts(dicts_path)
        self.out_path = out_path
        # 需要排除的词性
        self.word_pos_exc = ["x", "m", "uj", "p", "c", "f"]

    def _load_dicts(self, dicts_path):
        """load all dicts"""
        for file in os.listdir(dicts_path):
            if file.endswith("dict.txt"):
                full_path = os.path.join(dicts_path, file)
                jieba.load_userdict(full_path)

    def count_pos(self, data):
        """part of speech count"""
        output_file = codecs.open(self.out_path + "poscount.txt", "w", encoding="gbk")
        # 利用posseg.cut进行分词可用flag获得词性
        data = pseg.cut(data)
        count = []
        for w in data:
            if w.flag not in self.word_pos_exc:
                count.append(w.flag.lower())
        data = dict(Counter(count))
        data_dict = sorted(data.items(), key=lambda item: item[1], reverse=True)
        # 写入datacount中
        for k, v in data_dict:
            output_file.write("%s,%d\n" % (k, v))
        return data

    def check_all_word(self, data):
        """check all word"""
        output_file = codecs.open(self.out_path+"wordcount.txt", "w", encoding="gbk")
        data = pseg.cut(data)
        count = []
        for w in data:
            if w.flag not in self.word_pos_exc:
                print(w.word, w.flag)
                count.append(w.word.lower())
        data = dict(Counter(count))
        data_dict = sorted(data.items(), key=lambda item: item[1], reverse=True)
        for k, v in data_dict:
            output_file.write("%s,%d\n" % (k, v))
        return data

    def check_pos(self, data):
        """check special part of speech"""
        wls_list = ['weblogic', 'wls']
        was_list = ['websphere', 'was']
        output_file = codecs.open(self.out_path+self.pos+"count.txt", "w", encoding="gbk")
        data = pseg.cut(data)
        count = []
        for w in data:
            if w.flag not in self.word_pos_exc and w.flag == self.pos:
                if w.word in wls_list:
                    count.append('weblogic')
                elif w.word in was_list:
                    count.append('websphere')
                else:
                    count.append(w.word.lower())
        data = dict(Counter(count))
        data_dict = sorted(data.items(), key=lambda item: item[1], reverse=True)
        for k, v in data_dict:
            output_file.write("%s,%d\n" % (k, v))
        return data

