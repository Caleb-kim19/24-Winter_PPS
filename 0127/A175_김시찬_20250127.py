def solution(babbling):
    answer = 0
    valid_syllables = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for syllable in valid_syllables:
            if syllable * 2 not in word:
                word = word.replace(syllable, " ")
        if word.strip() == "":
            answer += 1
    return answer