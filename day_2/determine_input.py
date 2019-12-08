# part 2
import sys

from restore_gravity_assist import run_program

def find_inputs_for_answer(program, answer):
    # brute force
    noun = 0
    verb = 0
    temp_program = program.copy()
    for i in range(0, 100):
        for j in range(0, 100):
            temp_program[1] = i # noun
            temp_program[2] = j # verb
            if run_program(temp_program)[0] == answer:
                return (temp_program[1], temp_program[2])
            temp_program = program.copy()

def smart_find_inputs_for_answer(program, answer):
    import tensorflow as tf
    # generate a bunch of programs using known noun-verb pairs, and calculate their output  
    programs_to_generate = 100
    program_size = len(program)

    test_programs = tf.random.uniform(
        [programs_to_generate, program_size],
        minval=0,
        maxval=99,
        dtype=tf.dtypes.float32,
        seed=None,
        name=None
    )

    test_nouns = test_programs[:, 1]
    test_verbs = test_programs[:, 2]

    test_answers = [run_program(test_program) for test_program in test_programs]

    # [1, 0, 0, 2, ..] => (0,0) -> 1980123
    # [2, 0, 0, 2, ..] => (0,0) -> 37529
    # [99, 1, 0, 2, ..] => (1,0) -> 77729423

    x = tf.stack([test_nouns, test_verbs], axis = 1),
    y = test_answers

    train_size = math.floor(0.7 * programs_to_generate)
    test_size = programs_to_generate - train_size

    # train 2-layer network
    x_train = tf.convert_to_tensor(
        x[:train_size,:],
        dtype = tf.int32,
        dtype_hint = None,
        name = "x_train"
    )

    y_train = tf.convert_to_tensor(
        y[:train_size],
        dtype = tf.int32,
        dtype_hint = None,
        name = "y_train"
    )


    model = tf.keras.model.Sequential([
        tf.keras.Dense(program_size, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    model.fit(x_train, y_train, epochs=5)
    
    x_test = x[train_size:, :]
    y_test = y[train_size:]

    model.evaluate(x_test,  y_test, verbose=2)


    # predict noun-verb that results in answer
    model.predict(answer)



if __name__ == "__main__":
    INPUT_FILEPATH = sys.argv[1]
    DESIRED_ANSWER = int(sys.argv[2])

    with open(INPUT_FILEPATH, 'r') as input_file:
        program = [int(number) for number in input_file.readline().split(",")]

    print(find_inputs_for_answer(program, DESIRED_ANSWER))