'''
#test1
import os
import pickle

goal_set = {'train': [{'consult_id': 1,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                          'Pain or soreness of breast': True}}},
                        {'consult_id': 2,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {}}}],

            'test': [{'consult_id': 3,
                      'disease_tag': 'Dengue fever',
                      'group_id': 1,
                      'goal': {'request_slots': {'disease': 'UNK'},
                               'explicit_inform_slots': {'Joint stiffness or tightness': True},
                               'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                         'Pain or soreness of breast': True}}},
                     {'consult_id': 4,
                      'disease_tag': 'Dengue fever',
                      'group_id': 1,
                      'goal': {'request_slots': {'disease': 'UNK'},
                               'explicit_inform_slots': {'Joint stiffness or tightness': True},
                               'implicit_inform_slots': {}}}
                     ],

            'validate': []}

train_list = goal_set['train']
counter = 0
for i in range(len(train_list)):
    #print(train_list[i]['goal']['implicit_inform_slots'])
    if len(train_list[i]['goal']['implicit_inform_slots']) == 0:
        counter = counter+1
        del train_list[i]
print(counter)
print(train_list)
print(goal_set['train'])
#del consult
#print train_list
#goal_set = train_list
print(goal_set['test'])
'''

#test2
import os
import pickle

goal_set = {'train': [{'consult_id': 1,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {}}},
                      {'consult_id': 2,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                          'Pain or soreness of breast': True}}},
                      {'consult_id': 3,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                          'Pain or soreness of breast': True}}},
                      {'consult_id': 1,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {}}}
                      ],

            'test': [{'consult_id': 3,
                      'disease_tag': 'Dengue fever',
                      'group_id': 1,
                      'goal': {'request_slots': {'disease': 'UNK'},
                               'explicit_inform_slots': {'Joint stiffness or tightness': True},
                               'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                         'Pain or soreness of breast': True}}},
                     {'consult_id': 4,
                      'disease_tag': 'Dengue fever',
                      'group_id': 1,
                      'goal': {'request_slots': {'disease': 'UNK'},
                               'explicit_inform_slots': {'Joint stiffness or tightness': True},
                               'implicit_inform_slots': {}}}
                     ],

            'validate': []}
'''
train_list = goal_set['train']
counter = 0
print(len(train_list))
print(train_list)
for i in reversed(range(len(train_list))):
    # print(train_list[i]['goal']['implicit_inform_slots'])
    if len(train_list[i]['goal']['implicit_inform_slots']) == 0:
        counter = counter + 1
        del train_list[i]
print(counter)
print(len(train_list))
print(train_list)

# del consult?
# print train_list?
# goal_set = train_list?
'''

# import os
import pickle

counter1 = 0
counter2 = 0
goal_set = pickle.load(open('goal_set.p', 'rb'))
train_set = goal_set['train']
test_set = goal_set['test']
print('train set size : ', len(train_set))
print('test set size: ', len(test_set))

for i in reversed(range(len(train_set))):
    if len(train_set[i]['goal']['implicit_inform_slots']) == 0:
        counter1 = counter1 + 1
        # print(train_set[i])
        del train_set[i]
for j in reversed(range(len(test_set))):
    if len(test_set[i]['goal']['implicit_inform_slots']) == 0:
        counter2 = counter2 + 1
        del test_set[i]
print('number of consultation with no implicit symptoms in train set = ', counter1)
print('training data length after cleaning', len(train_set))
print('number of consultation with no implicit symptoms in test set = ', counter2)
print('testing data length after cleaning', len(test_set))

goal_set_new = {'train': [], 'test': [], 'validate': []}
goal_set_new['train'] = train_set
goal_set_new['test'] = test_set
print('new training set length', len(goal_set_new['train']))
pickle.dump(goal_set_new, open("goal_set2.p", "wb"))



'''
for i in range(len(test_set)):
    if len(test_set[i]['goal']['implicit_inform_slots']) == 0:
        counter2 = counter2 + 1
print('number of consultation with no implicit symptoms in test_set = ', counter2)
'''
