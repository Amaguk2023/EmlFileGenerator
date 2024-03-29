from datetime import datetime
import sys
from art import tprint

#METADATA CREATION PROMPT
def email_metadata_content_prompt():
	from_ = False
	while not from_:
		try:
			from_ = input('From: ').lower()
			sent_ = input('Sent: (T = Today / N = New Date) ').title()
			if sent_ == 'T':
				sent_ = datetime.now()
			else:
				sent_ = input('Sent: ').title()	
			to_ = input('To: ').lower()
			subject_ = input('Subject: ').title()
			content_creation(from_, sent_, to_, subject_)
		except ValueError:
			print('Check your spelling, value not accepted')
		except KeyboardInterrupt:
			print('\nGoodbye\n')
			sys.exit()

#CONTENT CREATION PROMPT		
def content_creation(from_, sent_, to_, subject_):
	print('\nContent: (Write \'endofmail\' after hitting enter to save the content or else an UnboundLocalError will be thrown.)\n')
	content_list = []
	while True:
		line = input()
		if 'endofmail' in line:
			break
		content_list.append(line)
		content = '\n'.join(content_list)
	eml_metadata_content_wrap(from_, sent_, to_, subject_, content)
				
#WRAP THE METADATA AND CONTENT IN ORDER
def eml_metadata_content_wrap(from_, sent_, to_, subject_, content):
	eml_From = ('From: {from_}'.format(from_=from_))
	eml_Sent= ('Sent: {sent_}'.format(sent_=sent_))
	eml_To= ('To: {to_} '.format(to_=to_))
	eml_Subject = ('Subject: {subject_}'.format(subject_=subject_))
	eml = eml_From + '\n' + eml_Sent + '\n' + eml_To + '\n' + eml_Subject + '\n' + '\n' + content + '\n'
	eml_file_creation(eml)

#OPEN .EML FILE, SAVE, EXPORT.
def eml_file_creation(eml):
	name = input('\nWrite down the file name (Don\'t include \'.eml\' ) >> ')
	with open(name + '.eml', 'w') as email:
		email.write(''.join(eml))
		print('\neml file has been exported!\n')

#INITIAL MESSAGE
print('\nWelcome to AGK eml file generator\n')
tprint('''
	EML
	FILE
	GENERATOR''', font='aquaplan')

if __name__ == '__main__':
	email_metadata_content_prompt()







