import time

import pymongo
import requests
from moudle.bili_Violating_user_info import User
#{'refresh_token': '25.82d9b211f176d6d97d688a79e6851fe9.315360000.1942886091.282335-24621329',
# 'expires_in': 2592000, 'session_key': '9mzdXvagf1+wi4CeRKzMHQsatuVe6gQX3vDb2KljnxlOa/emh7CmjbVp2VxFPNIXPhS5tSK27sRynId2oRA3U9+iwQHT5Q==',
# 'access_token': '24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329', 'scope': 'ai_custom_shuiguo59 ai_custom_SGUO59 ai_custom_wenben1233 ai_custom_abc12311 ai_custom_cmt_emo ai_custom_cmt_yypd ai_custom_cmt_ys public brain_all_scope easydl_mgr easydl_retail_mgr ai_custom_retail_image_stitch ai_custom_test_oversea easydl_pro_mgr wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base smartapp_mapp_dev_manage iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_
# 开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理 smartapp_component smartapp_search_plugin avatar_video_test', 'session_secret': 'c86d0dce207acb3dac60b58770bd201c'}
class Easydl():
    def __init__(self,community):
        self.emo_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/sentiment_cls/cmt_emo?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329"
        self.similar_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_matching/abc12311?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329"
        self.secrecy_url = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/cmt_ys?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329'
        self.rumor_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/cmt_rumos?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329"
        self.sense_url='https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/mingan?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329'
        self.advertise_url='https://aip.baidubce.com/rpc/2.0/ai_custom/v1/text_cls/guangg?access_token=24.e35f1b60f83efe3f5f7766f9252aff02.2592000.1630118091.282335-24621329'
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'Content-Type': 'application/json'
        }
        import datetime
        # date = str(datetime.date.today()).replace('-', '')
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # self.mydb = myclient['Bilibili']
        # print(self.mydb)
        # self.community=community
    def emo_request(self): #获取rumor-score
        # col = self.mydb[self.community]
        # print(col.find())
        for item in User.objects:
            if not item['emo_score']:
                print(item['content'])
                data={
                    'text':item['content']
                }
                resp=requests.post(self.emo_url,headers=self.header,json=data)
                time.sleep(0.5)
                resp_dic=resp.json()
                if resp_dic['results'][0]['name']=='positive':
                    name='1'
                else:
                    name='0'
                print(resp_dic)
                user=User.objects(name=str(item['name'])).first()
                user.update(
                    emo_score=name
                )



    def similar_request(self,text_a): #获取similar-score
        r = requests.session()
        for item in User.objects:
            if not item['similar_score'] and item['content'] != '':
                print(item['content'])
                data = {
                    'text_a': text_a,
                    'text_b': item['content']
                }
                resp = r.post(self.similar_url, headers=self.header, json=data)
                time.sleep(0.5)
                resp_dic = resp.json()
                if resp_dic['score'] >0.5:
                    name='1'
                else:
                    name='0'
                print(resp_dic)
                user = User.objects(name=str(item['name'])).first()
                user.update(
                    similar_score=name
                )


    def secrecy_request(self):  # 获取secrecy-score
        r = requests.session()
        for item in User.objects:
            if not item['secrecy_score'] and item['content'] !='':
                print(item['content'])
                data={
                    'text':item['content']
                }
                resp=r.post(self.secrecy_url,headers=self.header,json=data)
                time.sleep(0.5)
                resp_dic=resp.json()
                print(resp_dic)
                user=User.objects(name=str(item['name'])).first()
                user.update(
                    secrecy_score=resp_dic['results'][0]['name']
                )

    def rumor_request(self):  # 获取rumor-score
        r = requests.session()
        for item in User.objects:
            if not item['rumor_score'] and item['content'] !='':
                print(item['content'])
                data = {
                    'text': item['content']
                }
                resp = r.post(self.rumor_url, headers=self.header, json=data)
                time.sleep(0.5)
                resp_dic = resp.json()
                print(resp_dic)
                user = User.objects(name=str(item['name'])).first()
                user.update(
                    rumor_score=resp_dic['results'][0]['name']
                )

    def advertise_request(self):  # 获取advertise-score
        r = requests.session()
        for item in User.objects:
            if not item['advertise_score'] and item['content'] !='':
                print(item['content'],'222')
                data = {
                    'text': item['content']
                }
                print(item['content'])
                resp = r.post(self.advertise_url, headers=self.header, json=data)
                time.sleep(0.5)
                resp_dic = resp.json()
                print(resp_dic)
                user = User.objects(name=str(item['name'])).first()
                user.update(
                    advertise_score=resp_dic['results'][0]['name']
                )

    def sense_request(self,threshold):  # 获取sense-score
        r = requests.session()
        for item in User.objects:
            if not item['sense_score'] and item['content'] !='':
                data = {
                    'text': item['content'],
                    "threshold": threshold
                }
                print(item['content'])
                resp = r.post(self.sense_url, headers=self.header, json=data)
                time.sleep(0.1)
                resp_dic = resp.json()
                print(resp_dic)
                user = User.objects(name=str(item['name'])).first()
                user.update(
                    sense_score=resp_dic['results'][0]['name']
                )

    def search(self,percent):
        print(User.objects.count())
        user = User.objects.order_by("-index")[:int(User.objects.count() * percent)]
        print(int(User.objects.count() * percent))
        list_user=[]
        for u in user:
            list_user.append(u['name']+'     '+u['source']+'     '+str(round(u['index'],3))+'        '+u['content'] )
        return list_user
    def test(self):
        data = {
            'text': '哈哈哈哈哈哈哈哈',
            "threshold": 0.5
        }
        resp = requests.post(self.sense_url, headers=self.header, json=data)
        time.sleep(2)
        resp_dic = resp.json()
        print(resp_dic)

#
if __name__ == '__main__':
    s=Easydl(community="Bilibii")
    s.sense_request(0.5)
    #
    # print(User.objects.count())
    # user = User.objects.order_by("_id")[:4]
    # for u in user:
    #     print(u.)


    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    # host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=67PObkBZkERHPua4oHpzHaTI&client_secret=qTPCCPgbxdRX1ASbyA2mn6q7zYCXNwtD'
    # response = requests.get(host)
    # if response:
    #     print(response.json())