---
layout: post
title:  from Variational Inference to VAE
date:   2020-12-22
author: Jung Jaeeun
categories: Scribbles
tags: bayesian deep-learning variational-inference
use_math: true
---

이번 포스팅에서는 Bayesian의 중요한 토픽인 Variational Inference부터 그와 연관된 Variational Auto-encoder까지 알아보려고 한다. 

# Bayesian Framework

먼저, 베이지안의 기본적인 사고방식부터 알고 가자. 빈도론자와 베이지안의 가장 큰 차이점은 우리가 추정하고자하는 parameter를 확률변수로 보냐/아니냐이다. 빈도론자는 고정된 상수라고 보고 베이지안은 어떤 확률분포를 따르는 확률변수라고 생각한다.

예를 들어, 우리나라 사람들의 키를 수집한 데이터가 있다고 가정하자. 아무래도 우리가 관심있어 하는 parameter는 우리나라 사람들의 평균 키일 것이다. 빈도론자들은 이 평균 키($\mu$라고 하자.)가 고정된 상수(ex: 168cm)라고 가정하고 ML 방식으로 모수를 추정한다. 그에 비해, 베이지안은 $\mu$에 대한 사전 분포를 먼저 정의한 후(이를 prior belief라고 한다.) 주어진 데이터로 부터 사후분포를 추정한다. 

우리나라 사람들의 평균 키가 매우 작다고 믿는 베이지안은 평균이 160cm인 정규분포를 사전분포로 가정할 것이다. 그런데 데이터에 180cm 이상인 사람들이 많다면 데이터를 본 이후 사후분포는 평균이 175cm 정도인 정규분포가 된다. 한편, 빈도론자는 평균 키는 185cm구나!라고 결론을 지을 것이다.

글이 길어졌는데, 여튼 베이지안의 핵심은 **데이터에 사전믿음을 결합한다는 것**에 있다.

우리가 추정하고자 하는 모수를 $\theta$, 데이터를 $x$라고 할 때 결국 **베이지안의 목표는 사전분포 + 데이터로부터 사후분포를 추론하는 것이다.** 즉, 다음과 같다.

$p(\theta\vert X) = \frac{\prod_{i=1}^{n}{p(x_{i}\vert\theta)p(\theta)}}{\int {\prod_{i=1}^{n}{p(x_{i}\vert\theta)p(\theta)d\theta}}} \text{ where } x_{i}'s \text{ are i.i.d samples}$

그럼 이제 본격적으로 베이지안 입장에서 본 머신러닝 모델에 대해서 이야기해보도록 하자. $x$를 features, $y$를 class label/latent vector, $\theta$를 추정할 parameter로 정의하겠다. 그렇다면 우리가 관심있는 분포는 $x$가 given일 때 $y, \theta$의 결합 분포에 해당한다.

- $p(y, \theta \vert x) = p(y \vert \theta, x)p(\theta) \text{ } \because x \perp\theta$ 
- $p(\theta \vert X, Y) = \frac{p(Y \vert X, \theta)p(\theta)}{\int p(Y \vert X, \theta)p(\theta)}\text{ where X, Y denote whole training set}$
- test: $p(y \vert x, X, Y) = \int{ p(y \vert x, \theta)p(\theta \vert X, Y)d\theta}$

그러나 바로 여기에서 문제가 생긴다.  $p(\theta \vert X, Y)$를 구하기 위해서는 분모에 있는 적분이 가능해야 하는데, 
$p(y \vert x, \theta)$와 $p(\theta)$가 conjugate하지 않으면 대부분의 경우에서 적분이 어렵다는 것. test시에도 마찬가지.

