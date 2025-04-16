sweetT = {"R":[12,18,25],"T":[15,20,30],"M":[10,15,20]}
sweetB = {"H":5,"O":3,"J":2}
bobaK,bobaG = map(str,input().split(" "))
bobaG = int(bobaG)
teaK,teaS,teaV = map(str,input().split(" "))
teaS = int(teaS)
teaV = int(teaV)
sweetnessT = sweetT[teaK][teaS-1]
sweetnessB = sweetB[bobaK]
print(teaV*sweetnessT + bobaG*sweetnessB)
