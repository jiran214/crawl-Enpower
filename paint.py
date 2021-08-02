import matplotlib.pyplot as plt
from moudle.bili_Violating_user_info import User
import matplotlib
import pymongo
def tx_paint(bv_list,scorenum,label1,label2,xlabel,ylim,community,title):
    # 设置中文字体和负号正常显示
    score_list = ['emo_score', 'rumor_score', 'secrecy_score', 'similar_score', 'sense_score', 'advertise_score']
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False


    label_list = bv_list  # 横坐标刻度显示值

    num_list1 = []  # 纵坐标值1
    num_list2 = []  # 纵坐标值2
    for bv in bv_list:
        if scorenum==1:
            num_list1.append(User.objects(source=bv,emo_score='0').count())
            num_list2.append(User.objects(source=bv,emo_score= '1').count())
        if scorenum==2:
            num_list1.append(User.objects(source=bv,rumor_score='0').count())
            num_list2.append(User.objects(source=bv,rumor_score= '1').count())
        if scorenum==3:
            num_list1.append(User.objects(source=bv,secrecy_score='0').count())
            num_list2.append(User.objects(source=bv,secrecy_score = '1').count())
        if scorenum==4:
            num_list1.append(User.objects(source=bv,simlar_score='0').count())
            num_list2.append(User.objects(source=bv, simlar_score= '1').count())
        if scorenum==7:
            tx2_paint(bv_list=bv_list,ylim=int(ylim),title=title)
            return
        if scorenum==5:
            num_list1.append(User.objects(source=bv,advertise_score='0').count())
            num_list2.append(User.objects(source=bv, advertise_score= '1').count())
        if scorenum==6:
            num_list1.append(User.objects(source=bv,sense_score='0').count())
            num_list2.append(User.objects(source=bv, sense_score= '1').count())


    print(num_list1)
    print(num_list2)
    x = range(len(num_list1))
    """
    绘制条形图
    left:长条形中点横坐标
    height:长条形高度
    width:长条形宽度，默认值0.8
    label:为后面设置legend准备
    """
    rects1 = plt.bar(x=x, height=num_list1, width=0.4, alpha=0.8, color='red', label=label1)
    rects2 = plt.bar(x=[i + 0.4 for i in x], height=num_list2, width=0.4, color='green', label=label2)
    plt.ylim(0, int(ylim))     # y轴取值范围
    plt.ylabel("数量")
    """
    设置x轴刻度显示值
    参数一：中点坐标
    参数二：显示值
    """
    plt.xticks([index + 0.2 for index in x], label_list)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.legend()     # 设置题注
    # 编辑文本
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    for rect in rects2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    plt.show()

def tx2_paint(bv_list,ylim,title):

    label_list = bv_list  # 横坐标刻度显示值
    num_list1 = []  # 纵坐标值1
    num_list2 = []  # 纵坐标值2
    num_list3 = []  # 纵坐标值3
    num_list4 = []  # 纵坐标值4
    num_list5 = []  # 纵坐标值5
    list_=['emo_score','rumor_score','secrecy_score','similar_score','sense_score','advertise_score']
    list_index=[1,3,2,3,3,2]#权值
    for bv in bv_list:
        s=0
        a=0
        b=0
        c=0
        d=0
        for item in User.objects(source=bv):
            num=0
            indexs=0
            index=0
            for i in range(6):#索引
                if item[list_[i]]:
                    if item[list_[i]]!='0':
                        index=index+list_index[i]
                    indexs=index+list_index[i]
                    num=num+1
            user=User.objects(name=item['name']).first()
            user.update(
                index=index/num
            )
            #分值划分
            if index<=indexs*0.2:
                d=d+1
            elif index>indexs*0.2 and index<=indexs*0.4:
                c=c+1
            elif index>indexs*0.4 and index<=indexs*0.6:
                b=b+1
            elif index>indexs*0.6and index<=indexs*0.8:
                a=a+1
            else:
                user = User.objects(name=item['name']).first()
                user.update(
                    is_violation= True
                )
                s=s+1

            # if index>=indexs*x:
            #     col.update_one({"mid": item['mid']}, {"$set": {"[is_violation": True}})

        num_list1.append(d)
        num_list2.append(c)
        num_list3.append(b)
        num_list4.append(a)
        num_list5.append(s)
    x = range(len(num_list1))

    #从下到上
    rects1 = plt.bar(x=x, height=num_list1, width=0.5, alpha=0.8, color='red', label="D")
    rects2 = plt.bar(x=x, height=num_list2, width=0.5, alpha=0.8,color='blue', label="C", bottom=num_list1)
    rects3 = plt.bar(x=x, height=num_list3, width=0.5, alpha=0.8,color='green', label="B", bottom=num_list2)
    rects4 = plt.bar(x=x, height=num_list4, width=0.5, alpha=0.8,color='pink', label="A", bottom=num_list3)
    rects5 = plt.bar(x=x, height=num_list5, width=0.5,color='yellow', label="S", bottom=num_list4)
    plt.ylim(0, ylim)
    plt.ylabel("数量")
    plt.xticks(x, label_list)
    plt.xlabel("BV号")
    plt.title(title)
    plt.legend()
    plt.show()