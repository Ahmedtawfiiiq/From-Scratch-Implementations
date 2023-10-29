import numpy as np

sbox = np.array([
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ])

rcon = np.array([
    [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    ])

def toState(plainText):
    # plaintext block size is 128 bits
    # 128 bits = 16 bytes -> 4x4 matrix
    state = [[0 for i in range(4)] for j in range(4)]
    shift = 128 # size of plaintext in bits
    for i in range(4):
        for j in range(4):
            shift -= 8
            # get the most significant byte
            byte = plainText >> shift
            # and it with 0xFF to get the last 8 bits
            byte = byte & 0xFF
            # store the byte in the state (column by column)
            state[j][i] = byte
    return state

def xorState(state, roundKey):
    for i in range(4):
        for j in range(4):
            state[i][j] ^= roundKey[i][j]
    return state

def subBytes(state):
    # s-box is a 2D array (16x16) -> indexes are from 0 to 15
    for i in range(4):
        for j in range(4):
            state[i][j] = sbox[state[i][j] >> 4][state[i][j] & 0xF]
    return state

def shiftRows(state):
    # rotational shift of rows
    # row 0 -> no shift
    # row 1 -> rotate 1 byte to the left
    # row 2 -> rotate 2 bytes to the left
    # row 3 -> rotate 3 bytes to the left
    for i in range(4):
        # append the first i elements to the end of the row
        state[i] = state[i][i:] + state[i][:i]
    return state

def gf_2_8_multplication(f, g):
    m = 0b00011011
    # x * f(x) = f(x) << 1 if f(x) < 128 else (f(x) << 1) ^ m
    # from x to x^7 assume ord(f(x)) < 8 and ord(g(x)) < 8
    # create array of 8 bytes
    results = [0] * 8
    for i in range(8):
        if i == 0:
            results[i] = f & 0xff
        else:
            results[i] = (results[i - 1] << 1) & 0xff
            if results[i - 1] >= 128:
                results[i] ^= m
            results[i] &= 0xff
    # read g(x) from right to left
    # if g(x) == 1 then xor with f(x)
    result = 0
    for i in range(8):
        if g & 1:
            result ^= results[i]
        g >>= 1
    # return only last 8 bits
    return result


def columnMultiplication(stateColumn):
    # 4x4 matrix
    predefined = np.array([
    [0x02, 0x03, 0x01, 0x01],
    [0x01, 0x02, 0x03, 0x01],
    [0x01, 0x01, 0x02, 0x03],
    [0x03, 0x01, 0x01, 0x02]
    ])
    # 4x1 column
    result = np.array([[0] for i in range(4)])
    for i in range(4):
        for j in range(4):
            # xor performs addition in GF(2^8)
            result[i][0] ^= gf_2_8_multplication(predefined[i][j], stateColumn[j][0])
    return result


def mixColumns(state):
    # mulitplication in GF(2^8)
    # muliply predefined matrix with each column of the state
    for i in range(4):
        column = [[state[j][i]] for j in range(4)]
        mixColumn = columnMultiplication(column)
        for j in range(4):
            state[j][i] = mixColumn[j][0]
    return state

def rotWord(key_word):
    # key word is 4x1 column
    # append the first element to the end
    key_word = key_word[1:] + key_word[:1]
    return key_word

def subWord(key_word):
    # key word is 4x1 column
    for i in range(4):
        key_word[i][0] = sbox[key_word[i][0] >> 4][key_word[i][0] & 0xF]
    return key_word

def xorKey1(prev_word, curr_word, rcon):
    for i in range(4):
        prev_word[i][0] ^= curr_word[i][0]
        prev_word[i][0] ^= rcon[i][0]
    return prev_word

def xorKey2(prev_word, curr_word):
    for i in range(4):
        prev_word[i][0] ^= curr_word[i][0]
    return prev_word

def keySchedule(cipher_key):
    keys = [] # 4x4x11 matrix
    # first key is the cipher key
    for i in range(4):
        column = [cipher_key[j][i] for j in range(4)]
        keys.append(column)
    # generate 10 more keys (key for each round)
    k = 3
    for i in range(10):
        column = [[keys[k][j]] for j in range(4)]
        column = rotWord(column)
        column = subWord(column)
        prev_column = [[keys[k-3][j]] for j in range(4)]
        column = xorKey1(prev_column, column, rcon[:, [i]])
        new_column = [column[j][0] for j in range(4)]
        keys.append(new_column)
        for j in range(3):
            prev_column = [[keys[k-3+1+j][l]] for l in range(4)]
            column = xorKey2(prev_column, column)
            new_column = [column[l][0] for l in range(4)]
            keys.append(new_column)
        k += 4
    return keys

def initialRound(state, roundKey):
    state = xorState(state, roundKey[:, :4])
    return state

def round(state, roundKey, mix=True):
    state = subBytes(state)
    state = shiftRows(state)
    if mix:
        state = mixColumns(state)
    state = xorState(state, roundKey)
    return state

def intermediateRounds(state, roundKeys, n):
    for i in range(1, n+1):
        state = round(state, roundKeys[:, 4*i:4*(i+1)])
    return state

def finalRound(state, roundKey):
    return round(state, roundKey[:, 40:], False)

def getState(state):
    # row by row
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(hex(state[i][j]), end=" ")
        print()


plaintext = 0x3243F6A8885A308D313198A2E0370734
key = 0x2B7E151628AED2A6ABF7158809CF4F3C

cipher_key = toState(key)
keys = np.array(keySchedule(cipher_key)).T

state = toState(plaintext)
state = initialRound(state, keys)
state = intermediateRounds(state, keys, 9)
state = finalRound(state, keys)
getState(state)
