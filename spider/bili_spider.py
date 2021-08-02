import re
import json
import requests
import moudle.bili_Violating_user_info as bili
class Bili_commentspider():
    def __init__(self,bv_list):
        self.bv_list = bv_list
        self.maxpage=10
        self.headers = {
            'referer': 'http://www.bilibili.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        self.item=[]
        self.comment_parse()
    def get_oid(self,bv):
        base_url='https://www.bilibili.com/video/%s'
        r = requests.get(base_url%bv, headers=self.headers)
        res = r.text
        patten = '</script><script>window.__INITIAL_STATE__={"aid":(\d*)'
        oid = re.findall(patten, res)[0]
        return oid

    def comment_parse(self):
        for bv in self.bv_list:
            page=1
            while True:
                comment_url = 'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&' \
                              'next=%d&type=1&oid=%s&mode=3&plat=2&_=1627223958211'

                resp= requests.get(url=comment_url%(page,self.get_oid(bv)),headers=self.headers)
                resp_dict=json.loads(resp.text)
                comments =resp_dict['data']['replies']
                for comment in comments:
                    user = bili.User()
                    user.source = bv
                    content = comment.get('content').get('message').replace('\n', '')
                    user.content = ''.join(re.findall(r'[\u4e00-\u9fa5]', content))
                    # # 将content保存到本地文件
                    # newfile = open('./putong_comment2.txt', 'a', encoding='utf-8')
                    # newfile.write(user.content + '\n')
                    # newfile.close
                    user.mid=comment.get('member').get('mid')
                    user.name=str(comment.get('member').get('uname'))
                    user.is_violation=False
                    user.save()
                if page==self.maxpage:
                    break
                else:
                    page=page+1
if __name__ == '__main__':
    list=[
        'BV1No4y1S7TT','BV1J54y1J7kD','BV1JU4y1n7AJ','BV1Yo4y1Q71P','BV1Jy4y1j79i','BV1tb4y1r7Wv','BV1bv411n7yN','BV1764y167Lp'
        ,'BV1qg411M7ND', 'BV1CU4y137FJ', 'BV1VB4y1K7eL', 'BV15L411p7M8' ,'BV1L64y1t7ks', 'BV1Wv411n7FK' ,
        'BV1iM4y1K7DH','BV1Xb4y1k714', 'BV1KL411p7PA'
    ]
    list=['BV13A411P7mi']
    s=Bili_commentspider(list)
