def calculate_arithmetic(num_a, num_b):
    """
    두 숫자를 입력받아 사칙연산 결과를 반환하는 함수
    """
    addition = num_a + num_b
    subtraction = num_a - num_b
    multiplication = num_a * num_b
    
    if num_b == 0:
        division = "division_error"
    else:
        division = num_a / num_b
        
    return (addition, subtraction, multiplication, division)

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = calculate_arithmetic(a, b)
    print(f"{a}, {b} => {result}")