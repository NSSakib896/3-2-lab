def calculate_parameters(process,result):
    process.sort(key= lambda x:x[0])
    result.sort(key= lambda x:x[0])
    n=len(process)
    avg_tat=0
    avg_wt=0
    #tat,wt
    parameters=[
        ['p_id','p_tat','p_wt']
    ]
    for i in range(n):
        p_id=process[i][0]
        p_at=process[i][1]
        p_bt=process[i][2]
        p_ct=result[i][1]
        avg_tat+=p_ct-p_at
        avg_wt+=p_ct-p_at-p_bt
        parameters.append([p_id,p_ct-p_at,p_ct-p_at-p_bt])
    for i in range(len(parameters)):
        print(parameters[i])
    avg_tat=avg_tat/n
    avg_wt=avg_wt/n
    print("average tat =",avg_tat)
    print("average wt =",avg_wt)
    return parameters
