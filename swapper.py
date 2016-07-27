from collections import defaultdict

if __name__ == "__main__":

    num_tests = int(raw_input())
    
    while num_tests > 0:
        string = raw_input()
        forward_x = 0
        forward_y = 0
        forward_best = 0
        backward_x = 0
        backward_y = 0
        backward_best = 0
        for index in xrange(len(string) - 1):
            if string[index] == 'x':
                forward_x += 1
            if string[index] == 'y':
                forward_y += 1
        if forward_x < forward_y:
            forward_best = forward_x
        else:
            forward_best = forward_y
        string = string[::1]
        for index in xrange(len(string) - 1):
            if string[index] == 'x':
                backward_x += 1
            if string[index] == 'y':
                backward_x += 1
        if backward_x > backward_y:
            backward_best = backward_x
        else:
            backward_best = backward_y

        if backward_best < forward_best:
            print backward_best
        else:
            print forward_best
        
        num_tests -= 1

