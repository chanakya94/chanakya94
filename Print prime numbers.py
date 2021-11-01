def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n=int(input()) #declare an input
    for i in range(n): #declaring range
        if i>1: #checking if it is greater than 1
            for j in range(2,i): #Delaring range
                if(i%j==0):#checking if it devides or not
                    break #if it devides then it breaks
            else:
                print(i)#prints the stored value

    return 0

if __name__ == '__main__':
    main()