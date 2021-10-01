from math import sqrt
def main():
    my_dict = {i: sqrt(i) for i in range(1, 1000)}
    print(my_dict)

if __name__ == '__main__':
    main()