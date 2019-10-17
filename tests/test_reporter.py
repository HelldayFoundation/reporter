from reporter.header import create_header

""" fonctions de test pour create_header """
def test_create_header_incomplete():
	#liste de dictionnaires pour create_header, incomplete pour test
        authors_list = [   
            {"first" : "Le premier"},
            {"last":"Le second"},
            {"first" : "Le premier", "last":"Le second"},
        ]
        loc = "Londres"
        #On appelle la fonction dans une variable
        res = create_header(authors_list,loc)
        
        if not "premier" in res:  # si la chaine attendue n'est pas là. Pourrait être "assert". 
            raise ValueError('On trouve pas le premier')      # on remonte volontairement une erreur avec un message
        assert "Londres" in res #on force le nom de "loc" et on test sa prise en compte.


def test_create_header_withloc():
    auth_list = [
        {"first": "Jojo",
         "last": "Juju",},
        {"first": "Dodo",
         "last": "Dudu",},
    ]
    
    res = create_header(auth_list, "NY")
    
    assert "NY" in res

def test_create_header_incomplete():
    auth_list = [
        {"first": "Jojo",},
        {"last": "Dodo",},
    ]
    
    res = create_header(auth_list, "NY")
    
    assert "Dudu" in res
    assert "Jojo" in res


