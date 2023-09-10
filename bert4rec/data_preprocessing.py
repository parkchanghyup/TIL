from collections import defaultdict

class DataPreprocessing():
    """
    SequenceData 생성 클래스
    """
    def __init__(self, config, train_df, test_df, item_df):
        self.config = config
        self.train_df = train_df
        self.test_df = test_df
        self.item_df = item_df

        self.item_encoder, self.item_decoder = self.generate_encoder_decoder(self.item_df, 'items')
        self.num_item, self.num_user = len(self.item_df), len(self.train_df)
        self.user_train, self.user_test = self.generate_sequence_data()

    def generate_encoder_decoder(self, df, col: str) -> dict:
        """
        user id 와 item id를 단순히 int 형으로 변환시켜주는 함수

        Args:
            df (pd.DataFrame): 변환할 데이터 프레임
            col (str): 생성할 columns 명
        Returns:
            dict: 생성된 encoder, decoder
        """

        encoder = {}
        decoder = {}
        ids = df[col].unique()

        for idx, _id in enumerate(ids):
            encoder[_id] = idx
            decoder[idx] = _id

        return encoder, decoder

    def generate_sequence_data(self) -> dict:
        """
        data frame을 이용해 모델 학습에 사용가능하도록 변환시켜주는 함수

        Returns:
            dict: train user sequence / test user sequence
        """
        user_train = defaultdict(list)
        user_test = defaultdict(list)

        for idx in range(len(self.train_df)):
            items = self.train_df['item'][idx]
            items = [self.item_encoder[item] + 1 for item in items]
            user_train[idx] = items

        for idx in range(len(self.test_df)):
            items = self.test_df['item'][idx]
            items = [self.item_encoder[item] + 1 for item in items]
            label = self.test_df['label'][idx]
            user_test[idx] = items+[self.item_encoder[label] + 1]
        return user_train, user_test

    def get_train_test_data(self):
        return self.user_train, self.user_test