
from datamap.tests import *

from datamap.project import *
from . import dbg

import unittest
import json

#@unittest.skip("showing class skipping")
class KeywordTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test__get_nodes__tech_category(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        nodedf = Keyword().get_nodes(freq=1, category='Tech')

        dbg.print_df(nodedf)
        ids = list(nodedf.id)
        self.assertIn('Python', ids)
        self.assertNotIn('영어', ids)

    @unittest.skip("demonstrating skipping")
    def test__changed_colnames(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        nodedf = Keyword().get_nodes(freq=10)
        df = pd.DataFrame(nodes)
        self.assertEqual( set(list(df.columns)), set(['id','group']) )

    @unittest.skip("demonstrating skipping")
    def test__freq_threshold(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        nodedf = Keyword().get_nodes(freq=10)
        df = pd.DataFrame(nodes)
        freqs = list(df.group)
        for freq in freqs:
            self.assertGreaterEqual(freq, 10)

@unittest.skip("showing class skipping")
class KeywordCombinationTestCase(unittest.TestCase):

    #@unittest.skip("demonstrating skipping")
    def test__init(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        k = KeywordCombination()
        dbg.print_obj(k)
        self.assertEqual(k.tblname, 'KeywordCombination')

    #@unittest.skip("demonstrating skipping")
    def test__get_links(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        links = KeywordCombination().get_links(strength=3)
        df = pd.DataFrame(links)
        dbg.print_df(df)
        self.assertEqual( set(list(df.columns)), set(['source','target','value']) )

    #@unittest.skip("demonstrating skipping")
    def test__get_unq_keywords_in_combination(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        k = KeywordCombinationStrength()
        keywords = k.get_unq_keywords_in_combination()

        pp.pprint(keywords)

@unittest.skip("showing class skipping")
class ModuleFuncsTestCase(unittest.TestCase):

    #@unittest.skip("demonstrating skipping")
    def test__get_mapdata(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        map_data = get_mapdata(freq=10, strength=3)
        #print(f"\n type(map_data) : {type(map_data)}\n")
        self.assertTrue( isinstance(map_data, str) )
        print(f"\n json.loads(map_data) :\n\n")
        pp.pprint(json.loads(map_data))

    #@unittest.skip("demonstrating skipping")
    def test__apply_useless_keyword(self):
        print(f"\n{'='*60}\n {__class__.__name__} : {inspect.stack()[0][3]}\n")
        apply_useless_keyword(keyword='Ol')






def main():
    unittest.main()
