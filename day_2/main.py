def main():
    with open("./input.txt") as f:
        state = [int(el) for el in f.read().split(",")]
    chunks = [state[i : i + 4] for i in range(0, len(state) - 1, 4)]
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
            raise ValueError("Unknown Opcode")
    print(f"State: {state}")


if __name__ == "__main__":
    main()
