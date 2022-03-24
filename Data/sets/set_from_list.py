def observed():
  observations = []
  for i in range(7):
    observations.append(input("Please enter an observation: \n"))
  return observations

def run():
  print("Counting observations...")
  obs = observed()
  set_observations = set(obs)
  set_touples_obs = set()
  for observation in set_observations:
    count = 0
    for i in obs:
      if i == observation:
        count += 1
    set_touples_obs.add((observation, count))
  
  for tuplex in set_touples_obs:
    print(f"{tuplex[0]} has been observed {tuplex[1]}")
    
run()