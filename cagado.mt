bloco main 0

    0 a -- X d 1

    1 a -- a d 1
    1 X -- X d 1
    1 b -- X e 2

    2 a -- X d *
    2 X -- X e 2
    2 _ -- _ i pare

    0 * -- * i 3
    1 * -- * i 3
    2 * -- * i 3

    3 erro pare

fim

bloco erro 0

    0 * -- E d 1
    1 * -- R d 2
    2 * -- R d 3
    3 * -- O d retorne

fim
