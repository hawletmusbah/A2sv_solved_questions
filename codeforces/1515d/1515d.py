import sys
 
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    t = int(next(it))
    
    results = []
    for _ in range(t):
        n = int(next(it))
        l = int(next(it))
        r = int(next(it))
        
        lcnt = [0] * (n + 1)
        rcnt = [0] * (n + 1)
        
        for i in range(n):
            color = int(next(it))
            if i < l:
                lcnt[color] += 1
            else:
                rcnt[color] += 1
        
        for i in range(1, n + 1):
            match = min(lcnt[i], rcnt[i])
            lcnt[i] -= match
            rcnt[i] -= match
            l -= match
            r -= match
        
        if l < r:
            lcnt, rcnt = rcnt, lcnt
            l, r = r, l
            
        ans = 0
        extra_on_left = l - r
        for i in range(1, n + 1):
            can_form_pairs = lcnt[i] // 2
            do_moves = min(can_form_pairs, extra_on_left // 2)
            
            ans += do_moves
            l -= 2 * do_moves
            extra_on_left -= 2 * do_moves
            
        ans += (l - r) // 2 + (l + r) // 2
        results.append(str(ans))
        
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    solve()