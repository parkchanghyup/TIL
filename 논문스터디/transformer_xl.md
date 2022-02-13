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

 Transformer 또는 self-attention 을 언어 모델링에 적용하기 위해 중점은 임의로 긴 context를 고정 크기 표현으로 효과적으로 변환하도록 학습시키는 것이다. 무한한 메모리와 계산이 가능핟면, 간단한 해결책은 feed-forward 신경망과 유사한  무조건적인 transforemr decoder를 사용하여 전체 context 를 처리하는 것이다. 그러나 이것은 일발적으로 실현 불가능하다.   
 실현 가능한 대안책으로는 전체 말뭉치를 관리 가능한 크기의 짧은 segment로 나누고 이전 segment의 모든 상황별 정보를 무시하고 각 segment만 활용하여 모델을 훈련하는 것이다.  
이러한 학습 패러다임에서 정보는 segment간에 절대로 공유 되지 않습니다.  고정된 길이의 context를 사용할 경우 두 가지 중요한 한계가 있습니다. 
첫번쨰는 가능한 가장 큰 dependency length는 문자 수준 언어 모델링에서 수백인 세그먼트 길이에 의해 제한 된다. 따라서 self-attention 메커니즘은 RNN에 비해 기울기 소실 문제의 영향을 덜 받지만, vanilla model은 이러한 최적화 이점을 충분히 활용할 수 없다. 
둘째, 문장이나 다른 의미 경계를 존중하기 위해 패딩을 사용할 수 있지만, 실제로는 효율성이 향상되어 단순히 긴 텍스트를 고정 길이의 세그먼트로 chunk하는 것이 표준 관행이었다.
그러나 단순히 시퀀스를 고정 길이 segment로 chunk 하는 것은 **introduction**에서 논의한 대로 context fragmentation 문제를 초래할 것이다.   

evaluation 중에 각 단계에서 vanilla  model은 훈련과 동일한 길이의 세그먼트도 소비하지만 마지막 위치에서 하나의 예측만 한다. 그러면 다음 segment가 한 위치만 오른쪽으로 이동하며 새 segment는 처음 부터 모두  처리해야한다. 

그림 1b에서 표시된 바와 같이, 이 절차는 각 예측이 훈련 중에 노출된 가장 긴 context를 활용하도록 보장하고, 또한 훈련에서 직면하는 context fragmentation문제를 완ghk한다.  
이 절차는 각 예측이 훈련 중에 노출된 가장 긴 context를 활용하도록 보장하고, 또한 훈련에서 직면하는 컨텍스트 단편화 문제를 완화한다. 그러나 이과정은 매우 많은 리소스를 필요로 한다.   
우리는 우리가 제안한 아키텍처가 평가 속도를 크게 향상시킬 수 있다는 것을 보여줄 것이다.

## Segment-Level Recurrence with State Reuse

고정 길이 context를 사용할 때의 한계를 해결하기 위해 Transformer 아키텍처에 recurrence 메커니즘을 도입할 것을 제안한다. 학습 중에 이전 세그먼트에 대해 계산된 hidden state 시퀀스는 고정되고 모델이 다음 새 세그먼트를 처리할 때 확장 context로 재사용되도록 캐시된다.(2a)  
그래디언트는 여전히 세그먼트 내에 남아 있지만, 이 추가 입력은 네트워크가 기록의 정보를 이용할 수 있게 해주므로 장기적인 의존성을 모델링하고 컨텍스트 단편화를 방지할 수 있다. 형식적으로, 길이 L의 연속된 두 세그먼트를 각각 $s_t = [x_{\tau+1,1},...,,x_{\tau+1,L}], s{\tau+1} = [x_{\tau+1,1},...,,x_{\tau+1,L}]$이 되게 한다.   

$\tau$-th segment $s_\tau$에 대해 생성된 n 번째 레이어 은닉 상태 시퀀스를 $h_n^t$ ∈ $\mathbb{R}^{L * D}$로 나타냅니다. 여기서 $d$는 은닉 차원 입니다.   그런 다음 세그먼트 $s_{\tau+1}$에 대한 n번째 레이어 hidden state는 다음과 같이
 ...
 여기서 함수 SG(·)는 stop-gradient를 나타내며, 표기법 $[h_u \circ h_v]$는 길이 치수를 따라 숨겨진 두 시퀀스의 결합을 나타내며, $W$는 모델 파라미터를 나타낸다. 
 표준 트랜스포머와 비교하여, 중요한 차이점은 키 $k_{\tau+1}^n$와 value v_{\tau+1}^n가 확장된 컨텍스트 $\tilde{h}_{\tau+1}^{n-1}$에서 조건화되어 이전 세그먼트에서 캐시된 $h_{\tau}^{n-1}$라는 것이다. 그림 2a에서 녹색으로 강조된 부분이다. 

$\mathbb(R)$

이 실패 모드를 피하기 위해, 기본 아이디어는 hidden state의 상대적 위치 정보만 인코딩하는 것이다. 개념적으로, 위치 인코딩은 모델에 정보가 어떻게 수집되어야 하는지에 대한 시간적 단서 또는 "bais"를 제공한다. 
동일한 목적을 위해, 초기 임베딩에 bais를 정적으로 통합하는 대신, 각 레이어의 attnetion score에 동일한 정보를 주입할 수 있다. 더 중요한 것은 상대적으로 시간적 bias을 정의하는 것이 더 직관적이고 일반화 가능하다는 것이다. 
예를 들어, 쿼리 벡터 $q_{\tau,i}$가 키 벡터 $k_{\tau<=i}$에 attnetion할 때, 세그먼트의 시간 순서를 식별하기 위해 각 키 벡터의 절대 위치를 알 필요가 없다. 대신에, 각각의 핵심 벡터 $k_{\tau,i}$와 그 자체  $q_{\tau,i}$즉 $i-j$ 사이의 상대적인 거리를 아는 것으로 충분하다.  
실제로, R od R Lmax×d 의 상대 위치 인코딩 집합을 만들 수 있는데, 여기서 i번째 행 Ri는 두 위치 사이의 상대적인 거리를 나타낸다.