(**[conjugate prior](https://en.wikipedia.org/wiki/Conjugate_prior)**: conjugacy에 대해서는 자세히 언급하지 않겠지만, 궁금하신 분들은 이 링크를 참조하길 바란다. 대표적인 conjugate distributions은 beta-binom, poission-gamma 등이 있다.)

여튼, conjugacy가 없다면 posterior distribution(사후분포)을 구하기가 매우 힘들고 빈도론자들 처럼 $\theta$에 대한 point estimation을 할 수 밖에 없다. 이 경우를 Poor Bayes라고도 한다고... test시에도 이러한 point estimation을 통해 얻어진 $\theta_{MP}$를 가지고 $y$에 대한 추론을 하게 된다.

- $\theta_{MP} = argmax_{\theta}p(\theta \vert X, Y) = argmax_{\theta}P(Y \vert X, \theta)p(\theta)$
- $p(y \vert x, X, Y) \approx p(y \vert x, \theta_{MP})$

덧붙여서 말하자면, 빈도론자들이 overfitting을 막기 위해 쓰는 regularization 기법(ex: L2-loss)가 사실 이 Poor Bayes와 본질적으로 동등하다.

# Variational Inference
## Main Goal: to estimate $p(\theta \vert x)$

그러면 conjugacy가 없고, 다시 말해 analytical하게 푸는 것이 불가능한 상황에서 우리는 어떻게 해야할까? 방법은 크게 두 가지로 나뉜다.

1. **variational inference**: $q(\theta) \approx p(\theta \vert x)$
2. **sampling based method**: $p(x \vert \theta)p(\theta)$로 부터 샘플링하는 방법. MCMC 등이 있으나 시간이 오래 걸린다.

우리는 여기서 첫 번째 방법인 variational inference에 대해 알아보려고 한다. approximate posterior를 가정하고, true posterior과 최대한 가깝게 approximate posterior를 추정하는 방법이다. 분포의 거리를 측정하기 위해 우리는 KL-divergence를 사용한다. KL-divergence는 워낙 유명한 토픽이고 서치하기도 쉬우니까 생략..

$\hat{q}(\theta) = argmin_{q}D_{KL}(q(\theta) \vert\vert p(\theta \vert x)) = argmin_{q} \int q(\theta)log\frac{q(\theta)}{p(\theta \vert x)}d\theta$

- 문제1: $p(\theta \vert x)$를 모른다.
- 문제2: 분포에 대한 optimization은 어떻게 할 수 있나?

**Sol)**

$logp(x) = E_{q(\theta)}[logp(x)] = \int q(\theta)logp(x)d\theta = \int q(\theta)log\frac{p(x, \theta)}{p(\theta \vert x)}d\theta= \int q(\theta)log\frac{p(x, \theta)}{p(\theta \vert x)}\frac{q(\theta)}{q(\theta)}d\theta$

 $= \int q(\theta) log\frac{p(x, \theta)}{q(\theta)}d\theta + \int q(\theta) log\frac{q(\theta)}{p(\theta \vert x)}d\theta = \mathcal{L}(q(\theta)) + D_{KL}(q(\theta) \vert\vert p(\theta \vert x))$

 따라서, $D_{KL}(q(\theta) \vert\vert p(\theta \vert x))$를 maximize하는 문제는 $\mathcal{L}(q(\theta))$를 minimize하는 문제와 동등해진다.

 $\mathcal{L}(q(\theta)) = \int q(\theta) log\frac{p(x, \theta)}{q(\theta)}d\theta = \int q(\theta) log\frac{p(x \vert \theta)p(\theta)}{q(\theta)}d\theta$

 <b><font color='red'>$= E_{q(\theta)}[logp(x \vert \theta)] - D_{KL}(q(\theta) \vert\vert p(\theta)) = \text{data likelihood + KL-regularizer term}$</font></b>

 이제 남은 부분은 $q(\theta)$를 어떻게 최적화하는지인데, 크게 두 가지 방법이 있다.

 1. **[mean field approximation](https://en.wikipedia.org/wiki/Variational_Bayesian_methods)**: $\theta$끼리 독립일 때 사용하는 방법.
 2. **parametric approximation**: 대부분의 neural network에서 사용하는 방법. $q(\theta)=q(\theta \vert \lambda)$라고 정의한 후 $\lambda$에 대해서 최적화.

지금까지 배운 것들을 요약해보자면 다음과 같다.

- Full Bayesian inference: $p(\theta \vert x)$
- MP inference: $\theta_{MP} = argmax_{\theta}p(\theta \vert X, Y)$
- Mean field variational inference:  $p(\theta \vert x) \approx q(\theta) = \prod_{j=1}^{m}q_{j}(\theta_{j})$
- Parametric variational inference: $p(\theta \vert x) \approx q(\theta) = q(\theta \vert \lambda)$

# Latent Variable Models

# Stochastic Variational Inference and VAE
