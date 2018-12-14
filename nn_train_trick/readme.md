#### 训练过程中出现 NaN
- 检查 data 中是否有NaN(np.any(np.isnan(data)))
- 调整学习率
  - 若学习率调为0，还出现NaN，说明网络有问题
  - 若学习率调为0，没有出现，说明跟学习率有关
- 将模型由GPU改为由CPU训练，说不定能给出不同的错误
- clip norm
- 检查是否有 np.log, cross_loss
