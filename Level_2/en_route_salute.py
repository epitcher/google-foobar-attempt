def solution(s):

    hallway = s.replace('-', '')
    print(hallway)

    collisions = 0
    for i in range(len(hallway)):
        current_char = hallway[i]

        if current_char == '>':
            for a in range(i, len(hallway)):
                if hallway[a] == '<': collisions += 1
    
    salutes = collisions * 2
    return str(salutes)

print(solution('--<->>-<><--'))