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

    dfa.accept_language('101111')
    print (dfa.union(new_dfa))

    print (dfa.is_empty())