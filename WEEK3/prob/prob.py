def Read_File(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


def PROB(seq, num):

    seq = seq.upper()
    pG,pC = num/2, num/2
    pA,pT = (1-num)/2, (1-num)/2
    nA = seq.count('A')
    nT = seq.count('T')
    nG = seq.count('G')
    nC = seq.count('C')
    prob = math.pow(pA,nA)*math.pow(pT,nT)*math.pow(pG,nG)*math.pow(pC,nC)

    return round(math.log(prob,10),3)


def Result(seq,nums):

    arrayB = []
    for num in nums:
        arrayB.append(PROB(seq, num))
   
    return arrayB


if __name__ == '__main__':

    import sys
    import math

    raw_data = Read_File(sys.argv[-1])
    seq = raw_data[0].strip()
    arrayA = map(float, raw_data[1].split(" "))
    print ' '.join(map(str, Result(seq, arrayA))) 
