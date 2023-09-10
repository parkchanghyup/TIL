from tqdm import tqdm
from train import train
from evaluation import evaluate


def trainer(model, device, config, criterion, optimizer, data_loader, user_test, bert4rec_dataset, num_item):
    """
    모델을 학습해 ndch@10기준으로 가장 성능이 좋은 모델을 반환하는 함수

    Args:
        model
        device
        config
        criterion
        optimizer
        data_loader
        user_test : 모델 test에 사용할 데이터
        bert4rec_dataset
        num_item

    Returns:
        best_model : ndcg@10 기준 가장 점수가 높은 모델
    """

    best_model = model
    best_ndcg = 0
    for epoch in range(1, config.num_epochs + 1):
        tbar = tqdm(range(1))
        for _ in tbar:
            train_loss, model = train(
                model = model,
                criterion = criterion,
                optimizer = optimizer,
                data_loader = data_loader,
            device = device)

            NDCG_10, HIT_10, HIT_1 = evaluate(
                model = model,
                user_test = user_test,
                max_len = config.max_len,
                bert4rec_dataset = bert4rec_dataset,
                num_item = num_item,
                sample = 5000
                )

            if NDCG_10 > best_ndcg:
                best_model = model
                best_ndcg = NDCG_10


            tbar.set_description(f'Epoch: {epoch:3d}| Train loss: {train_loss:.5f}| NDCG@10: {NDCG_10:.5f}| HIT@10: {HIT_10:.5f}')

    return best_model