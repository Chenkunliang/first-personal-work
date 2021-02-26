{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from wordcloud import WordCloud\n",
    "import PIL.Image as image\n",
    "import numpy as np\n",
    "import jieba\n",
    "\n",
    "# 分词\n",
    "def trans_CN(text):\n",
    "    # 接收分词的字符串\n",
    "    word_list = jieba.cut(text)\n",
    "    # 分词后在单独个体之间加上空格\n",
    "    result = \" \".join(word_list)\n",
    "    return result\n",
    "\n",
    "with open(\"comment.txt\", encoding='utf-8') as fp:\n",
    "    text = fp.read()\n",
    "    # print(text)\n",
    "    # 将读取的中文文档进行分词\n",
    "    text = trans_CN(text)\n",
    "\n",
    "    mask = np.array(image.open(\"111.jpg\"))\n",
    "    wordcloud = WordCloud(\n",
    "        # 添加遮罩层\n",
    "        mask=mask,\n",
    "        background_color='white',\n",
    "        font_path = \"simkai.ttf\"\n",
    "    ).generate(text)\n",
    "    image_produce = wordcloud.to_image()\n",
    "    wordcloud.to_file('cy.png')\n",
    "    image_produce.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
