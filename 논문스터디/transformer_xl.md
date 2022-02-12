# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

## Abstract

Transformer는 longer-term dependency를 학습 할 수 있는 잠재력을 가지고 있지만,   
언어 모델링 설정에서 고정된 길이의 문맥에 의해 제한된다.  
우리는 시간적 결합을 방해하지 않고 고정된 길이를 넘어 학습 의존성을 가능하게 하는새로운 신경망 구조인  `Transforemr-XL`을 제안 한다.  `Transforemr-XL`은 segment-level 의 반복 메커니즘과 새로운 positional encoding 체계로 구성 된다.  우리의 방법은 장기적인 의존성을 포착할 수 있을 뿐만 아니라 문맥을 무시하는 문제를 해결한다. 그 결과, `TransformerXL`은 RNN보다 80%, vanilla Transformers보다 450% 긴 의존성을 학습하고 짧은 시퀀스 및 긴 시퀀스 모두에서 더 나은 성능을 보이며, vanilla Transformers보다 최대 1,800배 이상 빠르다. 특히, 우리는 bpc/perplexity의 `state-of-the-art` 결과를 **enwiki8에서 0.99**, **text8에서 1.08**, **WikiText-103에서 18.3**, **One Billion Word에서 21.8** 및 PenTreeBank에서 54.5로 향상 시켰다. WikiText-103으로만 훈련할 때 Transformer-XL은 수천 개의 토큰으로 상당히 일관되고 참신한 텍스트 기사를 생성할 수 있다.

## Instruction

언어 모델링은 비지도 사전 학습과 같은 성공적인 응용프로그램과 함께 long-term dependency modeling을 필요로 하는 중요한 문제 중 하나다. 하지만 신경망을 sequence data의 long-term dependency을 모델링하는 기능을 갖추는 것은 어려웠다.  RNN, 특히 LSTM은 언어 모델링에서 표준 solution 이였으며, 여러 벤치마크에서 높은 성능을 발휘하였다. 그러나 RNN은 기울기 소실 및 폭발로 인해 최적화하기 어려웠으며 LSTM또한 gating과 gradient clipping 기법의 도입 으로도 이 문제를 완전히 해결하기에 충분하지 않을 수 있다. 경험적으로, 이전 연구에서는 LSTM언어 모델이 평균적으로 200개의 문맥 단어를 사용하는 것으로 밝혀져(Khandelwal et al., 2018) 추가적인 개선의 여지가 있음을 시사했다. 반면에 
attention mechanisms으로 변환된 장거리-단어 쌍 사이의 직접적인 연결은 optimization을 용이하게 하고 long-term dependency의 학습을 가능하게 할 수 있다.  
최근 설계된 깊은 transformer 는 네트워크를 학습하기 위해 보조손실을 설계했으며 이는 LSTM을 압도적으로 능가하는 퍼포먼스를 보인다. 이러한 성공에도 불구하고 언어 모델링 학습은 segment간 정보 흐름 없이 수백개의 문자로 구성된 분리된 고정 기이 세그먼트에 대해 수행된다.   
고정된 context 길이의 결과로, 모델은 미리 정의된 context 길이를 초과하는 장기 의존성을 식별 할 수 없다. 또한, 고정 길이 세그먼트는 문장이나 다른 semantic boundary를 고려하지 않고 연속적인 chunk of symbol을 선택하여 생성 된다. 따라서 이 모델은 처음 몇 개의 기호를 잘 예측하는 데 필요한 상황별 정보가 부족하여 비효율적인 최적화와 성능 저하로 이어진다. 우리는 이 문제를 `context fragmentation`이라 부른다.  

앞에서 언급한 고정된 길이의 context의 한계를 해결하기 위해 Transformer-XL이라는 새로운 아키텍처를 제안한다. 특히 새로운 각 세그먼트에 대해 hidden states를 처음부터 계산하는 대신 이전 세그먼테어서 얻은 hidden states를 재사용 한다. 재사용 되는 hidden state는 현재 세그먼트에 대한 메모리 역할을 하며, 세그먼트 간에 반복적인 연결을 구축한다. 그 결과, 정보가 반복 연결을 통해 전파될 수 있기 때문에 매우 long-trem dependecy 모델링이 가능해진다. 한편, 이전 세그먼트에서 정보를 전달하면 `context fragmentation` 문제도 해결할 수 있다. 더 중요한 것은, 우리는 시간적 혼란을 야기하지 않고  state를 재사용 가능하게 하기 위해 **상대적 인코딩을 사용할 필요성을 보여준다.** 따라서 추가적인 기술적 기여로, 우리는 학습중에 관찰된 것보다 더 긴 observation 길이로 일반화하는 단순하지만 더 효과적인 상대적 positional encoding 공식을 도입한다. Transformer-XL은 단어 수준에서 문자 수준 언어 모델링까지 다양한 5개의 datasets에서 강력한 결과를 얻었다. 또한 100M 토큰에서만 훈련된 수천 개의 토큰으로 비교적 일관성 있는 긴 텍스트 기사를 생성할 수 있다. 우리의 주요 기술적 기여는 순전히 self-attentive model에 순환 개념을 도입하고 새로운 positional eocidng 체계를 도출 하는 것을 포함한다. 둘중 어느 하나만으로는 고정된 길이의 context 문제를 다루지 않기 때문에, 이 두 기술을 완전한 해결책 세트를 형성한다.  
Transformer-XL은 문자 수준 및 단어 수준 언어 모델링 모두에서 RNN보다 훨씬 더 나은 결과르 달성하는 최초의 self-attention model 이다. 

## model 
x토큰의 말뭉치 $x = (x_1,...,x_T)$ 가 주어지면 언어 모델링의 task는  joint probability P(x), which is often auto-regressively factorized as $P(x) = \sqcap_t P(x_t| x_<t)$를 추정 하는 것이다.  
 factorization에서는 문제가 각 조건부 요인을 추정하는 것으로 줄어 든다. 이 연구에서, 우리는 조건부 확률을 모델링하기 위한 standard neural 접근법을 고수한다.   
 특히, trainable neural network은 context $x_<t$를 고정된 크기의 hidden state로 인코딩 하는데 사용되며, logit을 얻기 위해 embbding과 곱한다. 그런 다음 logits은 소프트맥스 함수에 공급되어 다음 토큰에 대한 범주형 확률 분포를 산출한다. 

 ## Vanila Transformer Language Models