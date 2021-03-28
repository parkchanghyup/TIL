[→ Open in Slid](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473)


---


본 논문에서는 \`깊은 네트워크\`를 학습시키기 위한 방법으로 \`residual learning(잔여 학습)\`을 제안 한다.


이 논문이 주목받는 이유 두가지는 성능이 상당히좋고, 아이디어가 이해하기 쉽다.

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/14cb51c7-d7cc-4c0e-b059-0c707ce091ed.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=112.16594883787536)


일반적인 Layer에서는 단순히 깊게 쌓으면 어느 시점부터는 정확도가 떠어지지만,


\`잔여학습\`을 적용한 Layer 는 깊게 쌓을수록 정확도는 전반적으로 상승한다.





\## CNN 모델의 특징(Feature Map)

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/dd894015-ce30-4002-8b8e-ede1d3f009bb.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=229.42457103814698)


 - 일반적으로 CNN에서 레이어가 깊어질수록 채널의 수가 많아지고 너비와 높이는 줄어든다.
 - convolution layer의 \*\*서로 다른 필터들은 각각 적절한 특징(feature) 값을 추출\*\*하도록 학습 된다.





\## VGG Net


VGG net은 작은 크기의 \`3x3 convolution filter\`를 이용해 레이어의 깊이를 늘려 우수한 성능을 보인다.

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/150303cc-b733-48d2-ae74-779acd0d8220.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=380.95429699046326)





\## 본 논문의 핵심 아이디어 : 잔여 블록 (Residual Block)


 - 잔여 블록을 이용해 네트워크의 최적화(optimization) 난이도를 낮춘다.
 - 실제로 내재한 mapping인 H(x)를 곧바로 학습하는 것은 어려우므로 대신 $F(x) = H(x) - x $를 학습한다.

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/74f56b1c-7095-4c76-82f6-97190d3a197e.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=560.4773157448922)





 - \`residual block\`를 이용해 네트워크의 최적화 난이도를 낮춘다.

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/3732b3bf-ba2d-47ef-8126-90053df08501.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=750.9021130071526)


\## ImageNet에서의 테스트 결과 분석


이전까지의 아키텍처와 다르게 \*\*레이어가 깊어질수록 성능이 향상\*\* 된다.


물론 레이어가 과도하게 깊으면 오히려 감소 할 수 있으니, 적당히.. 깊게 쌓아야 한다.

[![ResNet image](https://slid-capture.s3.ap-northeast-2.amazonaws.com/public/capture_images/63704d3bcdaa45a2826af1fbd2b81473/d51f310a-7aeb-472f-b6c1-d6793dc273c6.png)](https://slid.cc/vdocs/63704d3bcdaa45a2826af1fbd2b81473?v=cdefa431f9264b1e8028e55b921f97fa&start=840.1418962551079)



