from dfa import DFA

if __name__ == '__main__':
    dfa = DFA (
        states=['q0', 'q1', 'q2'],
        input_symbols=['0', '1'],
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q1'}
        },
        initial_state='q0',
        final_states=['q1']
    )

    new_dfa = DFA (
        states=['q0', 'q1', 'q2'],
        input_symbols=['0', '1'],
        transitions={
            'q0': {'0': 'q0', '1': 'q1'},
            'q1': {'0': 'q0', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q1'}
        },
        initial_state='q0',
        final_states=['q1']
    )

    # dfa.accept_language('101111')
    # print (dfa.union(new_dfa))
    # print (dfa.is_empty())
    
    test_dfa = DFA(
        states=['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9'],
        input_symbols=[0,1],
        transitions={
            'q0': {'0': 'q1', '1': 'q9'},
            'q1': {'0': 'q8', '1': 'q2'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q2', '1': 'q4'},
            'q4': {'0': 'q5', '1': 'q8'},
            'q5': {'0': 'q4', '1': 'q5'},
            'q6': {'0': 'q7', '1': 'q5'},
            'q7': {'0': 'q6', '1': 'q5'},
            'q8': {'0': 'q1', '1': 'q3'},
            'q9': {'0': 'q7', '1': 'q8'}
        },
        initial_state='q0',
        final_states=['q3','q4','q8','q9']
    )
    print(test_dfa.minimize())
