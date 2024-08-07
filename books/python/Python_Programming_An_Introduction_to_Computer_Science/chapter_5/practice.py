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
    decoded_message = []
    for n in encoded_message:
        n = int(n)
        decoded_message.append(chr(n))
    final_message = ''.join(decoded_message)
    print(final_message)

def date_conversion():
    date_input = input('Give a date: ').split('/')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    month = ''
    for i in range(1, 13):
        if int(date_input[1]) == i:
            month = months[i-1]
    result = f'{month} {date_input[0]}, {date_input[2]}'
    print(result)

def file_proc():
    name = 'chapter_5\quotes.txt'
    infile = open(name, 'r')
    new_file = open('chapter_5\output.txt', 'w')

    for line in infile:
        print(f'{line} TEST!!', file=new_file, end='')
    infile.close()
    new_file.close()

file_proc()