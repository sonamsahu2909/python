def get_unique_to_bring(M,N,common_stones):
    mars_weight = list(range(1,M+1))
    earth_weight = common_stones
    mars_set = set(mars_weight)
    earth_set = set(earth_weight)  
    unique_mars_weights = list(mars_set-earth_set)
    unique_mars_weights.sort()
    total_weight = 0
    num_stones_selected = 0 
    
    for weight in unique_mars_weights:
        if total_weight + weight <=M:
            total_weight+=weight
            num_stones_selected+=1
        else:
            break
    return num_stones_selected


input1 = int(input("etr the capacity of rob's bag:")) #10
input2 = int(input("etr the number of common stones on earth:")) #3
input3 = list(map(int,input("list of stones from earth:").split())) #[2,3,4,5,7,9,10]

# call

output = get_unique_to_bring(input1,input2,input3)
print(output)