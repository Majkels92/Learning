lista = [1, 2, "Empty slot", 5, "Empty slot", "Empty slot", 6]

def bubble_sorting(sorted_list):
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == "Empty slot":
            if sorted_list[i+1] != "Empty slot":
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
            elif sorted_list[i+1] == "Empty slot":
                k = 1
                while i+k != len(sorted_list):
                    if sorted_list[i + k] != "Empty slot":
                        sorted_list[i], sorted_list[i+k] = sorted_list[i+k], sorted_list[i]
                    k += 1
    return sorted_list

print(bubble_sorting(lista))

