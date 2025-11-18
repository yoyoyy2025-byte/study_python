# 1번문제

#second = "Python is fun."

#if "Python" in second:
#    print(f"Welcome! {second}")


# 2번문제
#first = 5

#while first > 0 :
#    print(f"while 값 : "+str(first))
#    if first == 2 :
#        print ("special")
#        break
#    first = first - 1
    
#print("while 종료")   

#3번문제

kor = [70 ,80 ,90 ,40 ,50]                    
eng = [90 ,80 ,70 ,70 ,60]
sum1, sum2, sum3, sum4 = 0, 0, 0, 0 

for score in kor + eng:
    print(score, end=' ')
    sum1 = score + sum1
print('\ntotal_scores :', sum1)
