with open('input.txt') as puzzleInput:
    stones = {num:1 for num in puzzleInput.readline().split(' ')}
    
blinks = 75
for blink in range(blinks):
    new_stones = {}
    for num, quant in stones.items():
        if num == '0': #do 0->1
            new_stones['1'] = new_stones.get('1',0) + quant
            
        elif len(num)%2 == 0: #deal with even length numbers
            left = num[:len(num)//2]
            right = str(int(num[len(num)//2:]))
            new_stones[left] = new_stones.get(left,0) + quant
            new_stones[right] = new_stones.get(right,0) + quant
            
        else: #multiply by 2024
            new = str(int(num)*2024)
            new_stones[new] = new_stones.get(new,0) + quant
    #redirect stones to point to new_stones
    stones = new_stones
    
print(sum(stones.values()))
    
