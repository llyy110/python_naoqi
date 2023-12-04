import pickle
import os
import random

pic_data_dir = 'C:/Users/35472/naoqi/pic_datas'


def get_pic_remote(pic_data_name):
    with open(os.path.join(pic_data_dir, pic_data_name), 'rb')as f:
        m = pickle.load(f)
    return m


def get_random_remote():
    pic_data_names = os.listdir(pic_data_dir)
    random_name = random.choice(pic_data_names)
    return get_pic_remote(random_name)


if __name__ == '__main__':
    pic_remote = get_random_remote()
    print(pic_remote)
