# Test case 1
print("=== Challenge 1: Collatz Conjecture ===")

current_number = int(input())
sequence = [current_number]
step_count = 0

while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = 3 * current_number + 1
    sequence.append(current_number)
    step_count += 1

print(f"Enter starting number: Sequence:", end=" ")
for num in sequence:
    print(num, end=" ")
print()
print("Steps:", step_count)

print()

#test case 2
num = int(input())
divisor = num - 1
print("=== Challenge 2: Prime Number Checker ===")
print(f"Enter a number: Testing divisors from 2 to {divisor}...")

prime = True
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime (divisible by {i})")
        prime = False
        break

if prime:
    print(f"{num} is prime!")
print()
