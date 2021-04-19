def anagrams(word, words):
    letters = [
        letter for letter
        in word
    ]
    anagrams = [
        word for word
        in words if
        sorted(letters) == sorted([
            letter for letter
            in word
           ])
    ]
    return anagrams

def test_solution():
	assert(
		anagrams(
			'abba',
			['aabb', 'abcd', 'bbaa', 'dada']
		) == ['aabb', 'bbaa'])
	assert(
		anagrams(
			'racer',
			['crazer', 'carer', 'racar', 'caers', 'racer'
		]) == ['carer', 'racer'])

if __name__ == "__main__":
	test_solution()
