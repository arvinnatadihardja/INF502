def user_input():
	shift = int(raw_input("Maximum shift: "))
	approach = int(raw_input("1 for number of matches and 2 for maximum chain: "))
	in1 = raw_input("first sequence file path")
	in2 = raw_input("second sequence file path")

	return shift, approach, in1, in2

def file_input(file_path):
	tmp_f = open(file_path)
	seq = tmp_f.readlines()

	return seq[0]

def basic_similar(seq1, seq2):
	score = 0
	for c in seq1:
		tmp_ind = seq1.index(c)
		if c == seq2[tmp_ind]:
			score = score + 1
		else:
			pass

	return score

def max_cont(seq1, seq2):
	score = 0
	iter_len = len(seq1)
	x = 0
	while (x < iter_len):
		if seq1[x] == seq2[x]:
			tmp_score = 1
			y = x
			while (y<iter_len) and (seq1[y] == seq2[y]):
				tmp_score = tmp_score + 1
				y = y+1
		try:
			if tmp_score>score:
				score = tmp_score
		except Exception as e:
			pass
		x = x+1

	return score

def shift_seq(seq1, seq2):
	seq1 = "N"+seq1
	seq2 = seq2+"N"

	return seq1, seq2

if __name__ == "__main__":
	shift, approach, in1, in2 = user_input()
	seq1 = file_input(in1)
	seq2 = file_input(in2)
	main_score = 0
	tmp1_seq1, tmp1_seq2 = seq1, seq2
	tmp2_seq1, tmp2_seq2 = seq1, seq2
	for s in range(0,shift):
		if approach == 1:
			tmp_score = basic_similar(tmp1_seq1, tmp1_seq2)
		else:
			tmp_score = max_cont(tmp1_seq1, tmp1_seq2)

		tmp1_seq1, tmp1_seq2 = shift_seq(tmp1_seq1, tmp1_seq2)

		if tmp_score > main_score:
			main_score = tmp_score

		if approach == 1:
			tmp_score = basic_similar(tmp2_seq1, tmp2_seq2)
		else:
			tmp_score = max_cont(tmp1_seq1, tmp1_seq2)

		tmp2_seq1, tmp2_seq2 = shift_seq(tmp2_seq2, tmp2_seq1)

		if tmp_score > main_score:
			main_score = tmp_score

	res_dict = {1: "Score for basic Similarity is " + str(main_score), 2: "Score for maximum CONTIGUOUS is " + str(main_score)}

	print res_dict[approach]

