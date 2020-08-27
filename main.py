def timeElapsed(hour, minute, second):
    return (hour * 3600) + (minute * 60) + second


def main():
    hr = int(input("Enter hour: "))
    minu = int(input("Enter minute: "))
    second = int(input("Enter second: "))
    
    print("Time elapsed: ",timeElapsed(hr, minu, second)," Second!")



main()