def escada2(N,M,matriz):
    direita = M - 1

    for j in range(M):
        if matriz[0][j] !=0: 
            direita = j - 1
            break

    for i in range(1,N):
        for j in range(direita+1):
            if matriz[i][j] != 0:
                return 'N'

        if direita == M - 1:
            continue
        
        direita = direita + 1
        if matriz[i][direita] != 0:
            return 'N'
        zero = True
        while (zero and direita < M-1):
            direita = direita + 1
            if matriz[i][direita] != 0:
                zero = False
        direita = direita -1
    return 'S'  
