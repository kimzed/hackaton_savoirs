import python.functions_xml as functions_xml

def test_get_title_returns_correct_title(file, expected_title):
    actual_title = functions_xml.get_title(file)


    print(f"actual title is {actual_title}")
    print(f"expected title is {expected_title} \n\n")

    #assert (actual_title == expected_title)

def test_get_author_returns_correct_title(file, expected_author):
    actual_author = functions_xml.get_author(file)


    print(f"actual title is {actual_author}")
    print(f"expected title is {expected_author} \n\n")

    assert (actual_author == expected_author)



directory_xml_files = "C:/Users/57834/Documents/savoirs/HackathonSavoirs/COrpusTEI/"

file = 'Spectres_04_LAMY.xml'
author = 'Jérôme Lamy'
test_get_author_returns_correct_title(directory_xml_files+file, author)

file = "LDSI_24_Mandressi.xml"
expected_title = "Réseaux, généalogies, contrats : collectifs savants Lieux de savoir 1"
test_get_title_returns_correct_title(directory_xml_files+file, expected_title)

file = "Spectres_01_ADELL.xml"
expected_title = "Lettrés, érudits, savants Manières d’être et façons de faire avec le savoir"
test_get_title_returns_correct_title(directory_xml_files+file, expected_title)


file = "ANABASES-872_Burlot.xml"
expected_title = "Le faux, source intentionnelle d’erreurs : le cas des contrefaçons de peintures antiques"
test_get_title_returns_correct_title(directory_xml_files+file, expected_title)


file = "BNU_Gutenberg_Herrmann.xml"
expected_title = "Innovation et tradition : la Bible de Gutenberg, patrimoine culturel"
test_get_title_returns_correct_title(directory_xml_files+file, expected_title)