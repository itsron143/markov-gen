import random
import os


def ngram_gen(txt, n_gram_order):
    n_grams = {}
    for i in range(len(txt) - n_gram_order + 1):
        gram = txt[i:i+n_gram_order]
        if gram not in n_grams:
            n_grams[gram] = []
        next_char_index = i+n_gram_order
        if next_char_index < len(txt):
            n_grams[gram].append(txt[next_char_index])
    return n_grams


def ngram_markovIt(txt, n_gram_order, size):
    n_grams = ngram_gen(txt, n_gram_order)
    currentGram = txt[0:n_gram_order]
    result = currentGram
    for _ in range(size):
        possibilities = n_grams[currentGram]
        if len(possibilities) == 0:
            break
        next_char = random.choice(possibilities)
        result += next_char
        currentGram = result[len(result)-n_gram_order:len(result)]
    return result


def word_gram_gen(txt_list):
    word_grams = {}
    for i in range(len(txt_list) - 1):
        if txt_list[i] not in word_grams:
            word_grams[txt_list[i]] = []
        word_grams[txt_list[i]].append(txt_list[i+1])
    word_grams[txt_list[len(txt_list) - 1]] = []
    return word_grams


def word_markovIt(txt_list, size):
    word_grams = word_gram_gen(txt_list)
    currentGram = txt_list[0]
    result = currentGram
    for _ in range(size):
        possibilities = word_grams[currentGram]
        if len(possibilities) == 0:
            break
        next_word = random.choice(possibilities)
        result += " " + next_word
        currentGram = next_word
    return result
