def what_is_my_sign(day, month):
    # разделям месеците по зодии
    signs = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    # също така тук забелязах доста интересна последователност - за Capricorn за месец Януари началната дата се пада в предходния месец декември, а крайната дата 
    # се пада в текущия месец, после при Aquarius за месец Февруари имаме обратното нещо - началната дата се пада в текущия месец а крайната дата в следващия месец Март
    # от там забелязах, че реално имам крайните дати за всяка зодия по месеци - Capricorn до 20 Януари, Aquarius до 19, Pisces до 20 и т.н.

    # представям карйната дата за всяка зодия като цяло число в масив (индекса се пада според месеца и зодията)
    # Януари = индекс 0 = Capricorn, Февруари = индекс 1 = Aquarius и т.н.
    signPeriods = [20, 19, 20, 20, 21, 21, 22, 22, 23, 23, 22, 21]

    for i in range(0, len(signs)):
        if month == i + 1:
            # получавам карйната дата за текущата зодия
            endDate = signPeriods[i]

            # ако въведения ден е по-голям от крайната дата то тя спада в периода на следващата зодия
            if day > endDate:
                nextSignIndex = i + 1

                # ако имаме 28 Декември примерно и трябва да вземем Козирог от месец Януари
                if nextSignIndex > len(signs) - 1:
                    nextSignIndex = 0

                return signs[i + 1]
            else:
                return signs[i]

print(what_is_my_sign(5, 8))
print(what_is_my_sign(29, 1))
print(what_is_my_sign(30, 6))
print(what_is_my_sign(31, 5))
print(what_is_my_sign(2, 2))
print(what_is_my_sign(8, 5))
print(what_is_my_sign(9, 1))
