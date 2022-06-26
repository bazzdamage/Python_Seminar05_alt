# 3. Вот вам текст:
text = "Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. " \
       "Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче." \
       "Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее." \
       "И снова вышел, короче, из подъезда. Ясен пень, в магазин." \
       "В общем, лето на дворе, жарко, солнечно, птицы, короче, летают." \
       "Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем." \
       "Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно." \
       "В общем, в магазин мне надо. Что-то явно не так, короче." \
       "«Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму." \
       "Хлеба купил."
bad_phrases = ["короче говоря", "как бы", "ясен пень", "в общем"]
bad_words = ["ну", "короче", "кажется"]
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть.
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.


def text_filter(bad, good, proc_text):
    index = 0
    # Find all occurrences to end of str
    while index < len(proc_text):
        temp = good
        index_l = proc_text.lower().find(bad.lower(), index)
        if index_l == -1:
            return proc_text
        bad_length = len(bad)
        # try to remove commas before bad words if exist
        if proc_text[index_l:index_l + len(bad) + 3].find(',') != -1:
            bad_length += 2
        if proc_text[index_l - 2] == ',':
            index_l -= 2
            bad_length += 2
            temp = ' '

        proc_text = proc_text[:index_l] + temp + proc_text[index_l + bad_length:]
        index = index_l + len(good)
    return proc_text


def filtering(init_text, lst_bad_phrases, lst_bad_words):
    # First filter occasionally repeating symbols
    r = [None]
    for sym in init_text:
        if sym != r[-1] and sym.capitalize() != r[-1]:
            r.append(sym)
    out = ''.join(r[1:])
    print(out)

    # Then filter whole bad phrases, cause them contains words from bad_words too
    for phrase in lst_bad_phrases:
        out = text_filter(phrase, '', out)
    # Finally, filter bad words
    for word in lst_bad_words:
        out = text_filter(word, '', out)

    return out


# I still don't figure it out, how remove Single "э" or other single characters in all cases (other text, for example)
print(filtering(text, bad_phrases, bad_words))
