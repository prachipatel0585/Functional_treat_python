print(input('please enter your choice:'))
def input_data():
    data= input('enter data for a 1D array:')
    return list(map(int, data.split()))
data = input_data()
print('data has been stored successfully! \n')