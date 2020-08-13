
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	allen = 0
	at = 0
	ap = 0
	viki = 0
	vt = 0
	vp = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				at += 1
			elif s[2] == '圖片':
				ap += 1
			else:
				for n in s[2:]:
					allen += len(n)
		elif name == 'Viki':
			if s[2] == '貼圖':
				vt += 1
			elif s[2] == '圖片':
				vp += 1
			else:
				for n in s[2:]:
					viki += len(n)
		#print(line)
	print('Allen said', allen, 'words', ',', 'sent', at, 'stickers', ',', 'sent', ap, 'pictures')
	print('Viki said', viki, 'words', ',', 'sent', vt, 'stickers', ',', 'sent', vp, 'pictures')

def write_file(filename, lines):
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	filename = 'LINE-Viki.txt'
	lines = read_file(filename)
	convert(lines)
	#write_file('output.txt', lines)
main()