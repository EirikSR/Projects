def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for i in states:
        print(emit_p[i][obs[0]])
        V[0][i] = start_p[i] * emit_p[i][obs[0]]
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for y in states:
            (prob, state) = max(
                (V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states
            )
            V[t][y] = prob
        for i in dptable(V):
            print(i)
        opt = []
        for j in V:
            for x, y in j.items():
                if j[x] == max(j.values()):
                    opt.append(x)
    # the highest probability
    h = max(V[-1].values())
    print(
        "The steps of states are "
        + " ".join(opt)
        + " with highest probability of %s" % h
    )
    # it prints a table of steps from dictionary


def dptable(V):
    yield " ".join(("%10d" % i) for i in range(len(V)))
    for y in V[0]:
        yield "%.7s: " % y + " ".join("%.7s" % ("%f" % v[y]) for v in V)


states = {"B-PER", "<s>", "I-PER", "O"}
observations = ("Prinsesse", "MÃ¤rtha", "Louise", "savnet", "neppe", "sin", "Ari")
start_probability = {
    "B-PER": 6.2499750001e-08,
    "<s>": 1.2499900000799993e-07,
    "I-PER": 1.2499900000799993e-07,
    "O": 2.4999960000063997e-08,
}
transition_probability = {
    "O": {
        "O": 0.399999560000704,
        "B-PER": 4.99998000008e-07,
        "I-PER": 0.9999930000559994,
        "<s>": 9.999920000639994e-07,
    },
    "B-PER": {
        "O": 0.399999560000704,
        "B-PER": 4.99998000008e-07,
        "I-PER": 9.999920000639994e-07,
        "<s>": 9.999920000639994e-07,
    },
    "I-PER": {
        "O": 1.9999968000051197e-07,
        "B-PER": 0.499998500006,
        "I-PER": 9.999920000639994e-07,
        "<s>": 9.999920000639994e-07,
    },
    "<s>": {
        "O": 1.9999968000051197e-07,
        "B-PER": 4.99998000008e-07,
        "I-PER": 9.999920000639994e-07,
        "<s>": 9.999920000639994e-07,
    },
}
emission_probability = {
    "O": {
        "": 0.19999988000019198,
        "MÃ¤rtha": 1.9999968000051197e-07,
        "sin": 1.9999968000051197e-07,
        "Prinsesse": 1.9999968000051197e-07,
        "Ari": 1.9999968000051197e-07,
        "Louise": 1.9999968000051197e-07,
        "savnet": 1.9999968000051197e-07,
        "neppe": 1.9999968000051197e-07,
    },
    "<s>": {
        "": 9.999920000639994e-07,
        "MÃ¤rtha": 9.999920000639994e-07,
        "sin": 9.999920000639994e-07,
        "Prinsesse": 0.9999930000559994,
        "Ari": 9.999920000639994e-07,
        "Louise": 9.999920000639994e-07,
        "savnet": 9.999920000639994e-07,
        "neppe": 9.999920000639994e-07,
    },
    "I-PER": {
        "": 9.999920000639994e-07,
        "MÃ¤rtha": 9.999920000639994e-07,
        "sin": 9.999920000639994e-07,
        "Prinsesse": 9.999920000639994e-07,
        "Ari": 9.999920000639994e-07,
        "Louise": 9.999920000639994e-07,
        "savnet": 9.999920000639994e-07,
        "neppe": 9.999920000639994e-07,
    },
    "B-PER": {
        "": 4.99998000008e-07,
        "MÃ¤rtha": 4.99998000008e-07,
        "sin": 4.99998000008e-07,
        "Prinsesse": 4.99998000008e-07,
        "Ari": 4.99998000008e-07,
        "Louise": 4.99998000008e-07,
        "savnet": 4.99998000008e-07,
        "neppe": 4.99998000008e-07,
    },
}


viterbi(
    observations,
    states,
    start_probability,
    transition_probability,
    emission_probability,
)
