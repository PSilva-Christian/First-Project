import csv
import os

order = ("AGATC","TTTTTTCT","AATG","TCTAG","GATA","TATC","GAAA","TCTG")
qtds_in_txt = []
qtds_in_csv = []

def main():

    with open("databases/large.csv", newline='') as database:
        excel = csv.reader(database, delimiter=",", quotechar="|")

        cell_name = str("")
        compatible_person = str("")

        with open("sequences/6.txt", "r") as sequence:
            print(f"\t\t\nArchive: 1 \n")
            for l in sequence: #Lê os arquivos de sequencias e salva a maior sequencia
                for b in range(0, len(order)):
                    qtds_in_txt.append(longest_match(l, order[b]))

            firstline = True

            for row in excel: # Lê cada linha
                if firstline: # Ignora a primeira linha da tabela
                    firstline = False

                else:
                    for cell in row: # Lê cada célula

                        if cell.isalpha() and cell_name == "": # Se for o primeiro nome
                            cell_name = cell

                        elif cell.isnumeric(): # Se for numero
                            qtds_in_csv.append(int(cell))

                        elif cell.isalpha() and cell_name != "":

                            if qtds_in_csv == qtds_in_txt:
                                compatible_person = cell_name
                                print(f"\nName: {cell_name}\nSequence: {qtds_in_csv}\nArchive: {qtds_in_txt}")
                            cell_name = cell
                            qtds_in_csv.clear()

            qtds_in_txt.clear()

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
