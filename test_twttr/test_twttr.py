from twttr import shorten

def main():
    test_shorten()
    
def test_shorten():
    assert shorten('moshe') == 'msh'
    assert shorten('twitter') == 'twttr'
    assert shorten('Kochava') == 'Kchv'
    assert shorten('moshe8') == 'msh8'
    assert shorten('rozenbaum.') == 'rznbm.'
    assert shorten('Octopus') == 'ctps'

if __name__ == "__main__":
    main()