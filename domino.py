# Task: https://py.checkio.org/ru/mission/domino-chain/
# 

def check_chain_found(dom_chain, all_chains):
    for item in all_chains:
        s1 = ''.join(item)
        if s1[::-1] == ''.join(dom_chain):
            return True
    return False

def dominos(dom_list, index, dom_chain, all_chains) -> int:
    cur_list = dom_list
    ok = True
    for item in cur_list:
      if (item not in dom_chain) and (item[::-1] not in dom_chain)  and ((len(dom_chain) == 0) or \
        (item[0] == dom_chain[-1][2]) or (len(dom_chain) == 1 and (item[-1] == dom_chain[0][0] or item[0] == dom_chain[0][0])) or \
        (item[-1] == dom_chain[-1][-1])):
# item (or rotated item) not in chain
# check 1s tile
# 1st tile need to rotate
# current tile need to rotate
        ok = True
        if (len(dom_chain) == 1) and (item[-1] == dom_chain[0][0] or item[0] == dom_chain[0][0]):   # rotate 1st
          dom_chain[0] = dom_chain[0][::-1]
        dom_chain.append(item)  # add tile into chain
        if (len(dom_chain) > 1)  and (item[-1] == dom_chain[-2][-1]):
            dom_chain[-1] = dom_chain[-1][::-1]  # rotate current tile
        if len(cur_list) == len(dom_chain):  # all tiles are used
          if not check_chain_found(dom_chain, all_chains):
            index +=1
            all_chains.append(dom_chain)
          dom_chain = list(dom_chain[:-2])
          return(index, dom_chain, all_chains)
        (index, dom_chain, all_chains) = dominos(cur_list, index, dom_chain, all_chains)
      else:  # no correct chain
        ok = False
    dom_chain = list(dom_chain[:-1])

    if not ok:
      return (index, dom_chain, all_chains)
    return(index, dom_chain, all_chains)

def domino_chain(tiles: str) -> int:
  # your code here
  dom_list = list(tiles.split(", "))
  x = dominos(dom_list, 0, [], [])
  print(x[0])
  return x[0]




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert domino_chain("0-2, 0-5, 1-5, 1-3, 5-5") == 1 # N1
#    assert domino_chain("0-1, 1-2, 5-6, 1-4, 0-6, 2-5, 1-6, 0-5, 3-6, 0-3, 1-1") == 88 # extra 4
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4") == 6 # N3

#    assert domino_chain("0-0, 4-6, 5-6, 1-4, 0-6, 0-5, 1-6, 0-4, 2-2, 0-3, 3-4") == 0 # test

    assert domino_chain("0-5, 1-5, 2-5, 3-5, 4-5, 3-4") == 0
    
    
    
    assert domino_chain("1-2, 2-2, 2-3, 3-3, 3-1") == 5
    assert domino_chain("1-5, 2-5, 3-5, 4-5, 3-4") == 2 #
    assert domino_chain("0-1, 0-2, 1-3, 1-2, 3-4, 2-4, 3-0, 0-4") == 0
    assert domino_chain("1-4, 3-4, 0-4, 0-5, 4-5, 2-4, 2-5") == 0
    assert domino_chain("1-4, 1-5, 0-2, 1-6, 4-6, 4-5, 5-6") == 0
    assert domino_chain("1-2, 2-3, 2-4, 3-4, 2-5, 2-6, 5-6") == 8
    assert domino_chain("1-2, 2-3, 3-1, 4-5, 5-6, 6-4") == 0
    assert domino_chain("1-2, 1-4, 1-5, 1-6, 1-1, 2-5, 4-6") == 28
    print("Basic tests passed.")
