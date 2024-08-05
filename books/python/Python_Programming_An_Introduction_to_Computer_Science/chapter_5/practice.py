def months_list():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = int(input("Give a month's number: "))

    print(months[month - 1])

def encoder():
    input_message = input('Give the message to encode.')
    for c in input_message:
        print(ord(c), end=' ')

def decoder():
    encoded_message = input('Give the sequence of numbers to decode. ').split()
    decoded_message = ''
    for n in encoded_message:
        n = int(n)
        decoded_message = decoded_message + chr(n)
    print(decoded_message)

decoder()