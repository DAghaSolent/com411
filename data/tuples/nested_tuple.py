def steps():
    likelihoods = [("step 1",50),("step 2",38),("step 3",27),("step 4",99),("step 5", 4)]
    return likelihoods

def run():
    step_testing = steps()
    good_steps = []
    bad_steps = []

    for sets in step_testing:
        if sets[1] > 50:
            bad_steps.append(sets)
        else:
            good_steps.append(sets)

    print(f"Good Steps:{good_steps},\nBad steps:{bad_steps}")

if __name__ =="__main__":
    run()

