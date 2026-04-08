print(input('please enter your choice:'))
print('choose sorting option:')
print('1. ascending')
print('2. descending')
sort_choice= input('enter your choice:')
def sort_data(data):
    if sort_choice == '1':
        sorted_data = sorted(data)
        order = 'descending'
    elif sort_choice == '2':
        sorted_data = sorted(data, reverse=True)
        order = 'descending'
    else:
        print('invalid choice')
        return
    print(f'sorted data in {order} order:')
    print(', '.join(map(str,sorted_data)))
data = [34,12,56,78,43,21,90]
sort_data(data)