# SimCLUE：3000000+中文语义理解与匹配数据集

You can get the english version of [README](README_EN.md).

### 简介
提供一个大规模语义数据集；可用于语义理解、语义相似度、召回与排序等检索场景等；作为通用语义数据集，用于训练中文领域基础语义模型。
可用于无监督对比学习、半监督学习、Prompt Learning等构建中文领域效果最好的预训练模型。

整合了中文领域绝大多数可用的开源的语义相似度和自然语言推理的数据集，并重新做了数据拆分和整理。

##### 数据集与数据量
    训练集（train_rank.json），三列，可用于排序模型：        389,370
    训练集（train_pair.json），句子对，用于分类或召回：      2,678,728
    验证集(dev.json)，用于验证：                           33,617
    测试集(test_public.json)，用于内部测试：                28,031
    语料库(corpus.json)，可用于无监督对比学习：              2,288,523
    正样本训练集（train_pair_postive.json），正样本句子对：  775,593

    其中，train_pair_postive.json源于train_pair.json，可用于批次内负采样 (in-batch negatives)形式的模型训练

##### 示例数据集

    示例（train_rank.json）：
    {"query": "胡子长得太快怎么办？", "title": "胡子长得快怎么办？", "neg_title": "怎样使胡子不浓密！"}
    {"query": "在香港哪里买手表好", "title": "香港买手表哪里好", "neg_title": "在杭州手机到哪里买"}
    {"query": "全职妈妈在家怎么赚钱？", "title": "全职妈妈在家上网做什么工作赚钱", "neg_title": "怎样在家挣钱？"}
    {"query": "她是一个非常慷慨的女人，拥有自己的一大笔财产。", "title": "她有很多钱，但她是个慷慨的女人。",
                                                         "neg_title": "百万富翁是由一个女人经营的。"}
    {"query": "明天多少度啊", "title": "明天气温多少度啊", "neg_title": "沈阳多少度"}
    
    示例（train_pair.json）：
    {"sentence1": "化妆水什么牌子的比较好？", "sentence2": "什么牌子的化妆水比较好呢？", "label": "1"}
    {"sentence1": "怀孕能吃圆葱吗", "sentence2": "怀孕能吃甲鱼吗", "label": "0"}
    {"sentence1": "两个人穿着工作服，正看着墙上插着的一根管子。", "sentence2": "两个人看着一根管子。", "label": "1"}
    
    
    示例（dev/test.json）：
    {"sentence1": "我没整懂啊", "sentence2": "没整明白", "label": "1"}
    {"sentence1": "北京特产什么茶", "sentence2": "北京特产是什么？", "label": "0"}
    
    示例（corpus.json）：
    我还有几天过生日
    不就是这么回事吗？
    女子撑竿跳高距离田径场不到75英里。
    杨幂胡歌到底是什么关系啊
    凡尼亚躺在席子底下一动不动。
    一群人走在一座雾蒙蒙的山脚下。
    花呗于期还款会怎样
    
    示例（train_pair_postive.json）：
    {"query": "很成功,我见过真正", "title": "事情完成得很圆满。"}
    {"query": "你在干什么？小波", "title": "小波在不在，你在不在"}
    {"query": "以后我就是你主人知道吗", "title": "听清以后我就是你主人了晓得不"}
    


在datasets目录下可以看到每个文件的前1万个数据，其中dev和test_public为全量。

下载链接：<a href='https://storage.googleapis.com/cluebenchmark/tasks/simclue_public.zip'>SimCLUE数据集</a>
    

### 预训练模型
使用simclue(260万训练集)在sentence-bert(distiluse-base-multilingual-cased-v1)上训练过的模型

下载链接：<a href='https://storage.googleapis.com/cluebenchmark/pretrained_models/sentencebert_simclue.zip'>sentencebert_simclue</a>

### triclue_small数据集介绍
数据量：train(8313)/dev(1037)/test(1359)

相对于规模较大的SimCLUE数据集，此数据集较小，可认为是train_rank的一个类似的小型数据集。

