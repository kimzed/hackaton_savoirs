import python.functions as functions
import unicodedata


def test_remove_duplicates_from_list_removes_duplicate():
    list_to_clean = ["abc", "abc", "efg"]

    list_cleaned = functions.remove_duplicates_from_list(list_to_clean)

    list_expected = ["abc", "efg"]

    assert (list_cleaned == list_expected)

def normalize_string_to_nfc(text:str)->str:

    norm = unicodedata.normalize('NFC', text)
    #test_return = f"{form}: {norm} ({len(norm.encode('utf-8'))} bytes)"

    return norm

accented_text = "RÃ©seaux, gÃ©nÃ©alogies, contratsÂ : collectifs savants Lieux de savoirÂ 1"
print(normalize_string_to_nfc(accented_text))


test_remove_duplicates_from_list_removes_duplicate()