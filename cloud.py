import jieba
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from collections import Counter
# f = open('test.txt',encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

content = open('test.txt', 'r',encoding="utf-8").read()
jieba.set_dictionary('userdict_Mayday.txt')
words = jieba.cut(content, cut_all=False)

# for word in words:
#     print(word)

# 設定停用字詞 
# stopwords = {}.fromkeys(["也","但","來","個","再","的","和","是","有","更","會","可能","有何","從","對","就", '\n','越','為','這種','多','越來',' '])


# Sentence = jieba.cut_for_search(content) 
# # create a python dictionary
# hash = {}
# for item in Sentence:
 
#     if item in stopwords:
#         continue
    
#     if item in hash:
#         hash[item] += 1
#     else:
#         hash[item] = 1
 
# # 文字雲樣式設定
# wc = WordCloud(font_path="/Users/hsuanlee/Library/Fonts/NotoSansCJKtc-Regular.otf", #設置字體
#                background_color="white", #背景顏色
#                max_words = 2000 ,        #文字雲顯示最大詞數
#                stopwords=stopwords)      #停用字詞
 
# # 使用dictionary的內容產生文字雲
# wc.generate_from_frequencies(hash)
 
# # 視覺化呈現
# plt.imshow(wc)
# plt.axis("off")
# plt.figure(figsize=(20,10), dpi =200)
# plt.show()

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

#要分析的來源，這個範例是五月天20首歌
text_from_file_with_apath = open('test.txt', "r",encoding="utf-8").read()

#設定字典
jieba.set_dictionary('dict.txt')
#設定自訂的字典
# jieba.load_userdict('userdict_mayday.txt')

#設定停用詞
stops = {}.fromkeys(["也","但","來","個","再","的","和","是","有","更","會","可能","有何","從","對","就", '\n','越','為','這種','多','越來','，','。','?','(',')','6','8'])

#
#開始段詞與排序
#
terms = [t for t in jieba.cut(text_from_file_with_apath, cut_all=True) if t not in stops]
sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True) 

#中文繪圖需要中文字體，請自己從windows font目錄抓
#微軟正黑體
font = 'msjh.ttc'
#想要文字雲出現的圖示
# mask = np.array(Image.open("mayday_mask.png"))

#背景顏色預設黑色，改為白色
#其他參數請自行參考wordcloud
my_wordcloud = WordCloud(background_color="white",font_path=font,collocations=False, width=2400, height=2400, margin=2)  
my_wordcloud.generate_from_frequencies(frequencies=Counter(terms))

#產生圖片
plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(my_wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
#顯示用
plt.show()

#存檔用
#plt.savefig("Mayday_Wordcloud.png")
