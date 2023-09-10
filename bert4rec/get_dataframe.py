import json
from tqdm import tqdm
from datetime import datetime
import random
import pandas as pd


def load_json(fname):
    with open(fname, encoding="utf-8") as f:
        json_obj = json.load(f)
    return json_obj


def get_dataframe(data_path, config):
    """
    json 형태의 파일을 불러와 가공하고 data frame 형태로 반환하는 함수

    Args:
        data_path : json 파일 path
        config

    Returns:
        train_df, test_df, item_df
    """

    # json 파일 load
    train_ = load_json(data_path[0])
    test_ = load_json(data_path[1])
    test_label = load_json(data_path[2])

    max_len = config.max_len
    session = config.session
    train_sample_length = config.train_sample_length

    # data frame 생성
    train_df = get_train_df(train_, max_len=max_len, train_sample_length=train_sample_length, session=session)
    test_df = get_test_df(test_, test_label, session=session)
    item_df = get_item_df(train_df, test_df)

    return train_df, test_df, item_df


def get_item_df(train_df, test_df):
    """
    train과 test에 등장하는 모든 item을 추출해 dataframe 형태로 반환
    """
    all_item = []
    for train_item in train_df['item']:
        all_item.extend(train_item)
    for test_item in test_df['item']:
        all_item.extend(test_item)
    for item in test_df['label']:
        all_item.append(item)

    all_items = list(set(all_item))
    item_df = pd.DataFrame(all_items, columns=['items'])

    return item_df


def get_test_df(test_log, test_label, session=None):
    """
    test_df 생성 함수

    Args:
        test_log : dict 형태의 test 원본 데이터
        test_label : test데이터의 label이 정의되어 있는 데이터
        session : 유저의 log를 session 별로 나눌지 여부

    Returns:
        test_df
    """
    users = list(test_log.keys())

    # 유저의 log중 마지막 session만 활용
    if session:
        items = get_session_data(test_log)
    # 유저의 전체 log 활용
    else:
        items = []
        for user in users:
            test_item = [item for item, _ in test_log[user]]
            items.append(test_item)

    # data frame으로 생성
    temp_ = []
    for idx in range(len(users)):
        temp_.append([users[idx], items[idx]])
    test_df = pd.DataFrame(temp_, columns=['user', 'item'])
    test_label_df = pd.DataFrame(test_label).T
    test_label_df.columns = ['item', 'timestamp']
    test_df['label'] = test_label_df['item'].to_list()

    return test_df


def get_train_df(train_log, max_len=50, train_sample_length=None, session=False):
    """
    train_df 생성 함수

    Args:
        train_log : dict 형태의 train 원본 데이터
        max_len : 학습에 사용한 log의 최대 길이
        train_sample_length : 학습에 사용할 sample의 갯수
        session : 유저의 log를 session 별로 나눌지 여부

    Returns:
        train_df
    """
    valid_user = []
    valid_item = []

    # 유저의 log를 session으로 나눠서 활용
    if session:
        items = get_session_data(train_log)
        # 유저 재정의
        users = ['user_' + str(num) for num in range(len(items))]
        user_log_len = [len(item) for item in items]

        # 유저 데이터를 전부 활용하지 않고
        # lop가 너무 길거나 짧은 유저의 데이터는 제거
        # 해당 수치는 데이터 분포를 보고 임의적으로 판단
        for idx, user in tqdm(enumerate(users)):

            if user_log_len[idx] < 5 or user_log_len[idx] > 50:
                continue
            else:
                valid_item.append(items[idx][-max_len:])
                valid_user.append(user)

    # 유저의 log를 session으로 나누지 않고 활용
    else:
        users = list(train_log.keys())
        items = []
        for user in tqdm(users):
            temp_1 = []
            for item, str_time in train_log[user]:
                temp_1.append(item)
            items.append(temp_1)

        user_log_len = [len(item) for item in items]
        # 유저 데이터를 전부 활용하지 않고
        # lop가 너무 길거나 짧은 유저의 데이터는 제거
        # 해당 수치는 데이터 분포를 보고 임의적으로 판단
        for idx, user in tqdm(enumerate(users)):

            if user_log_len[idx] < 9 or user_log_len[idx] > 84:
                continue
            else:
                valid_item.append(items[idx][-max_len:])
                valid_user.append(user)

    if train_sample_length:
        # random.seed(0)
        random_sample = random.sample(range(len(valid_user)), train_sample_length)
        temp_ = []
        for idx in random_sample:
            temp_.append([valid_user[idx], valid_item[idx]])
    else:
        temp_ = []
        for idx in range(len(valid_user)):
            temp_.append([valid_user[idx], valid_item[idx]])
    train_df = pd.DataFrame(temp_, columns=['user', 'item'])

    return train_df


def get_session_data(log_data, type='train'):
    """
    유저의 session을 분리하는 함수
    type이 train이 아니면 마지막 session만 활용
    """
    users = list(log_data.keys())
    new_items = []

    for user in tqdm(users):
        temp_item = [log_data[user][0][0]]
        user_click = log_data[user]
        for idx in range(1, len(user_click)):
            time_1 = datetime.strptime(user_click[idx - 1][1], "%Y-%m-%d %H:%M:%S")
            time_2 = datetime.strptime(user_click[idx][1], "%Y-%m-%d %H:%M:%S")
            time_diff = time_2 - time_1
            # 30분 이상 차이나면 다른 세션으로 판단
            if time_diff.total_seconds() > 60 * 30:
                if type == 'train':
                    new_items.append(temp_item)
                temp_item = [user_click[idx][0]]
            else:
                temp_item.append(user_click[idx][0])
        new_items.append(temp_item)

    return new_items