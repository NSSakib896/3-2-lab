def take_input():
    n=int(input())
    #p_id,p_at,p_bt
    process_list=[]
    for i in range(n):
        p_id=input()
        at=int(input())
        bt=int(input())
        process_list.append([p_id,at,bt])
    print(process_list)
    process_list.sort(key = lambda x:x[1])
    return process_list