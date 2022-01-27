# -*- coding: utf-8 -*-

# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
from sentence_transformers import SentenceTransformer, SentencesDataset, InputExample, evaluation, losses
from torch.utils.data import DataLoader
import random
import json

"""
使用SimCLUE数据集，进一步调优sentence-transformer
定义训练和验证、加载的模型、损失函数，训练并保存模型
"""
def read_txt(input_file):
    """
    读取数据
    :param input_file: txt文件
    :return: [[text1, text2, int(label)], [text1, text2, int(label)]]
    """
    with open(input_file, 'r', encoding='utf8') as f:
        reader = f.readlines()
    lines = []
    for line in reader:
        json_data=json.loads(line.strip()) # {"sentence1": "英德是哪个省", "sentence2": "英德是哪个市的", "label": "0"}
        text1, text2, label = json_data['sentence1'],json_data['sentence2'],json_data['label']
        lines.append([text1, text2, int(label)])
    random.shuffle(lines)
    return lines

# 定义加载的模型
model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

train_datas = read_txt('./datasets/train_pair_1w.json') # 大规模训练可以改成train_pair.json
test_datas = read_txt('./datasets/dev.json')
train_size = len(train_datas)
eval_size = len(test_datas)
train_data = []
for idx in range(train_size):
    train_data.append(InputExample(texts=[train_datas[idx][0], train_datas[idx][1]], label=float(train_datas[idx][2])))

# 设置验证集 Define your evaluation examples
sentences1 = []
sentences2 = []
scores = []
labels = []
for ss in test_datas:
    sentences1.append(ss[0])
    sentences2.append(ss[1])
    labels.append(int(ss[2]))
evaluator = evaluation.BinaryClassificationEvaluator(sentences1, sentences2, labels)

# 定义训练集、加载数据集和训练的损失 Define your train dataset, the dataloader and the train loss
train_dataset = SentencesDataset(train_data, model)
train_dataloader = DataLoader(train_dataset, shuffle=True, batch_size=64) #64
train_loss = losses.CosineSimilarityLoss(model)

# 训练模型
model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=3, warmup_steps=100, evaluator=evaluator,
          evaluation_steps=100, output_path='./sentence_transformer_checkpoint')
