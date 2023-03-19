# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    nosleguma_laiks = [0] * n
    thread = [[] for f in range(n)]

    for i in range(m):
        min_laiks = min(nosleguma_laiks)
        min_n = nosleguma_laiks.index(min_laiks)
        thread[min_n].append(i)

        sakuma_laiks = max(nosleguma_laiks[min_n],0)
        nosleguma_laiks[min_n] = sakuma_laiks + data[i]
        output.append((min_n, sakuma_laiks))


    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m = map(int, input().split())
    

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for i, sakuma_laiks in result:
        print(i, sakuma_laiks)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
