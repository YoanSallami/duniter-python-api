#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
# Caner Candan <caner@candan.fr>, http://caner.candan.fr
#

from .. import API, logging

logger = logging.getLogger("ucoin/network")


class Network(API):
    """
    /network/* , this URL is used for the "UCoin Gossip" protocol (exchanging UC.G. messages).
    """
    def __init__(self, connection_handler, module='network'):
        """
        Constructor

        :param connection_handler: The connection handler.
        :param str module: (Default value = network)
        """
        super(Network, self).__init__(connection_handler, module)


class Peering(Network):
    """GET peering information about a peer."""

    def __get__(self, **kwargs):
        """
        GET peering information about a peer : /network/peering

        :param kwargs:
        """
        r = yield from self.requests_get('/peering', **kwargs)
        return (yield from r.json())

from . import peering
