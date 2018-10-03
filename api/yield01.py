def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=", i)

    print("do somthing...")
    print("end.")


def call(i):
    print("call:", i)
    return i * 2


def main():
    for i in yield_test(5):
        print(i, "---")


main()
