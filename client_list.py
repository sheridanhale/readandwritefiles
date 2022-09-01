from ast import Or


def main():
    infile = open("clients.txt",'r')

    i=0
    for clients in infile:
        i+=1
        print(i,'. ',clients.rstrip('\n'), sep = '', )

main()

Or

def main():
    infile = open("clients.txt",'r')
    counter = 1

    for line in infile:
        print(counter, ".", line.rstrip('\n'), sep='')

        counter += 1