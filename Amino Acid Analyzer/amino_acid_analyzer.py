# Protein! (Week 4 coding exercise)
# Mike Kim
# February 3rd, 2022

# List, accumulators and dictionaries

# Abbreviated list
amino_acids = ["A","D","F","G","M","T"]

# accumulators per amino acid
amino_tally = {'A':0, 'D':0, 'F':0, 'G':0, 'M':0, 'T':0}
# accumulator for error
error = 0

# name of the amino acids
amino_name = {'A':'Alanine', 'D':'Aspartic Acid', \
'F':'Phenylalanine', 'G':'Glycine', \
'M':'Methionine', 'T':'Threonine'} 

# ask user
acid_sequence = input("Enter an amino acid sequence: ").upper()

# accumulating process
for i in range(len(acid_sequence)):
  if acid_sequence[i] in amino_tally:
    amino_tally[acid_sequence[i]] += 1
  else:
    error += 1

# percentages

a_percentage = amino_tally['A'] / len(acid_sequence) * 100
d_percentage = amino_tally['D'] / len(acid_sequence) * 100
f_percentage = amino_tally['F'] / len(acid_sequence) * 100
g_percentage = amino_tally['G'] / len(acid_sequence) * 100
m_percentage = amino_tally['M'] / len(acid_sequence) * 100
t_percentage = amino_tally['T'] / len(acid_sequence) * 100
error_percentage = error / len(acid_sequence) * 100


# ending /report:
if acid_sequence[-1] in amino_acids:
  print("REPORT ON PROTEIN: " + acid_sequence[0]\
  + " -- " + acid_sequence[-1])
else:
  print("REPORT ON PROTEIN: " + acid_sequence[0] + " -- " + "*")

# Sequence length:
print("Sequence length: ", len(acid_sequence))

# Each amino acids info:

# A
print(amino_name['A'], ": " , amino_tally['A'],\
 ",{:.3f}".format(a_percentage), "%")

# D
print(amino_name['D'], ": " , amino_tally['D'],\
 ",{:.3f}".format(d_percentage), "%")

# F
print(amino_name['F'], ": " , amino_tally['F'],\
 ",{:.3f}".format(f_percentage), "%")

# G
print(amino_name['G'], ": " , amino_tally['G'],\
 ",{:.3f}".format(g_percentage), "%")

# M
print(amino_name['M'], ": " , amino_tally['M'],\
 ",{:.3f}".format(m_percentage), "%")

# T
print(amino_name['T'], ": " , amino_tally['T'],\
 ",{:.3f}".format(t_percentage), "%")

# Error
print("Error: ", error, ",{:.3f}".format(error_percentage), "%")
