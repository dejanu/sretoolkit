# a+=b extends
# a = a + b creates new object

l = [i for i in range(10)]
ll = l

l = l + [100]

if __name__ == "__main__":

    print(f"l is {l} and ll is {ll}")
