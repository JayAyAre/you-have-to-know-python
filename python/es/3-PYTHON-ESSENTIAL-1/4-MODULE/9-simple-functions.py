"""
    Key takeaways

        1. A variable that exists outside a function has a scope inside the function body (Example 1) 
            unless the function defines a variable of the same name (Example 2, and Example 3), e.g.:

            Example 1:

                var = 2


                def mult_by_var(x):
                    return x * var


                print(mult_by_var(7))    # outputs: 14

            Example 2:

                def mult(x):
                    var = 5
                    return x * var


                print(mult(7))    # outputs: 35

            Example 3:

                def mult(x):
                    var = 7
                    return x * var


                var = 3
                print(mult(7))    # outputs: 49

        2. A variable that exists inside a function has a scope inside the function body (Example 4), e.g.:

            Example 4:

                def adding(x):
                    var = 7
                    return x + var


                print(adding(4))    # outputs: 11
                print(var)    # NameError
        
        3. You can use the global keyword followed by a variable name to make the variable's scope global, e.g.:

                var = 2
                print(var)    # outputs: 2


                def return_var():
                    global var
                    var = 5
                    return var


                print(return_var())    # outputs: 5
                print(var)    # outputs: 5

        
        Exercise 1

            What will happen when you try to run the following code?

                def message():
                    alt = 1
                    print("Hello, World!")


                print(alt)

        Exercise 2

            What is the output of the following snippet?

                a = 1


                def fun():
                    a = 2
                    print(a)


                fun()
                print(a)

        Exercise 3

            What is the output of the following snippet?

                a = 1


                def fun():
                    global a
                    a = 2
                    print(a)


                fun()
                a = 3
                print(a)

        Exercise 4

            What is the output of the following snippet?

                a = 1


                def fun():
                    global a
                    a = 2
                    print(a)


                a = 3
                fun()
                print(a)

"""
