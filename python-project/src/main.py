def main() -> None:
    num=10;
    num2=20;
    sum=sum_numbers(num, num2);
    if sum>10:
        print("Hello, World!")
        print("Hello from python-project!")
        print("The sum of", num, "and", num2, "is", sum)
    for i in range(10):
        print(i)

def sum_numbers(num, num2):
    return num+num2;

if __name__ == "__main__":
    main()
