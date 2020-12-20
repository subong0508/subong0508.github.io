---
layout: post
title:  Unsupervised Landmark Learning
date:   2020-12-20
author: Jung Jaeeun
categories: review
tags: deeplearning unsupervisedlearning 
use_math: true
---

# [Unsupervised Learning of Object Landmarks through Conditional Image Generation](https://papers.nips.cc/paper/7657-unsupervised-learning-of-object-landmarks-through-conditional-image-generation.pdf)

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


# [Unsupervised Landmark Learning from unpaired data](https://arxiv.org/pdf/2007.01053.pdf)

## Task: Reconstructing images with the apprearance and pose originated from different images and establish various consistencies among these reconstructed images

## Method
### Cross-Image cycle Consistency Framework
Given $I_{i}, I_{j}$: pair of images 

$\mathbf {a_{i}} = E_{a}(N(I_{i})), \mathbf {a_{j}} = E_{a}(N(I_{j}))$

$\mathbf {p_{i}} = E_{p}(N(I_{i})), \mathbf {p_{j}} = E_{p}(N(I_{j}))$

$I_{i, j} = D(\mathbf {a_{i}}, \mathbf {p_{j}}), I_{j, i} = D(\mathbf {a_{j}}, \mathbf {p_{i}})$

$\mathbf {a_{i}}' = E_{a}(N(I_{i, j})), \mathbf {a_{j}}' = E_{a}(N(I_{j, i}))$

$\mathbf {p_{i}}' = E_{p}(N(I_{i,j})), \mathbf {p_{j}}' = E_{p}(N(I_{i,j}))$

$I_{i, j}' = D(\mathbf {a_{i}}', \mathbf {p_{j}}'), I_{j, i}' = D(\mathbf {a_{j}}', \mathbf {p_{i}}')$

**$\mathcal{L_{cycle}} = \mathcal{P}(I_{i}, I_{i}')+\mathcal{P}(I_{j}, I_{j}')$: P is perceptual loss implemented by VGG network**

**$\mathcal{L_{inv}} = \vert\vert\mathbf {p_{i}}' - \mathbf{p_{i}}\vert\vert ^ {2} + \vert\vert\mathbf {p_{j}}' - \mathbf{p_{j}}\vert\vert ^ {2}$**

### Cross-Image Flow Module

$T^{i \rightarrow j}$: the location correspondences

$\mathbf{C}$: 4D tensor containing the element-wise cosine similiarity between two feature maps($\mathbf {f_{i}}', \mathbf {f_{j}}'$) 


$\hat{C} = \mathbf {W_{1}} \bigotimes (\mathbf {W_{2}} \bigotimes \mathbf {C})$: 4D convolution using 2D convolutions consequently

$S^{i \rightarrow j}(x_{j}, y_{j}) = softmax(\hat{\mathbf{C}}(*, *, x_{j}, y_{j}))$

$T^{i \rightarrow j}(x_{j}, y_{j}) = argmax_{(x_{i}, y_{i})}S^{i \rightarrow j}(x_{j}, y_{j})$ (vice versa for j->i)

Thus, transformation maps can reflect the semantic correlations between landmarks of two images.

**$\mathcal{L_{equiv}} = \vert\vert\mathbf {p_{i}} - T^{i \rightarrow j}\circ\mathbf{p_{j}}\vert\vert ^ {2}+\vert\vert\mathbf {p_{j}} - T^{j \rightarrow i}\circ\mathbf{p_{i}}\vert\vert ^ {2}$**

### Final Loss: $\mathcal{L_{total}}=\lambda_{cycle}\mathcal{L_{cycle}}+\lambda_{equiv}\mathcal{L_{equiv}}+\lambda_{inv}\mathcal{L_{inv}}$

## Overall Architecture

![model architecture](../../../../img/Unsupervised-Landmark/unpaired.png)

# [Unsupervised Part-Based Disentangling of Object Shape and Appearance](https://arxiv.org/pdf/1903.06946.pdf)