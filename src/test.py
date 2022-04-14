from utils.indexer import Indexer

def test_index():
    index = Indexer(0, [])
    while True:
        op = int(input('> '))
        if op == 1:
            print('allocate:', index.allocate())
        elif op == 2:
            index.free(int(input('free: ')))
            print(index)
        elif op == 3:
            print(index)

if __name__ == '__main__':
    test_index()