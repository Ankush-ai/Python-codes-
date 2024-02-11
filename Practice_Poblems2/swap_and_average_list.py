def sum_and_adverage(numbers):
    total_sum=sum(numbers)
    avg = total_sum/len(numbers)

    return total_sum,avg

numbers=[1,2,3,4,5,6,7,8,9,10]
total_sum,avg=sum_and_adverage(numbers)
print("The Total sum is :", total_sum)
print("The averge is :,", avg)