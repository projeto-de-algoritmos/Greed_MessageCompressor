class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
huffmanObject = {}

def CreateHuffmanObject(node, val=''):
	# huffman code for current node
	newVal = val + str(node.huff)
	

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		CreateHuffmanObject(node.left, newVal)
	if(node.right):
		CreateHuffmanObject(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")
		huffmanObject[node.symbol] = newVal
	return huffmanObject

def huffman():
    test =  "Bylly!"
    symFreqs = {}

    for c in test:
        symFreqs[c] = 0
    for c in test:
        symFreqs[c] = symFreqs[c] + 1
    chars = []
    print(symFreqs)
    # Get keys of object
    for key in symFreqs:
        chars.append(key)
    # frequency of characters
    freq = list(symFreqs.values())

    # list containing unused nodes
    nodes = []

    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        nodes.append(node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    huffmanDict = CreateHuffmanObject(nodes[0])
    for key in symFreqs:
        test = test.replace(key,huffmanDict[key])
    # for key in huffmanDict:
    #     huffmanDict[key] = bitarray(huffmanDict[key])
    huffmanDict["msg"] = test
    # dec = bitarray(test).decode(huffmanDict)
    # print(dec)
    # print(''.join(dec))
    return huffmanDict
