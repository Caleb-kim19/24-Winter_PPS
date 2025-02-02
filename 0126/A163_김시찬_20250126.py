def solution(today, terms, privacies):
    def date_to_days(date_str):
        year, month, day = map(int, date_str.split('.'))
        return year * 12 * 28 + month * 28 + day

    today_days = date_to_days(today)

    term_dict = {}
    for term in terms:
        t, duration = term.split()
        term_dict[t] = int(duration)

    answer = []
    for i, privacy in enumerate(privacies, start=1):
        date_str, term_type = privacy.split()
        collection_days = date_to_days(date_str)
        expiry = collection_days + term_dict[term_type] * 28 - 1
        if expiry < today_days:
            answer.append(i)
    return answer