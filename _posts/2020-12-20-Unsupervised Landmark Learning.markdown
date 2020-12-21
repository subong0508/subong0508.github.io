---
layout: post
title:  Unsupervised Landmark Learning
date:   2020-12-20
author: Jung Jaeeun
categories: review
tags: deeplearning unsupervisedlearning 
use_math: true
---

# [1. Unsupervised Learning of Object Landmarks through Conditional Image Generation](https://papers.nips.cc/paper/7657-unsupervised-learning-of-object-landmarks-through-conditional-image-generation.pdf)

## Task: Generate the target image given the source image and the encoded target image. 

## Method
### Heatmaps bottleneck
$\Phi(x)$: learn to extract keypoint-like structures

$S_{u}(x;k)$: K heatmaps
=> $u_{k}^{*}(x) = \frac{\sum ue^{S_{u}(x;k)}}{\sum e^{S_{u}(x;k)}}$ (spatial softmax)

$\Phi_{u}(x;k)$: Gaussian-like function centered at $u_{k}^{*}$

### Generator: Perceptual Loss
$\mathcal{L}(x', \hat{x'}) = \sum_{l} \alpha_{l} \vert\vert\Gamma_{l}(x')-\Gamma_{l}(\hat{x'})\vert\vert^{2}$: perceptual loss

## Overall Architecture
![model architecture](../../../../img/Unsupervised-Landmark/cond.png)

## Summary
**By using K-heatmaps as a bottleneck having keypoints information and exploiting training method of conditional image generation, this paper achieved SOTA results of landmark detection**


# [2. Unsupervised Landmark Learning from unpaired data](https://arxiv.org/pdf/2007.01053.pdf)

## Task: Reconstructing images with the apprearance and pose originated from different images and establish various consistencies among these reconstructed images

## Method
### Cross-Image cycle Consistency Framework
Given $I_{i}, I_{j}$: pair of images 

$\mathbf {a_{i}} = E_{a}(N(I_{i})), \mathbf {a_{j}} = E_{a}(N(I_{j}))$

$\mathbf {p_{i}} = E_{p}(N(I_{i})), \mathbf {p_{j}} = E_{p}(N(I_{j}))$

$I_{i, j} = D(\mathbf {a_{i}}, \mathbf {p_{j}}), I_{j, i} = D(\mathbf {a_{j}}, \mathbf {p_{i}})$

$\mathbf {a_{i}}' = E_{a}(N(I_{i, j})), \mathbf {a_{j}}' = E_{a}(N(I_{j, i}))$

$\mathbf {p_{i}}' = E_{p}(N(I_{i,j})), \mathbf {p_{j}}' = E_{p}(N(I_{j,i}))$

$I_{i, j}' = D(\mathbf {a_{i}}', \mathbf {p_{j}}'), I_{j, i}' = D(\mathbf {a_{j}}', \mathbf {p_{i}}')$

**$\mathcal{L_{cycle}} = \mathcal{P}(I_{i}, I_{i}')+\mathcal{P}(I_{j}, I_{j}')$: P is perceptual loss implemented by VGG network**

**$\mathcal{L_{inv}} = \vert\vert\mathbf {p_{i}}' - \mathbf{p_{i}}\vert\vert ^ {2} + \vert\vert\mathbf {p_{j}}' - \mathbf{p_{j}}\vert\vert ^ {2}$**

### Regularization via Cross-Image Flow Module

$T^{i \rightarrow j}$: the location correspondences

$\mathbf{C}$: 4D tensor containing the element-wise cosine similiarity between two feature maps($\mathbf {f_{i}}', \mathbf {f_{j}}'$) 


$\hat{C} = \mathbf {W_{1}} \bigotimes (\mathbf {W_{2}} \bigotimes \mathbf {C})$: 4D convolution using 2D convolutions consequently

$S^{i \rightarrow j}(x_{j}, y_{j}) = softmax(\hat{\mathbf{C}}(*, *, x_{j}, y_{j}))$

$T^{i \rightarrow j}(x_{j}, y_{j}) = argmax_{(x_{i}, y_{i})}S^{i \rightarrow j}(x_{j}, y_{j})$ (vice versa for j->i)

Thus, transformation maps can reflect the semantic correlations between landmarks of two images.

**$\mathcal{L_{equiv}} = \vert\vert\mathbf {p_{i}} - T^{j \rightarrow i}\circ\mathbf{p_{j}}\vert\vert ^ {2}+\vert\vert\mathbf {p_{j}} - T^{i \rightarrow j}\circ\mathbf{p_{i}}\vert\vert ^ {2}$**

