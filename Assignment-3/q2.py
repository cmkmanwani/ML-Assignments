import sys
import pandas
import utils
import numpy as np
import pickle
from NN import NN


def part_a(
    train_filename,
    test_filename,
    one_hot_train_filename,
    one_hot_test_filename
):
    data = pandas.read_csv(train_filename, header=None)
    X_train = data.drop(10, axis=1).values
    Y_train = data[10].values

    cols_to_encode = range(10)
    col_values = [[1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                  [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                  [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                  [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                  [1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]
    X_train = utils.one_hot_encoder(X_train, cols_to_encode, col_values)
    Y_train = utils.one_hot_encoder(np.reshape(Y_train, (Y_train.shape[0], 1)),
                                    [0], [range(10)])

    data = np.hstack((X_train, Y_train))
    np.savetxt(one_hot_train_filename, data.astype(int), delimiter=',',
               fmt='%d')

    data = pandas.read_csv(test_filename, header=None)
    X_test = data.drop(10, axis=1).values
    Y_test = data[10].values

    X_test = utils.one_hot_encoder(X_test, cols_to_encode, col_values)
    Y_test = utils.one_hot_encoder(np.reshape(Y_test, (Y_test.shape[0], 1)),
                                   [0], [range(10)])
    data = np.hstack((X_test, Y_test))
    np.savetxt(one_hot_test_filename, data.astype(int), delimiter=',',
               fmt='%d')


def part_b(
    config_file,
    train_filename,
    test_filename
):
    nn = NN(85, 10, [5])
    nn.fit(X_train, Y_train, lr=1, epochs=500, batch_size=100)


def part_c(
    train_filename,
    test_filename
):
    print('part-c')


def part_d(
    train_filename,
    test_filename
):
    print('part-d')


def main(
    args
):
    part = args[-1]
    if part == 'a':
        part_a(args[0], args[1], args[2], args[3])
    elif part == 'b':
        part_b(args[0], test_filename)
    elif part == 'c':
        part_c(args[0], test_filename)
    elif part == 'd':
        part_d(args[0], test_filename)
    # elif part == 'e':
    #     part_e(train_filename, test_filname)
    # elif part == 'f':
    #     part_e(train_filename, test_filname)
    # elif part == 'g':
    #     part_g(train_filename, test_filname)
    else:
        print('Invalid question part. a-f Valid')
        exit()


if __name__ == '__main__':
    main(sys.argv[1:])
