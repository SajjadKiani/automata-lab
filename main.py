from dfa import DFA
from nfa import NFA
from dpda import DPDA
import json

if __name__ == '__main__':

    testcase = {}
    # open testcase.json
    with open('testcase.json', 'r') as f:
        testcases = json.load(f)

    dfa1 = DFA(testcases[0]['states'], testcases[0]['input_symbols'], testcases[0]['transitions'], testcases[0]['initial_state'], testcases[0]['final_states'])
    dfa2 = DFA(testcases[1]['states'], testcases[1]['input_symbols'], testcases[1]['transitions'], testcases[1]['initial_state'], testcases[1]['final_states'])

    print ('dfa1 accept 101111: ', dfa1.accept_string('101111'))

    print ('print union dfa1 and dfa2: ')
    print (dfa1.union(dfa2))

    print ('print intersection dfa1 and dfa2: ')
    print (dfa1.intersection(dfa2))

    print ('print complement dfa1: ')
    print (dfa1.complement())

    print ('print difference dfa1 and dfa2: ')
    print (dfa1.difference(dfa2))

    print ('print is_empty dfa1: ')
    print (dfa1.is_empty())

    print ('print is subset dfa1 and dfa2: ')
    print (dfa1.subset(dfa2))

    print ('print separate dfa1 and dfa2: ')
    print (dfa1.separate(dfa2))

    print ('print dfa is finite: ')
    print (dfa1.is_finite())

    print ('print shortest string dfa1: ')
    print (dfa1.shortest_string())

    print ('print longest string dfa1: ')
    print (dfa1.longest_string())


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
    print ('print minimize dfa: ')
    print(test_dfa.minimize())

    nfa = NFA(testcases[2]['states'], testcases[2]['input_symbols'], testcases[2]['transitions'], testcases[2]['initial_state'], testcases[2]['final_states'])
    print ('print nfa: ')
    print(nfa.eliminate_nondeterminism())

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
    print ('print dpda: ')
    print(dpda.accept_string("[[[[]][]]]"))

    answer = DFA.regex_to_dfa('((aa+b)∗(aba)∗bab)∗')
    print ('print regex "((aa+b)∗(aba)∗bab)∗" to dfa: ')
    print (NFA (answer['states'], answer['input_symbols'], answer['transitions'], answer['initial_state'], answer['final_state']))

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
    print ('print dfa to regex: ')
    print (DFA.dfa_to_regex(test_dfa))

