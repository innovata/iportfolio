
import pandas as pd
import json
from idatamap import models, APP_PATH
import inspect
import sys
sys.path.append('/Users/sambong/libs/idebug')
sys.path.append('/Users/sambong/libs/ilib')
import idebug as dbg


class Nodes:

    def save(self, csv=True):
        func = dbg.Function(inspect.currentframe()).report_init()
        df = pd.read_csv(f"{APP_PATH}/data/KeywordFrequency.csv")
        df = df.rename(columns={'keyword':'id', 'freq':'group'})
        if csv:
            df.to_csv(f"{APP_PATH}/data/nodes.csv", index=False)
        else:
            for d in df.to_dict('records'):
                n = models.Node(name=d['id'], group=d['group'], category=d['category'], lang=d['lang'])
                n.save()
        func.report_fin()

    def get(self, category=None, lang='english'):
        func = dbg.Function(inspect.currentframe()).report_init()
        df = pd.read_csv(f"{APP_PATH}/data/nodes.csv")
        df = df[ df.lang == lang ]
        if len(df) is not 0:
            if category is not None:
                df = df[ df.category == category ]
                df = df.reindex(columns=['id','group'])
        func.report_fin()
        return df

    def load(self, category=None, lang='english'):
        func = dbg.Function(inspect.currentframe()).report_init()
        entries = Node.objects.filter(category=category, lang=lang)
        nodes = []
        for entry in entries:
            nodes.append({'id':entry.keyword, 'group':entry.freq})
        df = pd.DataFrame(nodes)
        func.report_fin()
        return df

class Links:

    def transform(self, df):
        df.combination = df.combination.str.replace(pat="^\['|'\]$", repl="")
        df.combination = df.combination.apply(lambda x: x.split("', '"))
        df['source'] = df.combination.apply(lambda x: x[0])
        df['target'] = df.combination.apply(lambda x: x[1])
        df = df.rename(columns={'strength':'value'})
        return df.reindex(columns=['source','target','value'])

    def save(self, csv=True):
        func = dbg.Function(inspect.currentframe()).report_init()
        df = pd.read_csv(f"{APP_PATH}/data/KeywordCombinationStrength.csv")
        df = self.transform(df)
        if csv:
            df.to_csv(f"{APP_PATH}/data/links.csv", index=False)
        else:
            for d in df.to_dict('records'):
                link = models.Link(source=d['source'], target=d['target'], value=d['value'])
                link.save()
        func.report_fin()
        return self

    def filter(self, df, nodes):
        df = df[ df.source.isin(list(nodes.id)) ]
        df = df[ df.target.isin(list(nodes.id)) ]
        return df

    def get(self, nodes):
        func = dbg.Function(inspect.currentframe()).set_invisible_regex(['nodes']).report_init()
        df = pd.read_csv(f"{APP_PATH}/data/links.csv")
        df = self.filter(df, nodes)
        func.report_fin()
        return df

    def load(self, nodes):
        func = dbg.Function(inspect.currentframe()).set_invisible_regex(['nodes']).report_init()
        entries = Link.objects.all()
        links = []
        for entry in entries:
            links.append({'source':entry.source, 'target':entry.target, 'value':entry.value})
        df = pd.DataFrame(links)
        df = self.filter(df, nodes)
        func.report_fin()
        return df

def get(category=None, lang='english'):
    nodes = Nodes().get(category, lang)
    links = Links().get(nodes)
    mapdata = json.dumps({'nodes': nodes.to_dict('records'), 'links': links.to_dict('records')})
    return mapdata

#def load_mapdata(category=None, lang='english'):
