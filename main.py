from dfa import DFA
from nfa import NFA
from dpda import DPDA
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
    
    # test_dfa = DFA(
    #     states=['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9'],
    #     input_symbols=[0,1],
    #     transitions={
    #         'q0': {'0': 'q1', '1': 'q9'},
    #         'q1': {'0': 'q8', '1': 'q2'},
    #         'q2': {'0': 'q3', '1': 'q2'},
    #         'q3': {'0': 'q2', '1': 'q4'},
    #         'q4': {'0': 'q5', '1': 'q8'},
    #         'q5': {'0': 'q4', '1': 'q5'},
    #         'q6': {'0': 'q7', '1': 'q5'},
    #         'q7': {'0': 'q6', '1': 'q5'},
    #         'q8': {'0': 'q1', '1': 'q3'},
    #         'q9': {'0': 'q7', '1': 'q8'}
    #     },
    #     initial_state='q0',
    #     final_states=['q3','q4','q8','q9']
    # )
    # print(test_dfa.minimize())

    # print (dfa.is_empty())
    # print(test_dfa.minimize())
    test_nfa = NFA(
        states=['q0','q1', 'q2', 'q3','q4'],
        input_symbols=['a', 'b'],
        transitions={
            'q0': {'a':['q1','q2'],'b':['q4']},
            'q1': {'a': ['q0']},
            'q2': {'a': ['q3']},
            'q3': {'b': ['q0']},
            'q4': {},
            
        },
        initial_state='q0',
        final_states=['q4']
    )
    # print(test_nfa.eliminate_nondeterminism())

    dpda = DPDA(
        states={'q0', 'q1'},
        input_symbols={'[', ']'},
        stack_symbols = {'[',']','Z0'},
        initial_stack_symbol = 'Z0',
        transitions={
            'q0': {'[':{'Z0': ['q1',['[','Z0']]}},
            'q1': {'[':{'[': ['q1',['[','[']]},']':{'[': ['q1',[]]},'':{'Z0':['q0',['Z0']]}}
        },
        initial_state='q0',
        final_states={'q0'}
    )
    # print(dpda.accept_string("[[[[]][]]]"))

    # answer = DFA.regex_to_dfa('b*')
    # print (NFA (answer['states'], answer['input_symbols'], answer['transitions'], answer['initial_state'], answer['final_state']))

    # Convert the DFA to a Regular Expression
    test_dfa = DFA(
        states=['1', '2', '3'],
        input_symbols=['a', 'b'],
        transitions={
            '1': {'a': '1', 'b': '2'},
            '2': {'a': '1', 'b': '3'},
            '3': {'a': '1', 'b': '2'}
        },
        initial_state='1',
        final_states=['2']
    )
    print (DFA.dfa_to_regex(test_dfa))

