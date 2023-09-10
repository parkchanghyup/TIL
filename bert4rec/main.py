import torch
import torch.nn as nn
from box import Box
from data_preprocessing import DataPreprocessing
from get_dataframe import get_dataframe
from custom_dataset import BERTRecDataSet

from torch.utils.data import DataLoader
from trainer import trainer
from BERT.bert import BERT4Rec
from evaluation import evaluate

if __name__ == '__main__':
    config = {
        'max_len': 21,
        'hidden_units': 64,  # Embedding size
        'num_heads': 4,  # Multi-head layer 의 수 (병렬 처리)
        'num_layers': 2,  # block의 개수 (encoder layer의 개수)
        'dropout_rate': 0.1,  # dropout 비율
        'lr': 0.001,
        'batch_size': 16,
        'num_epochs': 20,
        'num_workers': 1,
        'mask_prob': 0.15,  # for cloze task
        'session': False,  # log 세션 분리 여부
        'train_sample_length': 50000,  # train시 사용할 sample의 길이
        'only_evaluation': False,  # 모델 평가만 진행
        'save_model_path':  './saved_model/bert4rec_non_session.pth'  # 모델 평가만 진행시 저장된 모델의 경로
    }

    config = Box(config)
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # 모델 학습 및 평가에 사용할 데이터 위치
    data_path = ['./data/train_user_seq_log.json',
                 './data/test_user_seq_log.json',
                 './data/test_user_label.json']

    # json 형태의 데이터를 DataFrame 형태로 변환
    train_df, test_df, item_df = get_dataframe(data_path=data_path, config=config)

    # DataFrame을 학습에 필요한 형태로 변환
    make_sequence_dataset = DataPreprocessing(config, train_df, test_df, item_df)
    user_train, user_test = make_sequence_dataset.get_train_test_data()

    # custom dataset 정의
    bert4rec_dataset = BERTRecDataSet(
        user_train = user_train,
        max_len = config.max_len,
        num_user = make_sequence_dataset.num_user,
        num_item = make_sequence_dataset.num_item,
        mask_prob = config.mask_prob,
        )

    # DataLoader 정의
    data_loader = DataLoader(
        bert4rec_dataset,
        batch_size = config.batch_size,
        shuffle = True,
        pin_memory = True,
        num_workers = config.num_workers,
        )

    # model 정의
    model = BERT4Rec(
        num_user = make_sequence_dataset.num_user,
        num_item = make_sequence_dataset.num_item,
        hidden_units = config.hidden_units,
        num_heads = config.num_heads,
        num_layers = config.num_layers,
        max_len = config.max_len,
        dropout_rate = config.dropout_rate,
        device = device,
        ).to(device)

    criterion = nn.CrossEntropyLoss(ignore_index=0) # label이 0인 경우 무시
    optimizer = torch.optim.Adam(model.parameters(), lr=config.lr)

    # 모델 학습 진행
    if config.only_evaluation is False:
        # 모델 학습 및 NDCG@10기준으로 가장 성능이 좋은 모델을 best model 로 정의
        best_model = trainer(model,
                             device,
                             config,
                             criterion,
                             optimizer,
                             data_loader,
                             user_test,
                             bert4rec_dataset,
                             make_sequence_dataset.num_item)
    # 저장된 모델을 이용해 평가만 진행
    else:
        best_model = model
        best_model.load_state_dict(torch.load(config.save_model_path))

    # best model을 이용해 모델 평가
    NDCG_10, HIT_10, HIT_1 = evaluate(
        model=best_model,
        user_test=user_test,
        max_len=config.max_len,
        bert4rec_dataset=bert4rec_dataset,
        num_item=make_sequence_dataset.num_item,
    )

    print('NDCG@10 score : ', NDCG_10)
    print('HIT@10 score : ', HIT_10)
    print('HIT@1 score : ', HIT_1)
