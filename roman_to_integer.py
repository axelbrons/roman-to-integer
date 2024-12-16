def romanToInt():
    """
    :type s: str
    :rtype: int
    """
    s_data = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    s_data_letter = ['I','V','X','L','C','D','M']
    s_data_number = [1, 5, 10, 50, 100, 500, 1000]

    s = input()
    nb = 0
    s_list = list(s)
    #print(len(s_list))
    temp = 0

    # Only roman letter and less than 15 characters
    for k in range(len(s_list)):
        for key in s_data:
            if s_list[k] == key:
                temp += 1
    if temp != len(s_list) or len(s_list) >= 15:
        print("Please only roman letter")
        exit()

    # Finding more than 3 same following letter
    temp_same = s_list[0]
    #print(temp_same)
    count = 0
    for n in range(1,len(s_list)):
        if s_list[n] == temp_same:
            count += 1
            #print(count)
            if (count == 1) and ((s_list[n] != 'X') and (s_list[n] != 'I')):
                #print(count)
                print("Impossible to get more than 2 letters of this")
                exit()
            if (count == 3):
                #print(count)
                print("Impossible to have more than 3 letters")
                exit()
        else:
            temp_same = s_list[n]
            count = 0

    # The letter I is only last or last -1
    if len(s_list) > 2:
        for g in range(len(s_list) - 3, -1, -1):
            if (s_list[g] == 'I') and g == len(s_list) - 3:
                if s_list[len(s_list)-2] != 'I' or s_list[len(s_list)-1] != 'I':
                    print("'I' are only in last or last - 1 or last - 2 if there are 'III'")
                    exit()
            if (s_list[g] == 'I') and g != len(s_list) - 3:
                print("2 :'I' are only in last or last - 1 or last - 2 if there are 'III'")
                exit()

    # Check if the biggest letter is on the left (also verify the principle of IV and IX)
    temp = 0
    for j in range(len(s_list)-1):
        for m in range(1,len(s_list) - j):
            if s_list[j] != 'I':
                #print(s_data[s_list[j]], s_data[s_list[j + m]])
                if s_data[s_list[j]] < s_data[s_list[j + m]]:
                    if m == 1:
                        print()
                    #print(s_data[s_list[j]], s_data[s_list[j + m]])
                    print("In roman number, the bigger is on the left and the smaller on the right")
                    exit()

        if s_list[j] == 'I':
            if (s_list[j + 1] != 'V') and (s_list[j + 1] != 'X') and (s_list[j + 1] != 'I'):
                print("'I' can be following only by 'V', 'X' or 'I'")
                exit()

    # Calcul of the number
    for i in range(len(s_list)):


        if i != len(s_list) - 1 :
            if s_list[i] == 'I' and s_list[i + 1] == 'V':
                nb += 4
                break
            if s_list[i] == 'I' and s_list[i + 1] == 'X':
                nb += 9
                break
        if s_list[i] == 'I':
            nb += 1
        if s_list[i] == 'V':
            nb += 5
        if s_list[i] == 'X':
            nb += 10
    return nb

if __name__ == "__main__":
    nb = romanToInt()
    print(nb)
