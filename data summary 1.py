print(input('please enter your choice:'))
def data_summary(data):
    print('\ndata summary:')
    print(f'- total elements: {len(data)}')
    print(f'- minimum value: {min(data)}')
    print(f'-maximum value: {max(data)}')
    print(f'-sum of all values: {sum(data)}')
    print(f'-average value: {sum(data)/len(data)}')
data = [34,12,56,78,43,21,90]
data_summary(data)