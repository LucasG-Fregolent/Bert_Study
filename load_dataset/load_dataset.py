import os
import random

class LoadDataset:
    def __init__(self, path):
        max_valid = 5000
        self.path = path
        x_train_pos = self.load_texts(self.path + '/aclImdb/train/pos')
        x_train_neg = self.load_texts(self.path + '/aclImdb/train/neg')
        x_test_pos  = self.load_texts(self.path + '/aclImdb/test/pos')
        x_test_neg  = self.load_texts(self.path + '/aclImdb/test/neg')

        x_train = x_train_pos + x_train_neg
        x_test  = x_test_pos + x_test_neg
        y_train = [True] * len(x_train_pos) + [False] * len(x_train_neg)
        y_test  = [True] * len(x_test_pos)  + [False] * len(x_test_neg)

        c = list(zip(x_train, y_train))
        random.shuffle(c)
        x_train, y_train = zip(*c)

        x_valid = x_train[-max_valid:]
        y_valid = y_train[-max_valid:]
        x_train = x_train[:-max_valid]
        y_train = y_train[:-max_valid]

        print('\nFirst two train samples:')
        for i, (source, target) in enumerate(zip(x_train[:2], y_train[:2])):
            print(f"{i}: Input: {source}\n   Target: {'positive' if target else 'negative'}\n")

        print('-'*200)
        print('\nFirst two valid samples:')
        for i, (source, target) in enumerate(zip(x_valid[:2], y_valid[:2])):
            print(f"{i}: Input: {source}\n   Target: {'positive' if target else 'negative'}\n")

        print('-'*200)
        print(f'Train size: {len(x_train)}')
        print(f'Valid size: {len(x_valid)}')
        print(f'Test size: {len(x_test)}')
    
    def load_texts(self, folder):
        texts = []
        for path in os.listdir(folder):
            with open(os.path.join(folder, path)) as f:
                texts.append(f.read())
        return texts