import WOMnew
import pickle


brain = []

with open("data/trained_model.pickle", "rb") as f:
    brain = pickle.load(f)

env = WOMnew.wom_train()

for i_episode in range(20):
   observation = env.reset()
   for t in range(100):                        # For 100 time steps
      #env.render()
      print(observation)
      action = env.get_random_word(observation[-1])
      observation, reward, done, winner = env.step(action)

      if done:                                # Finish the episode if done
        update_model(observation, reward, done, winner)
        break

        
def update_model(observation, reward, done, winner):
    p_word = []
    n_word = []
    if winner:
        