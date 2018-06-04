def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))  #it is the old (Python 2.7 ) way to format00

if __name__ == "__main__":
    main()
