
"""
please fill in the code.
"""
import jieba
import wordcloud
from scipy.misc import imread
def main():
    f = open("cnText.txt", "r", encoding="utf-8").read()
    mask=imread('cat.jpg')
    txt = " ".join(jieba.lcut(f))
    W=wordcloud.WordCloud(mask=mask,font_path='STHUPO.TTF')
    W.generate(txt)
    W.to_file("cat2.jpg")

if __name__ == '__main__':
  main()
