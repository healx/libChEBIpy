'''
libChEBIpy (c) University of Manchester 2015

libChEBIpy is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
import json
import urllib
import urllib2

from libchebipy._chebi_entity import ChebiEntity as ChebiEntity
from libchebipy._chebi_entity import ChebiException as ChebiException
from libchebipy._comment import Comment as Comment
from libchebipy._compound_origin import CompoundOrigin as CompoundOrigin
from libchebipy._database_accession import DatabaseAccession \
    as DatabaseAccession
from libchebipy._formula import Formula as Formula
from libchebipy._name import Name as Name
from libchebipy._reference import Reference as Reference
from libchebipy._relation import Relation as Relation
from libchebipy._structure import Structure as Structure
from pandas.stats.interface import ols


def search(term, exact=False):
    '''Searches ChEBI via ols.'''
    url = 'http://www.ebi.ac.uk/ols/api/search?ontology=chebi' + \
        '&exact=' + str(exact) + '&queryFields=label&q=' + urllib.quote(term)

    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    return [ChebiEntity(doc['obo_id']) for doc in data['response']['docs']]
