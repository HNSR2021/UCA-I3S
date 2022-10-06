import pickle
import os
#
'''
label = 'label1'
#path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses/synthetic_dataset/'+ label
path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses/synthetic_dataset/'


os.chdir(path)
goal_set = pickle.load(open('goal_set.p', 'rb'))
print(goal_set["train"])
#'''
# test'''
#perf = {4994: {'success_rate': 0.5, 'average_reward': 0.062, 'average_turn': 15.536, 'average_match_rate': 0.167, 'average_match_rate2': 0.334, 'average_repeated_action': 0.011}, 4995: {'success_rate': 0.468, 'average_reward': -1.404, 'average_turn': 16.884, 'average_match_rate': 0.156, 'average_match_rate2': 0.34, 'average_repeated_action': 0.01}, 4996: {'success_rate': 0.479, 'average_reward': 2.336, 'average_turn': 15.078, 'average_match_rate': 0.179, 'average_match_rate2': 0.342, 'average_repeated_action': 0.005}, 4997: {'success_rate': 0.47, 'average_reward': -2.664, 'average_turn': 15.994, 'average_match_rate': 0.18, 'average_match_rate2': 0.358, 'average_repeated_action': 0.01}, 4998: {'success_rate': 0.489, 'average_reward': 1.998, 'average_turn': 16.216, 'average_match_rate': 0.167, 'average_match_rate2': 0.345, 'average_repeated_action': 0.008}, 4999: {'success_rate': 0.485, 'average_reward': 4.298, 'average_turn': 15.284, 'average_match_rate': 0.17, 'average_match_rate2': 0.331, 'average_repeated_action': 0.009}}
#s = 0
#for i in perf:
    #print(perf[i])
    #if perf[i]['success_rate'] > s:
        #s = perf[i]['success_rate']
#print(s)

path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses/MeicalChatbot-HRL-master/model/DQN/performance_new'
os.chdir(path)
data = pickle.load(open('_4999.p', 'rb'))
#print(data)
s = 0
t = 0
for i in data:
    if data[i]['success_rate'] > s:
        s = data[i]['success_rate']
        t = data[i]['average_turn']

print('higher success rate ',s)
print('average turn',t)
#'''
'''
record = ['disease_record.p', 'lower_reward_by_group.p', 'master_index_by_group.p', 'symptom_by_group.p']
path = 'C:/Users/hady_/Desktop/Conversational agent for medical diagnoses\MeicalChatbot-HRL-master/src/data'
os.chdir(path)
data2 = pickle.load(open('symptom_by_group.p','rb'))
data2
'''