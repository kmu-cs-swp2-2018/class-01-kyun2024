import calcFunctions

numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
]

constantDict = {
    constantList[0]:'3.141592',
    constantList[1]:'3E+8',
    constantList[2]:'340',
    constantList[3]:'1.5E+8'
}

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]

functionDict = {
    functionList[0]:calcFunctions.factorial,
    functionList[1]:calcFunctions.decToBin,
    functionList[2]:calcFunctions.binToDec,
    functionList[3]:calcFunctions.decToRoman
}