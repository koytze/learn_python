'''

Exercise 16

Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    - Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

'''
import random,string

UserRequest = int(input('''Choose the complexity of your password:\n 
                        1. Weak (4-6 chars)\n
                        2. Medium (7-10 chars)\n
                        3. Hard (11-17 chars and special chars)\n
                        Your choice is: '''))

def p_gen(x):

    if x == 1:
        chars = string.ascii_letters + string.digits
        spec_chars = '!@#$%^&*()_+=-|\\[]{}`~:;,./?"\''
        length = random.randint(4,6)
        p = ''.join(random.sample(chars, length))
        print(p, 'lenght: ', len(p))
    elif x == 2:
        chars = string.ascii_letters + string.digits
        spec_chars = '!@#$%^&*()_+=-|\\[]{}`~:;,./?"\''
        length = random.randint(7,10)
        p = ''.join(random.sample(chars,length))
        print(p, 'lenght: ', len(p))
    elif x == 3:
        chars = string.ascii_letters + string.digits
        spec_chars = '!@#$%^&*()_+=-|\\[]{}`~:;,./?"\''
        all = chars + spec_chars
        length = random.randint(11,17)
        p = ''.join(random.sample(all,length))
        print(p, 'lenght: ', len(p))
    elif len(x) < 1:
        print('You did not choose any option!')

    else:
        print('You choose an unexisting value!')



p_gen(UserRequest)


