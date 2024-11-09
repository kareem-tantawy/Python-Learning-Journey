# ------------------- #
# -- Loop => While -- #
# ------------------- #

# ------------------------------------------ #
#          while condition_is_true         
# Code Will Run Until Condition Become False
# ------------------------------------------ #


num = 1

while num < 10:
    print(f"{num}")
    num += 1
    
else :
    print("Loop is done!")   # True become False
    
    

print('='*40)

    
    
while False:         # The while loop terminated because the condition is False 
    print("Hi")
    

friends = ["Yousef", "Ahmed", "Hany", "Mohamed", "Osama", "Safwan", "Abdulla", "Omar"]

count = len(friends)
zFill = 1
while count == 0:
    count/10
    zFill += 1
i = 0
while i < len(friends):
    print(f"{i+1}- {friends[i]}")
    i += 1
    

print('='*40)


chars = ['a', 'b','c','d','e','f','g','h','j','k','l','m','n','o','p','q']
count = len(chars)
zFill = 0
while int(count) > 0:
    count /= 10
    zFill += 1
j = 0
while j < len(chars):
    print(f"{str(j+1).zfill(zFill)}- {chars[j]}")
    j += 1