### Final Loss: $\mathcal{L_{total}}=\lambda_{cycle}\mathcal{L_{cycle}}+\lambda_{equiv}\mathcal{L_{equiv}}+\lambda_{inv}\mathcal{L_{inv}}$

## Overall Architecture

![model architecture](../../../../img/Unsupervised-Landmark/unpaired.png)

## Summary
**Through techinique of balancing losses which can be categorized into meaningful embedding/invariance/equivariance, unpaired images can be used to locate landmarks**

# [3. Unsupervised Part-Based Disentangling of Object Shape and Appearance](https://arxiv.org/pdf/1903.06946.pdf)

## Method

### Part-based Representation

- part based factorization of representation: $\phi(x) := (\phi_{1}(x), \phi_{2}(x), ...)^{\top}$ where $\phi_{i}(x)$ can be decomposed as $[\alpha_{i}(x), \sigma_{i}(x)]$

### Invariance and Equivariance

- invariance: $i)\alpha_{i}(x \circ s)=\alpha_{i}(x)$, $ii)\sigma_{i}(a(x))=\sigma_{i}(x)$ => **$\mathcal {L_{rec}} = \vert\vert x - D([\alpha_{i=1,...}(x), \sigma_{i=1,...}(x)]) \vert\vert_{1}$**
- equivariance: $\sigma_{i}(x \circ s) = \sigma_{i}(x) \circ s$ => **$\mathcal {L_{equiv}} = \sum_{i} \lambda_{\mu} \vert\vert \mu[\sigma_{i}(x \circ s)] - \mu[\sigma_{i}(a(x))\circ s]\vert\vert_{2} + \lambda_{\sum} \vert\vert \sum[\sigma_{i}(x \circ s)] - \sum[\sigma_{i}(a(x))\circ s]\vert\vert_{1}$**
- total loss: $\mathcal {L} = \mathcal {L_{rec}} + \mathcal {L_{equiv}}$  


## Overall Architecture

![model architecture](../../../../img/Unsupervised-Landmark/shape-appear.png)

where $f$ denotes localized image encoding

## Summary
**To sum up, shape stream extracts part shapes which are independent from appreances and appreance stream does same thing as well except it re-encodes part appearances using local features. In decoder, reconstruction is done by using approximate part shapes(normalized) and part appreances weighted on part shapes**


# [4. Self-supervised Learning of Interpretable Keypoints from Unlabelled Videos](https://www.robots.ox.ac.uk/~vgg/publications/2020/Jakab20/jakab20.pdf)

## Task: Recognizing the pose of objects from a single image that for learning uses only unlabelled videos and a weak empirical prior on the objects poses

## Method

- ${y} = \Phi({x})$: pose extracted from image
- $\Psi(\Phi(x), x')$: conditional decoder network

### Dual representation of pose & bottleneck

- $\mathbf{p} = (p_{1}, ..., p_{K})$: a vector of K 2D keypoint coordinates trained by $\eta(\mathbf {y})$
- $y* = \beta(\mathbf{p})_{u}$: a distance field from line segments that forms the skeleton image
- $x=\Psi(\beta \circ \eta \circ \Phi(x), x')$: so as to prevent cheating by exploting dual representation 

### Loss
- $\mathcal{L_{perc}}=\frac{1}{N}\sum_{i=1}^{N}{\vert\vert \Gamma(\hat{x_{i}}) - \Gamma(x_{i}) \vert\vert ^ {2}}$: **Auto-encoding** loss implemented by perceptual loss
- $\mathcal{L_{disc}}(D) = \frac{1}{M}\sum_{j=1}^{M} D(\bar{y_{j}})^{2} + \frac{1}{N}\sum_{i=1}^{N}{(1-D(y_{i}))^{2}}$: **Difference adversarial loss** to match $p(y)\approx q(y)$, encourages the images $y$ ro be 'skeleton-like'
- $\mathcal{L}(\Phi, \Psi, D) = \lambda_{disc}\mathcal{L_{disc}}(D)+\mathcal{L_{perc}}(\Psi, \Phi)$: **Total Loss**, minimized w.r.t $\Phi, \Psi$ and maximised w.r.t $D$

## Overall Architecture

![model architecture](../../../../img/Unsupervised-Landmark/pose.png)

## Summary
**While using conditional image generator as a decoder, the method utilized in this paper forces encoder to grab meaningful pose information by exploiting dual representation and empirical prior**

# [5. Unsupervised Learning of Landmarks by Descriptor Vector Exchange](https://arxiv.org/pdf/1908.06427.pdf)