import jax
import gym
import gymnax

num_episodes, num_steps, tolerance = 10, 100, 1e-04


def test_step(env_name):
    """Test a step transition for the env."""
    rng = jax.random.PRNGKey(0)
    env_jax, env_params = gymnax.make("BernoulliBandit-misc")

    # Loop over test episodes
    for ep in range(num_episodes):
        obs, state = env_jax.reset(rng_input, env_params)
        # Loop over test episode steps
        for s in range(num_steps):
            action = env_jax.action_space.sample(rng_input)
            break


def test_reset(env_name):
    """Test reset obs/state is in space of OpenAI version."""
    # env_gym = gym.make(env_name)
    rng = jax.random.PRNGKey(0)
    env_jax, env_params = gymnax.make(env_name)
    for ep in range(num_episodes):
        rng, rng_input = jax.random.split(rng)
        obs, state = env_jax.reset(rng_input, env_params)
        # Check state and observation space
        env_jax.state_space(env_params).contains(state)
        env_jax.observation_space(env_params).contains(obs)
