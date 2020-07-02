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
# jieba.set_dictionary('userdict_Mayday.txt')
words = jieba.cut(content, cut_all=False)

# for word in words:
#     print(word)

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import numpy as np
from collections import Counter

#要分析的來源
text_from_file_with_apath = open('test.txt', "r",encoding="utf-8").read()

#設定字典
jieba.set_dictionary('dict.txt')

#
#開始段詞與排序
#
# terms = [t for t in jieba.cut(text_from_file_with_apath, cut_all=True) if t not in stops]
# sorted(Counter(terms).items(), key=lambda x:x[1], reverse=True) 
termslist = jieba.cut(text_from_file_with_apath)
terms = " ".join(termslist)

#中文繪圖需要中文字體，請自己從windows font目錄抓
#微軟正黑體
font = 'msjh.ttc'
#想要文字雲出現的圖示
# mask = np.array(Image.open("mayday_mask.png"))

#背景顏色預設黑色，改為白色
my_wordcloud = WordCloud(background_color="white",font_path=font,collocations=False, width=2400, height=2400, margin=2)  
my_wordcloud.generate(terms)

#產生圖片
plt.figure( figsize=(20,10), facecolor='k')
plt.imshow(my_wordcloud,interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
#顯示用
plt.show()

#存檔用
#plt.savefig("Mayday_Wordcloud.png")
