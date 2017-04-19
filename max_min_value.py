def find_max_min(number_list):

    out_put = []
    max_value = max(number_list)
    min_value = min(number_list)

    if min_value != max_value:
        out_put.append(min_value)
        out_put.append(max_value)
    else:
        out_put.append(len(number_list))

    print(out_put)
