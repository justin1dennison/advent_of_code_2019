from itertools import product

def step(state, noun, verb):
    state[1] = noun
    state[2] = verb
    chunks = (state[i : i + 4] for i in range(0, len(state) - 1, 4))
    for chunk in chunks:
        opcode, x, y, out = chunk
        if opcode == 99:
            break
        elif opcode == 1:
            result = state[x] + state[y]
            state[out] = result
        elif opcode == 2:
            result = state[x] * state[y]
            state[out] = result
        else:
            raise ValueError('Unknown Opcode')
    return state

def main():
    with open("./input.txt") as f:
        original_state = [int(el) for el in f.read().split(",")]
    nouns = range(100)
    verbs = range(100)
    for noun, verb in product(nouns, verbs):
        goal, *_ = step(original_state[:], noun, verb)
        if goal == 19690720:
            print(f'Result: {100 * noun + verb}')
            break

if __name__ == "__main__":
    main()
