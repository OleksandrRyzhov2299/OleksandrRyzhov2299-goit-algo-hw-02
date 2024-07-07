from collections import deque

def is_palindrome(s) -> bool:
    
    deq = deque(s.lower().replace(" ", ""))
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            print("Не поліндром")
            return False
    print("поліндром")
    return True    
    
print(is_palindrome("A a "))