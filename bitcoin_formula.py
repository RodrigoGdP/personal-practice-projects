total_btc = 0
btc = 0
blocks_halving = 210000
halving = 0
reward = 50
half = 2
total_halving = 32
year1 = 2008
year2 = year1 - 4
for i in range (total_halving + 1):
    btc = (blocks_halving*(reward/(pow(half, halving))))
    total_btc += btc
    halving += 1
    year1 += 4
    year2 += 4
    print(f'{total_btc} total bitcoins, with {btc} btc generated from approximately {str(year2)} to {str(year1)}, at a rate of {btc/blocks_halving} btc per block')
