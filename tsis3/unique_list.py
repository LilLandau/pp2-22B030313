def unique_list(elements):
    unique_elements = []
    
    for x in elements:
        if x not in unique_elements:
            unique_elements.append(x)

    return unique_elements