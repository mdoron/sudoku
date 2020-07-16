import random

board1 = [
    "608904007",
    "030087506",
    "207065000",
    "003009400",
    "740602080",
    "006840700",
    "084506071",
    "975420600",
    "100308000"
]

board2 = [
    "070053020",
    "008020000",
    "350900000",
    "607000300",
    "030105000",
    "905000106",
    "000008037",
    "000030200",
    "080640090"
]


board3 = [
    '290100005',
    '070050000',
    '080000600',
    '400032000',
    '005807200',
    '000960001',
    '009000010',
    '000020050',
    '600001072',
]

board4 = [
    '090000700',
    '000010008',
    '020609000',
    '500060320',
    '300902005',
    '062030004',
    '000307050',
    '900040000',
    '006000040',
]

board5 = [
    "090000700",
    "000010008",
    "020609000",
    "500060320",
    "300902005",
    "062030004",
    "000307050",
    "900040000",
    "006000040"
]

board6 = [
    "400800700",
    "003004008",
    "800600400",
    "009001007",
    "300900600",
    "002005004",
    "200300800",
    "008006003",
    "700500100"
]

board7 = [
    "000000700",
    "000010008",
    "020609000",
    "500060320",
    "300900005",
    "062030004",
    "000307050",
    "000040000",
    "006000040"
]

solved = [
    "658934127",
    "431287596",
    "297165843",
    "813759462",
    "749612385",
    "526843719",
    "384596271",
    "975421638",
    "162378954",
]

for k in range(81):
    i = random.randint(0, 8)
    j = random.randint(0, 8)
    while solved[i][j] == "0":
        i = random.randint(0, 8)
        j = random.randint(0, 8)

    solved[i] = solved[i][:j] + "0" + solved[i][j+1:]


all_boards = [solved, board1, board2, board3, board4, board5, board6, board7]
