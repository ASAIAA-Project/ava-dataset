from cgi import test
import os, json
import numpy as np
import pickle

def pp():
    idx = np.arange(255508)
    np.random.shuffle(idx)
    sp = [229957, 12775, 12776]
    # 229957, 242732, 255508
    train_idx = idx[:229957]
    test_idx = idx[229957:242732]
    val_idx = idx[242732:]
    print(len(train_idx), len(test_idx), len(val_idx))
    train_data = []
    test_data = []
    val_data = []
    with open('AVA/AVA_corrected.txt', 'r') as lines:
        for i, line in enumerate(lines):
            data = [int(l) for l in line.split()[1:]]
            votes = sum(data[1:11])
            ttl = sum([(w+1)*v for w, v in enumerate(data[1:11])])
            score = ttl/votes
            data_pp = [data[0]] + [d/votes for d in data[1:11]] + [score]
            if i in train_idx:
                train_data.append(data_pp)
            if i in test_idx:
                test_data.append(data_pp)
            if i in val_idx:
                val_data.append(data_pp)
    
    with open('train.pickle', 'wb+') as handle:
        pickle.dump(np.array(train_data), handle)
    with open('test.pickle', 'wb+') as handle:
        pickle.dump(np.array(test_data), handle)
    with open('val.pickle', 'wb+') as handle:
        pickle.dump(np.array(val_data), handle)

def pp_check():
    with open('train.pickle', 'rb') as handle:
        train_data = pickle.load(handle)
    with open('test.pickle', 'rb') as handle:
        test_data = pickle.load(handle)
    with open('val.pickle', 'rb') as handle:
        val_data = pickle.load(handle)

    for data in [train_data, test_data, val_data]:
        print(len(data))
        print(data[0])
        print(data[1])

if __name__ == "__main__":
    pp_check()