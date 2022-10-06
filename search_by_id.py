'''
goal_set = {'train': [{'consult_id': 1,
                       'disease_tag': 'Dengue fever',
                       'group_id': 1,
                       'goal': {'request_slots': {'disease': 'UNK'},
                                'explicit_inform_slots': {'Joint stiffness or tightness': True},
                                'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                          'Pain or soreness of breast': True}}}],

            'test': [{'consult_id': 2,
                      'disease_tag': 'Dengue fever',
                      'group_id': 1,
                      'goal': {'request_slots': {'disease': 'UNK'},
                               'explicit_inform_slots': {'Joint stiffness or tightness': True},
                               'implicit_inform_slots': {'Sore throat': True, 'Fever': True,
                                                         'Pain or soreness of breast': True}}}],

            'validate': []}

consult_id = 1

train_list = goal_set['train']
# print(train_list)
for i in range(len(train_list)):
    # print(train_list[i])
    # print(train_list[i]['consult_id'])
    if train_list[i]['consult_id'] == consult_id:
        print('Id: ',train_list[i]['consult_id'])
        print('disease: ',train_list[i]['disease_tag'])
        print('group_id: ', train_list[i]['group_id'])
        print('goal: ',train_list[i]['goal'])#+'\n'+ train_list[i]['disease_tag']+'\n'+train_list[i]['group_id']+'\n'+train_list[i]['goal'])
    else:
        print('cant find consult_id !!!')
'''

import os
import pickle

label = 'label1'
#path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses/synthetic_dataset/'+ label
path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses/synthetic_dataset/'


os.chdir(path)
goal_set = pickle.load(open('goal_set.p', 'rb'))

consult_id = 12577

train_list = goal_set['train']
#print(train_list)
for i in range(len(train_list)):
    # print(train_list[i])
    # print(train_list[i]['consult_id'])
    if train_list[i]['consult_id'] == consult_id:
        print('Id: ',train_list[i]['consult_id'])
        print('disease: ',train_list[i]['disease_tag'])
        print('group_id: ', train_list[i]['group_id'])
        print('goal: ',train_list[i]['goal'])#+'\n'+ train_list[i]['disease_tag']+'\n'+train_list[i]['group_id']+'\n'+train_list[i]['goal'])
print('done')
