print(input('please enter your choice:'))
def get_statistics(data):
    print('dataset statistics:')
    print(f'minimum value: {min(data)}')
    print(f'maximum value: {max(data)}')
    print(f'sum of all value: {sum(data)}')
    print(f'average value: {sum(data)/len(data)}')
data = [34,12,56,78,43,21,90]
get_statistics(data)
