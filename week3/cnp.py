def cnp_valid(cnp):
    if not isinstance(cnp, str) or len(cnp) != 13 or not cnp.isdigit():
        return False

    sex = int(cnp[0])
    an = int(cnp[1:3])
    luna = int(cnp[3:5])
    zi = int(cnp[5:7])
    judet = int(cnp[7:9])
    NNN = int(cnp[9:12])
    control = int(cnp[12])

    if sex not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    if sex in [1, 3, 5] and an > 99:
        return False

    if sex in [2, 4, 6] and an > 99:
        an += 100

    if sex in [7, 8, 9] and an < 20:
        an += 100


    if NNN == 0:
        return False

    if judet == 0 and NNN < 500:
        return False

    if NNN >= 500:
        NNN -= 500

    if judet not in range(1, 47) and judet not in range(51, 53):
        return False

    if judet in range(41, 47):
        if NNN > 999:
            return False
    elif judet in range(51, 53):
        if NNN > 99:
            return False
    else:
        if NNN > 999:
            return False

    numar_de_inmultit = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    check_sum = sum([int(cnp[i]) * numar_de_inmultit[i] for i in range(12)]) % 11
    if check_sum == 10:
        check_sum = 1

    return check_sum == control and luna in range(1, 13) and zi in range(1, 32)

test_cnp_1 = "5010814510046"

print(cnp_valid(test_cnp_1))