有三个句子sentence_0，sentence_1，sentence_2。当标签为1的时候那么sentence_0和sentence_1语义更近，；当标签为2的时候，sentence_0和sentence_2语义更近。

    例子：
    {"id": 3, "sentence_0": "性格注定人的一生吗？", "sentence_1": "人生下来就决定命运了嘛", "sentence_2": "性格决定人生吗？", "label": 2}
    {"id": 5, "sentence_0": "苹果手机信号不好", "sentence_1": "安卓手机信号很好", "sentence_2": "苹果手机信号不好…", "label": 2}
    {"id": 6, "sentence_0": "广州现在天气穿什么", "sentence_1": "现在广州什么天气", "sentence_2": "现在的广州天气要穿什么", "label": 2}
    {"id": 7, "sentence_0": "什么海鲜好吃？", "sentence_1": "什么海鲜好吃啊", "sentence_2": "什么奶茶好喝？", "label": 1}
    {"id": 8, "sentence_0": "议论文要怎么写", "sentence_1": "怎样写好议论文", "sentence_2": "说明文要怎么写", "label": 1}

### 效果对比

SimCLUE有什么用？
可以使用SimCLUE进行对比学习或作为通用数据训练模型，使得语义理解或搜索等相关场景模型具有较好的基础，并最终促进业务场景效果提升。

召回场景：语义检索场景，使用train_pair.json训练后，再使用业务数据训练，相对于直接业务训练，效果提升5个点（84%--->89%）。

排序场景：同一个语义检索场景，在召回基础上，进一步使用train_rank.json训练后，再使用业务排序数据训练模型，效果进一步提升2个点（92%--->94%）

### 整合的数据集列表

- <a href='http://icrc.hitsz.edu.cn/Article/show/171.html' target="_blank">哈工大 LCQMC 数据集</a>
- <a href='https://tianchi.aliyun.com/dataset/dataDetail?dataId=106411' target="_blank">AFQMC 蚂蚁金融语义相似度数据集</a>
- <a href='https://tianchi.aliyun.com/competition/entrance/531851/introduction' target="_blank">OPPO 小布对话文本语义匹配数据集</a>
- <a href='https://github.com/pkucoli/PKU-Paraphrase-Bank/' target="_blank">北大中文文本复述数据集 PKU-Paraphrase-Bank</a>
- <a href='https://github.com/pluto-junzeng/CNSD' target="_blank">Chinese-STS-B 数据集</a>
- <a href='https://github.com/CLUEbenchmark/CLUE' target="_blank">Chinese-MNLI 自然语言推理数据集</a>
- <a href='https://gitee.com/jiaodaxin/CNSD' target="_blank">Chinese-SNLI 自然语言推理数据集</a>
- <a href='https://github.com/CLUEbenchmark/OCNLI' target="_blank">OCNLI 中文原版自然语言推理数据集</a>
- <a href='https://www.heywhale.com/mw/dataset/608a8c45d0bc41001722dc37/content' target="_blank">CINLID 中文成语语义推理数据集</a>

整合了以上9个数据集，如有引用请见源数据集地址；这些项目的示例的介绍也可以参考<a href='https://github.com/zejunwang1/CSTS'>CSTS</a>

### 需要做的工作：

请报告你的实验效果，包括各种形式的无监督、半监督或业务学习上的效果对比，邮件到：CLUEbenchmark@163.com

### 交流与合作
     提交你的issue；加QQ群（群号:836811304）；或加入SimCLUE微信群：
   <img src="https://github.com/CLUEbenchmark/SimCLUE/blob/main/resources/img/simcluegroup.jpeg"  width="40%" height="40%" /> 

   <img src="https://github.com/CLUEbenchmark/SimCLUE/blob/main/resources/img/brightmart.jpeg"  width="40%" height="40%" /> 


### 相关参考或阅读：

1、<a href='https://github.com/zejunwang1/CSTS'>中文自然语言推理与语义相似度数据集</a>

2、<a href='https://arxiv.org/abs/2104.08821'>SimCSE: Simple Contrastive Learning of Sentence Embeddings</a>

3、<a href='https://github.com/PaddlePaddle/PaddleNLP/tree/develop/applications/neural_search'>手把手搭建一个语义检索系统(PaddleNLP)</a>

4、<a href='https://spaces.ac.cn/archives/8496'>R-Drop：又是Dropout两次！这次它做到了有监督任务的SOTA</a>

5、 <a href='https://mp.weixin.qq.com/s/Ttcxna3qa1ym1U__jmnwbQ'>超越SimCSE两个多点，Prompt+对比学习的文本表示新SOTA</a>

