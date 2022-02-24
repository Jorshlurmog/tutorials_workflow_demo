numbers = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
count_seq = [2, 12]

while True:
    for i in range(len(count_seq) - 1):
        next_num = ''
        if i > 0:
            consecutive_num = 1
            for num in str(count_seq[i]):
                if count_seq[i][num] == count_seq[i][num - 1]:
                    consecutive_num += 1
                next_num += str(consecutive_num)
                next_num += str(count_seq[i][num])
        count_seq.append(next_num)    
        print(count_seq)

         
    

