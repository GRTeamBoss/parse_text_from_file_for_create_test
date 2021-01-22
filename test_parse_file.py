intro = """This script parse from file asks and answers.\nPlease separate asks, answers and true answer with: "+" and "-".\nExample: this-is-ask? -1.var+vars-2.var-3.var-4.var "1" or "1var" """
print(intro + '\n')

file = str(input("File name: "))
print('')
file_open = open('%s' % file, 'r')
file_read = file_open.read()
file_open.close()
text = file_read.split()
ball = 0
true_answer = ''
false_answer = ''
ask = []
answer = []
correct = []
ask_modify = []
answer_modify = []
answer_modify_second = []

def print_test():
	global ask, answer, correct, ask_modify, answer_modify, ball, true_answer, false_answer
	for i in range(0, len(ask)):
		n = str(i + 1)
		ask_modify.append(ask[i].split('-'))
		answer_modify.append(answer[i].split('-'))
		print(n + '. ' + ' '.join(ask_modify[i]))
		print('')
		print('\n'.join(answer_modify[i]).replace('+', ' '))
		print('')
		answer_input = str(input())
		if answer_input == correct[i]:
			ball += 1
			true_answer += str(n) + ', '
		else:
			false_answer += str(n) + ', '
		print('')
	return ball, true_answer, false_answer

def get_ask():
	global ask, text
	for i in range(0, len(text), 3):
		ask.append(text[i])
	return ask

def get_answer():
	global answer, text
	for i in range(1, len(text), 3):
		answer.append(text[i])
	return answer

def get_correct():
	global correct, text
	for i in range(2, len(text), 3):
		correct.append(text[i])
	return correct

get_ask()
get_answer()
get_correct()
print_test()
print("Result: " + str(ball) + "ball(-s)")
print("True answer: " + true_answer)
print("False answer: " + false_answer)