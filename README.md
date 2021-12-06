<!--
 * @Author: CLUE
 * @Date: 2021-12-02 05:15:14
 * @LastEditTime: 2021-12-05 22:52:34
 * @LastEditors: Xiang Pan
 * @Description: 
 * @FilePath: /SimCLUE/README.md
 * @email: xiangpan@nyu.edu
-->
# SimCLUE

You can get the english version of [README](README_EN.md).

### 目标
提供一个大规模数据集，并使用对比学习、Prompt Learning与半监督学习等构建中文领域效果最好的预训练模型

### triclue数据集介绍
数据量：train(8313)/dev(1037)/test(1359)

sentence1和sentence2语义是一致的；sentence1和sentence3语义是不一致的，通用适用于sentence2和sentence3。


    例子：

    {"id": 0, "sentence1": "恩，方便提供一下您这个不可用资金的截图吗？辛苦您了", "sentence2": "方便提供一下这个不可用资金的截图吗？辛苦您了", "sentence3": "好，可以按一下这个箱子上的按钮吗？多谢"}
    {"id": 1, "sentence1": "大家觉得她好看吗", "sentence2": "你认为她丑吗", "sentence3": "大家觉得跑男好看吗？"}
    {"id": 2, "sentence1": "口袋妖怪逆鳞", "sentence2": "口袋妖怪逆鳞？", "sentence3": "火影忍者网游"}
    {"id": 3, "sentence1": "性格注定人的一生吗？", "sentence2": "性格决定人生吗？", "sentence3": "人生下来就决定命运了嘛"}

### 需要做的工作：

做一下实验，获得至少三个数据对比。可以使用对比学习等。

### 相关参考：

1、<a href='https://spaces.ac.cn/archives/8496'>R-Drop：又是Dropout两次！这次它做到了有监督任务的SOTA</a>

2、 <a href='https://mp.weixin.qq.com/s/Ttcxna3qa1ym1U__jmnwbQ'>超越SimCSE两个多点，Prompt+对比学习的文本表示新SOTA</a>
