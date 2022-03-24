def steps():
  likelihoods = [("Step 1", 50), ("Step 2", 38), ("Step 3", 27), ("Step 4", 15), ("Step 5", 67)]
  return likelihoods

def run():
  probabilities = steps()
  good_steps = []
  bad_steps = []
  for tuplex in probabilities:
    if tuplex[1] < 50:
      good_steps.append(tuplex)
    else:
      bad_steps.append(tuplex)
  print("Good steps: {}, bad steps: {}".format(len(good_steps),len(bad_steps)))

run()