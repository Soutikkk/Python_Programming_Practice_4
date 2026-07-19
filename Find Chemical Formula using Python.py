import pubchempy as pcp

chemical_name = input("Enter chemical name: ")

try:
    compound = pcp.get_compounds(chemical_name, 'name')[0]

    print("IUPAC Name:", compound.iupac_name)
    print("Common Name:", compound.synonyms[0] if compound.synonyms else "N/A")
    print("Molecular Weight:", compound.molecular_weight)
    print("Formula:", compound.molecular_formula)

except IndexError:
    print("No information found for", chemical_name)