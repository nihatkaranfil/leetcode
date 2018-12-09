def FizzBuzz (n) :
    """a function that outputs the string representation of numbers from 1 to n
    But for multiples of three it should output “Fizz” instead of the number and
    for the multiples of five output “Buzz”. For numbers which are multiples of
    both three and five output “FizzBuzz”."""

    new_list = []  # first empty list to create the final list 
    
    for x in range (1, n+1): # n times for loop
        
        if x % 15 == 0 : # multiples of both three and five, which is same as multiples of 15 
                        
            new_list.append ( "FizzBuzz" ) # if the number multiples of both, then append as "FizzBuzz" to the list
                                           
        elif x % 5 == 0: # multiples of  five
                
                new_list.append( "Buzz" ) # if the number multiples of five, then append as "Buzz" to the list
        
        elif x % 3 == 0: # multiples of three
        
            new_list.append ( "Fizz" ) # if the number multiples of three, then append as "Fizz" to the list
        
        else: # multiples of neither five nor three
        
            new_list.append (str(x)) # if the number is not multiples of either five or three, then add the number as a string 
    
    return new_list

FizzBuzz(100) # n=100 as an example to execute the function
