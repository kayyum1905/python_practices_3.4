import multiprocessing
import time


def get_square(arry):  # arry = our_array, rslt = reult
    for index, n in enumerate(arry):
        result[index] = n*n
    print('Inside process the result array: ', str(result[:]))


def get_single_value(v):  # v = single_value
    v.value = 43.65  # the variable single_value is set to
    print('Inside process the single value: ', v.value)

if __name__ == '__main__':
    our_array = [1, 2, 5, 11]  # this list elements will be used for calculations
    result = multiprocessing.Array('i', 4)  # result of our_array squared, 'i' int, 4 is length
    single_value = multiprocessing.Value('d', 0.0)  # single variable that will be passed, 'd' float, 0.0 initial value

    # this will process: result, queue
    our_process1 = multiprocessing.Process(target=get_square, args=(our_array, ))
    # this will process: single value
    our_process2 = multiprocessing.Process(target=get_single_value, args=(single_value,))

    our_process1.start()
    our_process1.join()

    our_process2.start()
    our_process2.join()

    print('\n')
    time.sleep(0.25)

    print('Our result list outside the process: ', str(result[:]), '\nAnd our single value out side process is: ',
          str(single_value.value))

