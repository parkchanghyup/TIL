# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

## Abstract

Transformer는 longer-term dependency를 학습 할 수 있는 잠재력을 가지고 있지만,   
언어 모델링 설정에서 고정된 길이의 문맥에 의해 제한된다.  
우리는 시간적 결합을 방해하지 않고 고정된 길이를 넘어 학습 의존성을 가능하게 하는새로운 신경망 구조인  `Transforemr-XL`을 제안 한다.  `Transforemr-XL`은 segment-level 의 반복 메커니즘과 새로운 positional encoding 체계로 구성 된다.  우리의 방법은 장기적인 의존성을 포착할 수 있을 뿐만 아니라 문맥을 무시하는 문제를 해결한다. 그 결과, `TransformerXL`은 RNN보다 80%, vanilla Transformers보다 450% 긴 의존성을 학습하고 짧은 시퀀스 및 긴 시퀀스 모두에서 더 나은 성능을 보이며, vanilla Transformers보다 최대 1,800배 이상 빠르다. 특히, 우리는 bpc/perplexity의 `state-of-the-art` 결과를 **enwiki8에서 0.99**, **text8에서 1.08**, **WikiText-103에서 18.3**, **One Billion Word에서 21.8** 및 PenTreeBank에서 54.5로 향상 시켰다. WikiText-103으로만 훈련할 때 Transformer-XL은 수천 개의 토큰으로 상당히 일관되고 참신한 텍스트 기사를 생성할 수 있다.

## Instruction