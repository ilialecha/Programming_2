//count num of rep of each elem with dictionaries.

FREQUENCY_DISTRIBUTION(L)
    let D be the empty dicctionary
    for all x in L do
        if x in D then
            D[x] <- D[x] +1
        else
            D[x] <- 1

    for all x in D do
        output (x, D[x])