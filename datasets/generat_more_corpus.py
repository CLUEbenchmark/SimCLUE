import json

def write_corpus(source_file, target_file):
    lines=open(source_file,'r').readlines() # [0:1000]
    target_object=open(target_file,'a')
    for i, line in enumerate(lines):
        # {"qid": "qid_5982723620932473219", "category": "教育/科学-理工学科-地球科学", "title": "人站在地球上为什么没有头朝下的感觉 ", "desc": "", "answer": "地球上重力作用一直是指向球心的，因此\r\n只要头远离球心，人们就回感到头朝上。"}
        json_data=json.loads(line.strip())
        title=json_data["title"].strip()
        if len(title)<40 and len(title)>4:
            # 需要移除句尾被截断的内容。如结尾的最后一个符号是“，。”后面的内容不要啦
            last_char=title[len(title)-1:]
            find1=title.find("。")
            find2=title.find("？")
            find3=title.find("，")
            find4 = title.find(",") # 毛孔粗大怎么办我脸上长豆豆,出油,额头,鼻子上,脸上都有毛孔,很
            # 以正常的符号结尾，或者没有符号
            if last_char in ["。","？","，","?",".",","] or (find1==-1 and find2==-1 and find3==-1 and find4==-1 and len(title)<20) :
                target_object.write(title + "\n")

            # 问一个问题请问，在新浪如何分享小说。我要详细的描述，谢谢。
            # 加布林的获得我是LM的，这月暗影马戏团是在BL那边，但我想做加布
            # 奔腾B50两个前门上面的小音箱不响放CD，只有4个喇叭不响。前门
            # 河北610能被辽大录取吗？我是河北一女生，今年考了610，能被辽
            # 刚开始玩模拟人生为什么起火后无法扑灭,走开也不行,最后要烧死?
            # 为什么很多人患白癜风长期治疗还没好
            # 我存在，你深深的脑海里这是什么歌？
            # 为什么每天睡觉之后肚子都会痛？求解
            # 少见的称号有哪些最少人有的帮忙下有哪些找谁接的也写下谢谢拉
            # 请教股票指数的问题请教各位:以前上证指数1800点左右好像就是最
            # 屠龙问题如果我去黑龙插剑未插成功这时我死了我这时退出团队那个黑龙
            # 是否怀孕我已经买了两次验孕棒来试了，但是结果都是一样的结果是，一
            # 那里有好的英语聊天室？
    target_object.close()

source_file='/Users/xuliang/downloads/baike_qa2019/baike_qa_train.json'
# target_file='/Users/xuliang/downloads/baike_qa2019/baike_corpus.txt'
target_file='/Users/xuliang/downloads/simclue_public_0125/simclue_public/corpus.txt'
write_corpus(source_file, target_file)

