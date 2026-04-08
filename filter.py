print(input('please enter your choice:'))
threshold = int(input('enter a threshold value to filter out data about this value:'))
def filter_data(data,threshold):
    filtered= list(filter(lambda x:x >= threshold,data))
    return filtered
data = [34,12,56,78,43,21,90]
filtered_result = filter_data(data,threshold)
print(f"filtered data (values >= {threshold}):")
print(', '.join(map(str, filtered_result)))
filter_data(data,threshold)
