import gym;

env = gym.make('MountainCar-v0');

env.reset();

for _ in range(1000):
    env.render();
    action = env.action_space.sample();
    observation, reward, done, info = env.step(action);

    if done:
        observation = env.reset();

env.close();
