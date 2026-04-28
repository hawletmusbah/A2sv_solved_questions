import sys

def solve():
    # Read n
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    adj = []
    for _ in range(n):
        adj.append(sys.stdin.readline().strip())

    # p_res will store the final permutation
    p_res = [0] * n

    # We iterate through each value i (from 1 to n)
    for i in range(1, n + 1):
        before_count = 0
        # Check every other value j to see if it comes before i
        for j in range(1, n + 1):
            if i == j:
                continue
            
            # Use 0-based indexing for the adjacency matrix string
            u, v = i - 1, j - 1
            
            if j < i:
                # If j < i, j comes before i if there is an edge
                if adj[u][v] == '1':
                    before_count += 1
            else:
                # If j > i, j comes before i if there is NOT an edge
                if adj[u][v] == '0':
                    before_count += 1
        
        # before_count is the number of elements before value i
        # So p[before_count] = i
        p_res[before_count] = i

    print(*(p_res))

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line.strip())
        for _ in range(t):
            solve()

if __name__ == '__main__':
    main()