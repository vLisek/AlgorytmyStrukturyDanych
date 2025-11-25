def edit_distance(s1, s2):
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)

    if s1[0] == s2[0]:
        return edit_distance(s1[1:], s2[1:])
    else:
        insert = edit_distance(s1, s2[1:])     # wstawienie
        delete = edit_distance(s1[1:], s2)     # usunięcie
        replace = edit_distance(s1[1:], s2[1:])  # zamiana
        return 1 + min(insert, delete, replace)


s1 = "kitten"
s2 = "sitting"
print("Minimalna liczba operacji:", edit_distance(s1, s2))
