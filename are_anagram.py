def are_anagrams(s1, s2, s3):
    """
    Funkcja sprawdza czy łańcuchy znaków są swoimi wzajemnymi anagramami
    :param s1: pierwszy łańcuch znaków
    :param s2: drugi łańcuch znaków
    :param s3: trzeci łańcuch znaków
    :return: True jeśli łańcuchy znaków są anagramami, False jeżeli nie są
    """

    # Funkcja sprawdza czy łańcuchy znaków mają równe sobie długości
    if len(s1) != len(s2) or len(s1) != len(s3):
        return False

    # Łańcuchy znaków przekształcone w listy w celu możliwości usunięcia już sprawdzonych symboli
    s2_list = list(s2)
    s3_list = list(s3)

    for char in s1:
        if char not in s2_list or char not in s3_list:
            return False
        else:
            s2_list.remove(char)
            s3_list.remove(char)
    return True
