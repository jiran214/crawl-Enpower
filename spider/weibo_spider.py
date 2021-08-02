# encoding:UTF-8
import re, time, requests, random, argparse
import pandas as pd
from pandas import Series, DataFrame
import moudle.weibo_Violating_user_info as weibo
import jieba
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
# from text_emotion import get_sentiment_score, count_sentiment
# import pymysql

# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False

# # 读取过滤词，用于生成词云
# stopwords = set([line.strip() for line in open('./dictionary/Chinese_stop_words.txt', 'r').readlines()])
# with open('cookie.txt', 'r') as f:
#     cookie = {'Cookie': f.readline().strip()}  # 读取cookie，用于模拟登陆微博，cookie存储在cookie.txt文件
# time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())  # 生成时间字符串


class WeiboCommentCrawer(object):
    def __init__(self, weibo_id_list):
        self.weibo_id = weibo_id  # 单条微博的id
        # self.cookie = cookie
        self.page_index = 0  # 评论的页码
        self.comment_list = []
        self.txt = ''
        self.txt_list = []
        self.score_list = []
        self.r_data = {}
        self.stop_flag = False
        self.data_frame = DataFrame(columns=['text', 'score', 'user', 'time'])  # 存储评论内容(微博id，文本，用户名，时间)
        self.weibo_id_list=weibo_id_list
        # self.hot_url = 'https://m.weibo.cn/comments/hotflow?id=' + self.weibo_id + '&mid=' + self.weibo_id + \
        #                '&max_id_type=0'  # 热门评论的网址(按热度排序)
        self.headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "cookie": "WEIBOCN_FROM=1110006030; loginScene=102003; SUB=_2A25N-gs0DeRhGeFO6FcW8S_NyDSIHXVvBJV8rDV6PUJbkdAKLWXEkW1NQWa2hYBzrsf--jxnbVDDR4W00zl77qiG; _T_WM=87552757618; XSRF-TOKEN=825c5d; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4663142787324503%26luicode%3D20000174%26uicode%3D20000174"
        }
    def crawl_comment(self):
        # 按时间顺序爬取评论内容
        base_url = 'https://m.weibo.cn/api/comments/show?id=%s' + '&page=%d'  # 评论地址（按时间）
        for id in self.weibo_id_list:
            page_index = 0
            while True:
                self.id=id
                url = base_url%(id,page_index)
                self.get_comment_from_url(url)
                max_num=500
                if len(self.comment_list) >= max_num or len(self.comment_list) >= self.r_data['total_number'] or self.stop_flag or page_index==50:
                    print(' -------------------')
                    print('| Finished crawling |')
                    print(' -------------------')
                    break
                time.sleep(random.randint(1, 3))  # 随机等待3-10秒，模拟人的操作
                page_index += 1  # 用于更新url
                print(page_index)
            # self.data_frame.to_csv('./weibo-comments-csv/{}-weibo.csv'.format(time_str))  # 存入csv

    def get_comment_from_url(self, url):
        # 爬取单个url的评论内容
        r = requests.get(url=url,headers=self.headers)
        r_data = r.json()['data']
        print(r_data)
        self.r_data = r_data
        comment_page = r_data['data']
        for j in range(len(comment_page)):
            comment = comment_page[j]
            comment_id = comment['id']
            print(comment_id)
            if comment_id not in self.comment_list:
                user = weibo.User()
                user.source = self.id
                user.comment_id=str(comment_id)
                self.comment_list.append(comment_id)
                user_name = comment['user']['screen_name']
                user.name=user_name
                comment_text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]',
                                      '',
                                      comment['text'])  # 滤除评论文本的emoji等内容
                user.content=comment_text
                user.is_violation=False
                user.save()

                # self.txt = self.txt + comment_text + ' '  # 评论文本，用于打印词云和情绪分析
                # score = get_sentiment_score(comment_text)
                # self.score_list.append(score)

                # series = Series([user_name, comment_time, comment_text, score],
                #                 index=['user', 'time', 'text', 'score'])
                # self.data_frame = self.data_frame.append(series, ignore_index=True)
                # self.save_to_mysql(comment_text, score, user_name, comment_time)  # 如不需要mysql，注释掉

                # print('第 {} / {} 条评论 '.format(str(len(self.comment_list)).zfill(4), self.r_data['total_number']),
                #       '|', str(score).center(5), '| ', comment_text, ' | ', user_name, ' | ',comment_time)

    # def plot_word_cloud(self):
    #     # 打印词云
    #     text = []
    #     for word in jieba.cut(self.txt):
    #         if word in stopwords:
    #             continue
    #         if len(word) < 2:
    #             continue
    #         text.append(word)
    #     text = ''.join(text)
    #     self.tags = jieba.analyse.extract_tags(text,
    #                                            topK=100,
    #                                            withWeight=True)
    #     tf = dict((a[0], a[1]) for a in self.tags)
    #     wc = WordCloud(
    #         background_color='white',
    #         font_path='C:\Windows\Fonts\STZHONGS.TTF',
    #         max_words=2000,  # 设置最大现实的字数
    #         stopwords=STOPWORDS,  # 设置停用词
    #         max_font_size=200,  # 设置字体最大值
    #         random_state=30,
    #         width=1080,
    #         height=720)
    #     wc.generate_from_frequencies(tf)
    #     plt.figure(1)
    #     plt.imshow(wc)
    #     plt.axis('off')
    #     plt.show()
    #
    # def get_text_emotion(self):
    #     pos_num, neg_num = count_sentiment(self.score_list)
    #     print('\n 积极评论数：{} | 消极评论数：{} \n'.format(pos_num, neg_num))
    #
    # def save_to_mysql(self, comment_text, score, user_name, comment_time):
    #     # 将数据保存到mysql数据库中，数据库的参数需要根据自己的情况设定
    #     # 如果不想使用数据库，可注释掉此部分
    #     comment_time = comment_time[:20] + comment_time[25:]
    #     comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(comment_time, "%a %b %d %H:%M:%S %Y"))
    #     connection = pymysql.connect(host='localhost',
    #                                  port=3306,
    #                                  user='root',
    #                                  password='root',
    #                                  db='weibo_crawler',
    #                                  charset='utf8')
    #     cursor = connection.cursor()
    #     sql = '''
    #           INSERT INTO  weibo_comments
    #           (comment, score, user_name, time)
    #           VALUES
    #           ('{}', {}, '{}', '{}')
    #           '''.format(comment_text, score, user_name, comment_time)
    #     cursor.execute(sql)
    #     connection.commit()
    #     connection.close()
    #
    # def visual_data(self, csv_path):
    #     # 读取csv文件的内容，并打印词云、分析词频(TF-IDF)
    #     frame = pd.read_csv(csv_path, index_col=0)
    #     txt_list = frame['text'].values
    #     self.txt = ' '.join(txt_list)
    #     plt.figure(1)
    #     self.plot_word_cloud()
    #     words = [i[0] for i in self.tags[0:10]]
    #     freq = [i[1] for i in self.tags[0:10]]
    #
    #     plt.figure(2)
    #     plt.bar(words, freq)
    #     plt.show()


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-n', '--comment_num', type=int, help='the number of comments you want',
    #                     default=100)
    # parser.add_argument('-id', '--weibo_id', type=str, help='the weibo id to be crawled',
    #                     default='4400832105676005')
    # args = parser.parse_args()
    #
    # comment_num = args.comment_num
    # weibo_id = args.weibo_id
    comment_num = 40
    weibo_id = ['4663143361679325']
    weibo_crawler = WeiboCommentCrawer(weibo_id)
    weibo_crawler.crawl_comment()
    # weibo_crawler.crawl_hot_comment()  # 抓取热门评论
    # weibo_crawler.plot_word_cloud()    # 打印词云
    # weibo_crawler.get_text_emotion()   # 分析评论情绪

    # csv_path = 'weibo-comments/20190801133207-weibo.csv'
    # weibo_crawler.visual_data(csv_path)


