import torch
import os

PAD_token = 0  # 表示padding
SOS_token = 1  # 句子的开始
EOS_token = 2  # 句子的结束
MAX_LENGTH = 10  # 句子最大长度是10个词(包括EOS等特殊词)
save_dir = './save'

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

# loadFilename = r'./save\model\formatted_movie_lines\2-2_500\2500_checkpoint.tar'
loadFilename = None
corpus = './data/cornell movie-dialogs corpus/formatted_movie_lines.txt'
corpus_name = os.path.split(corpus)[-1].split('.')[0]

# 模型参数
model_name = 'model'
attn_model = 'dot'
# attn_model = 'general'
# attn_model = 'concat'
hidden_size = 500
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1
batch_size = 256
# batch_size = 64

# 训练相关和优化器参数
clip = 50.0
teacher_forcing_ratio = 1.0
learning_rate = 0.0001
decoder_learning_ratio = 5.0
n_iteration = 50000
print_every = 10
save_every = 500