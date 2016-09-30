'''
libChEBIpy (c) University of Manchester 2015

libChEBIpy is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import json
import urllib
import urllib2

from ._chebi_entity import ChebiEntity
from ._chebi_entity import ChebiException
from ._comment import Comment
from ._compound_origin import CompoundOrigin
from ._database_accession import DatabaseAccession
from ._formula import Formula
from ._name import Name
from ._reference import Reference
from ._relation import Relation
from ._structure import Structure
from pandas.stats.interface import ols


def search(term, exact=False):
    '''Searches ChEBI via ols.'''
    url = 'http://www.ebi.ac.uk/ols/api/search?ontology=chebi' + \
        '&exact=' + str(exact) + '&queryFields=label&q=' + urllib.quote(term)

    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    return [ChebiEntity(doc['obo_id']) for doc in data['response']['docs']]
