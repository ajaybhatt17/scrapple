"""
scrapple.selectors.xpath
~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import print_function

from lxml.etree import XPathError

from scrapple.selectors.css import CssSelector
from scrapple.utils.text import make_ascii
import json
from lxml import etree
from lxml import cssselect
from lxml.etree import fromstring

try:
	from urlparse import urljoin
except ImportError:
	from urllib.parse import urljoin


class ApiSelector(CssSelector):
	"""
	The ``XpathSelector`` object defines XPath expressions.

	"""
	
	def __init__(self, url, path='', header_options={}):
		"""
		The ``Selector`` class acts as the super class for this class.

		"""
		super(ApiSelector, self).__init__(url, header_options)
		if path != '':
			self.json_data = json.loads(self.content)[path]
			self.tree = etree.HTML(self.json_data)
		else:
			self.json_data = json.loads(self.content)
		