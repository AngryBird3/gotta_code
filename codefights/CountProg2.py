'''
Esoteric programming language, or esolang, as the name suggests, is a kind of programming language that is meant to be only understood by a few people. The reasons for their existence vary, ranging from studying the mathematical structure of program to just having fun. Among all kinds of esolangs, Brainfuck is perhaps the most well known one. You can find the detail about this programming language following the link, but for the purpose of this challenge, let me briefly summarize what a Brainfuck program is.

A Brainfuck program is composed of eight types of commands, represented by these eight characters: >, <, +, -, ., ,, [ and ]. A Brainfuck program is valid, if the brackets [ and ] are matched as parentheses do. As regular parenthesis, they can also be nested. For example, +++, [->+<], and ,>++++[->++++++++[-<<+>>]<]<.[-] are all valid Brainfuck programs, but +++<[ and []],. are not.

Because it has only eight kinds of commands, it is possible to count the number of valid programs of a specified length. This is your task: calculate the number of valid Brainfuck program of the given length. Since this number grows exponentially, return the answer modulo 109 + 7.

Example

For length = 1, the output should be
CountProgram(length) = 6.
For length = 2, the output should be
CountProgram(length) = 37.
Input/Output

[time limit] 4000ms (py)
[input] integer length

The specified length.

Constraints:
1 ≤ length ≤ 1000.

[output] integer

The number of valid Briainfuck programs of the given length modulo 109 + 7.
'''
def CountProgram(length):
    '''
    6 symbols can be used without order
    2 symbols require we have at least 2 len to use them
    '''
    opt = [0]*(max(length+1, 3))
    opt[0] = 1
    opt[1] = 6
    #opt[2] = 37
    for i in range(2, length+1):
        print "i: ", i
        opt[i] = opt[i-1]*6 #ith char is non-bracket
        #If its ']' then '[' can be anywahere in 1..length-1
        for j in range(1, i):
            left = opt[j-1]
            right = opt[i-j-1]
            opt[i] += left * right
            print "j: ", j, " left: ", left, " right: ", right
        print "i: ", i, " opt[i]: ", opt[i]
    return opt[length]
CountProgram(5)
