import unittest
import urlparse
import json

from leonardo import graph

from . import DATA_DIR


class GraphTest(unittest.TestCase):
    
    maxDiff = None

    def test_graph_init(self):
        g = graph.GraphiteGraph("%s/cpu.graph" % DATA_DIR)
        self.assertEqual( g.properties.get("title") , "Combined CPU Usage")

    def test_url(self):
        g = graph.GraphiteGraph("%s/cpu.graph" % DATA_DIR)
        parts = urlparse.parse_qs( g.url(), keep_blank_values=True)
        self.assertEqual ( parts, 
            {   'from'  : ['-1hour'], 
                'target': ['cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.wait.value),"IO Wait"),"si")', 
                         'cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.system.value),"System"),"si")', 
                         'cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.user.value),"User"),"si")'], 
                'title': ['Combined CPU Usage'], 
                'areaMode': ['stacked'], 
                'height': ['None'], 
                'width': ['None'], 
                'vtitle': ['percent'], 
                'until': ['Now']
            }
        )

    def test_get_graph_spec(self):
        g = graph.GraphiteGraph("%s/cpu.graph" % DATA_DIR)
        expected_result = {     'url': 'title=Combined CPU Usage&vtitle=percent&from=-1hour&width=None&height=None&until=Now&areaMode=stacked&target=cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.wait.value),"IO Wait"),"si")&target=cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.system.value),"System"),"si")&target=cactiStyle(alias(sumSeries(collectd.server-1.cpu.*.cpu.user.value),"User"),"si")&format=json',
                                'properties':
                                {   'ymaxright': None,
                                    'yunit_system': None,
                                    'height': None,
                                    'hide_y_axis': None,
                                    'timezone': None,
                                    'hide_axes': None,
                                    'ymin': None,
                                    'background_color': None,
                                    'vtitle_right': None,
                                    'draw_null_as_zero': False,
                                    'fontbold': False,
                                    'linewidth': None,
                                    'from': '-1hour',
                                    'ymax': None,
                                    'title': 'Combined CPU Usage',
                                    'minor_grid_line_color': None,
                                    'foreground_color': None,
                                    'width': None,
                                    'theme': None,
                                    'area_alpha': None,
                                    'hide_grid': None,
                                    'until': 'Now',
                                    'linemode': None,
                                    'description': 'The combined CPU usage',
                                    'graphtype': None,
                                    'fontsize': None,
                                    'vtitle': 'percent',
                                    'logbase': None,
                                    'placeholders': None,
                                    'surpress': False,
                                    'yminright': None,
                                    'major_grid_line_color': None,
                                    'area': 'stacked',
                                    'unique_legend': None,
                                    'fontname': None,
                                    'xformat': None,
                                    'hide_legend': None,
                                    'margin': None,
                                    'color_list': None}}

        self.assertEqual( expected_result, g.get_graph_spec()  )

