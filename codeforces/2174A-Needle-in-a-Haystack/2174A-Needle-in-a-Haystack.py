c= int(input())
for i in range(c):
    s = input()
    s = [str(i) for i in s ]
    t = input()
    t = [str(i) for i in t ]
    n = len(t)
    # print(t)
    possible = True
    for i in s:
        if i in t:
            t.remove(i)
        else:
            print("Impossible")
            possible = False
            break
    if possible:
        t.sort()
        # print(t)
        p_t = 0
        p_s = 0
        while p_t < len(t) and p_s < len(s) :
            
            if t[p_t] >= s[p_s]:
                t.insert(p_t , s[p_s])
                p_s += 1
                p_t += 1
            else:
                p_t += 1
        while p_s < len(s):
            t.append(s[p_s])
            p_s += 1
    
        print("".join(t))