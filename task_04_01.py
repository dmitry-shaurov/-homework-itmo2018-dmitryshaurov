n = int(input())
p = int(input())
with open('data.txt', 'r') as f:
    with open("out-1.txt", 'w') as result_1:
        with open("out-2.txt", 'w') as result_2:
                for i in f.read().strip().split(' '): # convert to list
                    if int(i) % n == 0:
                        result_1.write('{} '.format(i))
                        result_2.write('{} '.format(int(i)**p))
                    else:
                        result_2.write('{} '.format(int(i)**p))
