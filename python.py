
from browser import document
from io import StringIO

def showQuestions():
	out = StringIO()
	out.write('<b>Questions</b>')
	out.write('<p>')
	out.write('These are the questions')
	questions = document['questions']
	questions.html=out.getvalue()
	out.close()

def showAnswers():
	out = StringIO()
	out.write('<b>Answers</b>')
	out.write('<p>')
	out.write('These are the answers')
	answers = document['answers']
	answers.html = out.getvalue()
	out.close()

def revealAnswers():
	showAnswers()

showQuestions()

revealButton=document['revealId']
revealButton.bind("click", revealAnswers)
