
import brain
import WOMpro as wom

env = wom.wom_train()
episodes = 100000

manager = brain.manager()


for i in range(episodes):
    observation = env.reset()
    done = False
    while not done:
        action = env.get_random_word(observation[-1], observation)
        observation, reward, done, info = env.step(action)
        #print(observation, reward, done, info, env.score)
    win_words, lose_words = brain.transform(observation, brain.who_win(reward))
    manager.study(win_words, lose_words, reward)
    manager.study_start(observation[0], reward)
    print(f"episode{i} end")

manager.save_model()