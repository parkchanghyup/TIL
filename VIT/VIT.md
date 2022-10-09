# 비전 트랜스포머(VIT)
- 이미지 분야에서 ateetntion 기법을  사용할 경우 대부분 CNN과 함께 사용되거나 전체 CNN 구조를 유지하면서 CNN의 특정 구성 요소를 대체하는데 사용
- CNN에 의존하지 않고 이미지 패치의 시퀀스를 입력값으로 사용하는 transformer를 적용

## VIT의 장점
- transformer 구조를 거의 그대로 사용하기 때문에 확장성이 좋음
- large 스케일 학습에서 매우 우수한 성능을 보임
- transfer learnging 시 CNN보다 훈련에 더 적은 계산 리소스 사용

## VIT 단점
- `inductive bias`의 부족으로 인해 CNN보다 더 많은 데이터 요구
    - inductive bias : 모델이 처음 들어오는 input data에 대한 출력값을 에측하기 위해 사용하는 일련의 `가정`
    - 예를 들어, VIT에 이미지넷을 정규화 없이 학습에 사용할 경우 유사한 크기의 resNet보다 성능이 낮음

## VIT - 구조
![vit](images/img1.png)
![vit](images/img2 .png)


- 입력 Embedding
    - Token embedding을 1D sequence로 입력
        - 2D Image($x_{p}\in\mathbb{R}^{H\times W \times C}$)를 $x_{p}\in\mathbb{R}^{H\times (P^2C)}$로 변환
        - $(P,P)$ : Image Patch 해상도
        - $N$ : Patch의 수 $HW / P^2$
        - $D$: 모든 Layer에서의 동일한 latent Vectore size
            -    Flatten 한 Patch를 학습 가능한 Linear Projection(E)를 사용하여, D차원으로 매핑
    - Patch Embedding이 출력됨
- [CLS] Token
    - Bert의 [class] Token처럼, 학습 가능한 Embedding patch($z_0^0 = x_{class}$ )   를 추가
    - $Z_L^0$: 최종 L 번째 Layer의 0 번째 Token
        - pre-Training과 Fine-Tuning을 수행하는 Classification Head가 부착
- Classification Head
    - Pre-training : 1-hidden Layer인 MLP 

    - Fine-Tuning : 1-linear Layer

- Position embedding
    - Patch Embedding의 Position 정보를 유지하기 위해서, 추가 

    - 2D-Position Embedding을 추가해보았지만 더 좋은 성능 X

        - 이미지이지만, 1D Position Embedding 사용

- Transformer
    - 결과 embedding sequence는 Encoder의 입력으로 들어감 

        - Transformer Encoder

        - Multi-Head로 구성된 self-Attention 메커니즘 적용


        - MLP Block

        - 모든 Block 이전에 LayerNorm(LN) 적용

        - Residual Connection 모든 블록 끝에 적용

 

- Inductive bias
    - CNN(Locality 가정)이나 RNN(Sequentiality 가정) 경우, Global 한 영역의 처리는 어려움

    - ViT는 일반적인 CNN과 다르게 공간에 대한, "Inductive bias"이 없음

    - 그러므로, ViT는 더 많은 데이터를 통해, 원초적인 관계를 Robust 하게 학습시켜야 함

       - ViT는 MLP Layer에서만 Local 및 Translation Equivariance 함

       - Self-Attention 메커니즘은 Global 함

    - 2차원 구조 매우 드물게 사용

       - 이미지 Patch를 잘라서 넣는 Input 부분

       - Fine-tune 시, 다른 해상도(Resolution)의 이미지를 위한 위치 임베딩 조정

   - ▶ 공간(Spatial) 관계를 처음부터 학습해야 함 (∵ Position Embedding 초기화 시 위치정보 전달 X)

 

- Hybrid Architecture
    - Image Patch의 대안으로, CNN의 Feature Map의 Sequence를 사용할 수 있음

       - CNN의 Feature는 Spatial size가 1x1이 될 수 있음

       - CNN으로 Feature추출 → Flatten → Eq.1의 Embedding Projection ($E$) 적용