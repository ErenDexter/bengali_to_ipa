import pandas as pd

with open('trainIPAdb_u.csv', encoding='utf-8') as csv_file:
    train_df = pd.read_csv(csv_file)
    with open('Data/src_train.txt', 'w', encoding='utf-8') as src_train:
        with open('Data/tgt_train.txt', 'w', encoding='utf-8') as tgt_train:
            with open('Data/src_val.txt', 'w', encoding='utf-8') as src_val:
                with open('Data/tgt_val.txt', 'w', encoding='utf-8') as tgt_val:
                    for i in range(train_df.shape[0]):
                        if i <= int(train_df.shape[0] * 0.8):
                            src_train.write(train_df['text'][i] + '\n')
                            tgt_train.write(train_df['ipa'][i] + '\n')
                        else:
                            src_val.write(train_df['text'][i] + '\n')
                            tgt_val.write(train_df['ipa'][i] + '\n')


with open('testData.csv', encoding='utf-8') as test_data_csv:
    test_df = pd.read_csv(test_data_csv)
    with open('Data/src_test.txt', 'w', encoding='utf-8') as src_test:
        for i in range(100):
            src_test.write(test_df['text'][i] + '\n')
