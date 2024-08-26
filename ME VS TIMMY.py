def repeat():

    while True:
        first_number = float(input("First Number Please " ))
        operator = input("+,-,*or/ " )
        second_number = float(input("Second Number Please " ))

        if operator == ("+"):
            answer = first_number + second_number
            print (answer)

        if operator == ("-"):
            answer = first_number - second_number
            print (answer)

        if operator == ("*"):
            answer = first_number * second_number
            print (answer)
            
            if operator == ("/"):
                answer = first_number / second_number
                print (answer)



repeat()