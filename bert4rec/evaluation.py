import torch
import numpy as np
import random


def evaluate(model, user_test, max_len, bert4rec_dataset, num_item, sample=None):
    """
    모델을 평가하는 함수
    모델 학습시에는 sample 파라미터의 갯수만큼 만 test 데이터를 랜덤 샘플링하여 평가

    Args:
        model : 평가할 모델
        user_test : 평가에 사용할 데이터 셋
        max_len : 사용할 sequence의 길이
        bert4rec_dataset :random_neg_sampling 사용을 위해 필요한 객체
        num_item : 전체 아이템의 갯수
        sample : 샘플링할 갯수
    Returns:
        NDCG_10, HIT_10, HIT_1: 모델 평가 점수
    """
    model.eval()

    NDCG_10 = 0.0  # NDCG@10
    HIT_10 = 0.0  # HIT@10
    HIT_1 = 0.0  # HIT@1

    num_item_sample = 100

    # 모델 학습시 random smaple을 통해 학습 시간 단축
    if sample:
        users = random.sample(range(len(user_test)),  sample)
    else:
        users = list(user_test.keys())

    for user in users:
        seq = (user_test[user][:-1] + [num_item + 1])[-max_len:]
        rated = user_test[user]
        items = [user_test[user][-1]] + bert4rec_dataset.random_neg_sampling(rated_item=rated, num_item_sample=num_item_sample)

        with torch.no_grad():
            predictions = -model(np.array([seq]))
            predictions = predictions[0][-1][items] # sampling
            rank = predictions.argsort().argsort()[0].item()

        if rank < 10:  # Top10
            NDCG_10 += 1 / np.log2(rank + 2)
            HIT_10 += 1
        elif rank == 1:
            HIT_1 += 1

    NDCG_10 /= len(users)
    HIT_10 /= len(users)
    HIT_1 /= len(users)

    return NDCG_10, HIT_10, HIT_1
