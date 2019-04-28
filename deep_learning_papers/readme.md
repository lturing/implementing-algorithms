### general
- [Mixture density network](https://publications.aston.ac.uk/373/1/NCRG_94_004.pdf)
- [Numerical Coordinate Regression with Convolutional Neural Networks](https://arxiv.org/pdf/1801.07372.pdf)
- [non-local neural networks](https://arxiv.org/pdf/1711.07971.pdf)
- [network in networks](https://arxiv.org/pdf/1312.4400.pdf)
> the fully connected layers are prone to overfitting and heavily depend on dropout regularization, while global
average pooling is itself a structural regularizer, which natively prevents overfitting for the overall structure. 全连接神经网络的空间泛化能力不行(模型训练期间在一个位置获得得知识在推理阶段推广到另一个位置的能力, 比如训练集中图片中的气球在左上，拿一个气球在图片右下的图片，全连接不一定能检测到)

--------------------

### features fusing 
- concatenation
- element-wise product
- element-wise addition

* [Dynamic Fusion with Intra- and Inter-modality AttentionFlow for Visual Question Answering](https://arxiv.org/pdf/1812.05252.pdf)

---------------------------

### attention
1, content-based attention: a_i = Attend(s_{i-1}, h}, where s_{i-1} is the state of lstm and h is the output of encoder.  
2, location-based attention: a_i = Attend(s_{i-1}, a_{i-1}), where a_{i-1} is the previous attention alignment.   
3, hybrid attention: a_i = Attend(s_{i-1}, a_{i-1}, h)     

#### attention in computer vision
1, spatial attention: only consider the 2d h*w weight, and the weight will be broadcasted in c channels.      
2, channel attention: only consider the channel c weight, and the weight will be broadcasted in h and w.[ref](https://arxiv.org/pdf/1611.05594.pdf)        


- [Show, Attend and Tell: Neural Image Caption Generation with Visual Attention](https://arxiv.org/pdf/1502.03044.pdf)
- [Neural Turing Machines](https://arxiv.org/pdf/1410.5401.pdf)
- [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)
- [Attention-Based Models for Speech Recognition](https://arxiv.org/pdf/1506.07503.pdf)
- [neural machine translation by jointly learning to align and translate](https://arxiv.org/pdf/1409.0473.pdf)
- [weakly supervised memory networks](https://arxiv.org/pdf/1503.08895v2.pdf)
- [generating sequences with recurrent neural networks](https://arxiv.org/pdf/1308.0850.pdf)
- [multilingual hierarchical attention networks for document classification](https://arxiv.org/abs/1707.00896)
- [attention-over-attention neural networks for reading comprehension](https://arxiv.org/abs/1607.04423)
- [convolutional sequence to sequence learning](https://arxiv.org/abs/1705.03122)
- [attention-based models for speech recognition](https://arxiv.org/abs/1506.07503)
- [SCA-CNN: Spatial and Channel-wise Attention in Convolutional Networks for Image Captioning](https://arxiv.org/pdf/1611.05594.pdf)


----------------


### computer vision
- [focus loss for dense object detection](https://arxiv.org/pdf/1708.02002.pdf)
- [metaAnchor: learning to detect objects with customized anchors](http://papers.nips.cc/paper/7315-metaanchor-learning-to-detect-objects-with-customized-anchors.pdf)
- [Learning to Segment Every Thing](https://arxiv.org/pdf/1711.10370.pdf)
- [Spatial Transformer Networks](https://arxiv.org/pdf/1506.02025.pdf)
- [Inverse Compositional Spatial Transformer Networks](https://arxiv.org/pdf/1612.03897.pdf)
- [hyperNetworks](https://arxiv.org/pdf/1609.09106.pdf)
- [R-FCN: Object Detection via Region-based Fully Convolutional Networks](https://arxiv.org/pdf/1605.06409.pdf)
- [deformable convolutional networks](https://arxiv.org/pdf/1703.06211.pdf)
- [Deformable ConvNets v2: More Deformable, Better Results](https://arxiv.org/pdf/1811.11168.pdf)
- [what you get is what you see: a visual markup decompiler](https://arxiv.org/pdf/1609.04938v1.pdf)
- [show, attend and tell: neural image caption generation with visual attention](https://arxiv.org/pdf/1609.04938v1.pdf)
- [show and tell: lessons learned from the 2015 mscoco image captioning challenge](https://arxiv.org/pdf/1609.06647.pdf)
- [pixel recurrent neural networks](https://arxiv.org/pdf/1601.06759.pdf)
- [parallel multiscale autoregressive density estimation](https://arxiv.org/pdf/1703.03664.pdf)


### others
- [Learning to learn by gradient descent by gradient descent](https://arxiv.org/pdf/1606.04474.pdf)
- [Dynamic Routing Between Capsules](https://arxiv.org/pdf/1710.09829.pdf)
- [matrix capsule with em routing](https://openreview.net/pdf?id=HJWLfGWRb)


### NLP
- [sheduled sampling for sequence prediction with recurrent neural networks](https://arxiv.org/pdf/1506.03099.pdf)
- [Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translate](https://arxiv.org/pdf/1609.08144.pdf)
- [sequence-to-sequence learning as beam-search optimization](https://arxiv.org/pdf/1606.02960.pdf)
- [attention is all you need](https://arxiv.org/abs/1706.03762)
- [attending to mathematical language with transformers](https://arxiv.org/ftp/arxiv/papers/1812/1812.02825.pdf)
- [self-attention with relative position representation](https://arxiv.org/pdf/1803.02155.pdf)
- [Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures](http://aclweb.org/anthology/D18-1458)
- [tensor2tensor for neural machine translation](https://arxiv.org/pdf/1803.07416.pdf)


------------------------------------------

### Speech materials
- [linguistic data consortium](https://www.ldc.upenn.edu/)
- [kaldi](https://github.com/kaldi-asr/kaldi)
- [phd thesis: Exploring Deep Learning Methods for discovering features in speech signals](https://pdfs.semanticscholar.org/b041/75bb99d6beff0f201ed82971aeb91d2c081d.pdf?_ga=2.23777402.1357008885.1546424577-1806537053.1546424577)
- [eesen: end-to-end speech recognition using deep rnn models and wfst-based decoding](https://arxiv.org/pdf/1507.08240.pdf)
- [tacotron](https://google.github.io/tacotron/)
- [the ustc and iflytek speech synthesis systems for blizzard challenge 2007](http://www.festvox.org/blizzard/bc2007/blizzard_2007/full_papers/blz3_017.pdf)
- [fast, compact, and high quality lstm-rnn based statistical parametric speech synthesizers for mobile devices](https://arxiv.org/pdf/1606.06061.pdf)
- [local minimum generation error criterion for hybrid hmm speech synthesis](https://pdfs.semanticscholar.org/49ff/fcbd1de67c6aec0d87950f0b9a6dca06c890.pdf)
- [recent advances in google real-time hmm-driven unit selection synthesizer](https://ai.google/research/pubs/pub45564.pdf)
- [simultaneous modeling of spectrum, pitch and duration in hmm-based speech synthesis](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.28.2007&rep=rep1&type=pdf)
- [hidden markov models based on multi-space probability distribution for pitch pattern modeling](https://pdfs.semanticscholar.org/60e0/8c785d9266c0de8f07c453d67e6b8c7c9b94.pdf)
- [char2wav: end-to-end speech synthesis](https://mila.quebec/wp-content/uploads/2017/02/end-end-speech.pdf)
- [sampleRNN: an unconditional end-to-end neural audio generation model](https://arxiv.org/pdf/1612.07837.pdf)
- [exploring deep learning methods for discovering features in speech signals](https://pdfs.semanticscholar.org/b041/75bb99d6beff0f201ed82971aeb91d2c081d.pdf?_ga=2.23777402.1357008885.1546424577-1806537053.1546424577)
- [sample efficient adaptive text-to-speech](https://arxiv.org/pdf/1809.10460v1.pdf)










------------------------------------

### speech tools
- [htk](http://htk.eng.cam.ac.uk/)

### emotional speech
- [zenodo.org](https://zenodo.org/record/1188976)



