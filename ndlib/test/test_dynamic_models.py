from __future__ import absolute_import

import unittest
import past.builtins
import dynetx as dn
import networkx as nx

import ndlib.models.ModelConfig as mc
import ndlib.models.dynamic.DynSIModel as si
import ndlib.models.dynamic.DynSIRModel as sir
import ndlib.models.dynamic.DynSISModel as sis


class DynTest(unittest.TestCase):

    def test_DynSI(self):
        dg = dn.DynGraph()

        for t in past.builtins.xrange(0, 3):
            g = nx.erdos_renyi_graph(200, 0.05)
            dg.add_interactions_from(g.edges(), t)

        model = si.DynSIModel(dg)
        config = mc.Configuration()
        config.add_model_parameter('beta', 0.1)
        config.add_model_parameter("percentage_infected", 0.1)
        model.set_initial_status(config)
        iterations = model.execute_snapshots()
        self.assertEqual(len(iterations), 3)

        iterations = model.execute_iterations()
        trends = model.build_trends(iterations)
        self.assertEqual(len(trends[0]['trends']['status_delta'][1]),
                         len([x for x in dg.stream_interactions() if x[2] == "+"]))

    def test_DynSIS(self):
        dg = dn.DynGraph()

        for t in past.builtins.xrange(0, 3):
            g = nx.erdos_renyi_graph(200, 0.05)
            dg.add_interactions_from(g.edges(), t)

        model = sis.DynSISModel(dg)
        config = mc.Configuration()
        config.add_model_parameter('beta', 0.1)
        config.add_model_parameter('lambda', 0.1)
        config.add_model_parameter("percentage_infected", 0.1)
        model.set_initial_status(config)
        iterations = model.execute_snapshots()
        self.assertEqual(len(iterations), 3)

        iterations = model.execute_iterations()
        trends = model.build_trends(iterations)
        self.assertEqual(len(trends[0]['trends']['status_delta'][1]),
                         len([x for x in dg.stream_interactions() if x[2] == "+"]))

    def test_DynSIR(self):
        dg = dn.DynGraph()

        for t in past.builtins.xrange(0, 3):
            g = nx.erdos_renyi_graph(200, 0.05)
            dg.add_interactions_from(g.edges(), t)

        model = sir.DynSIRModel(dg)
        config = mc.Configuration()
        config.add_model_parameter('beta', 0.1)
        config.add_model_parameter('gamma', 0.1)
        config.add_model_parameter("percentage_infected", 0.1)
        model.set_initial_status(config)
        iterations = model.execute_snapshots()
        self.assertEqual(len(iterations), 3)

        iterations = model.execute_iterations()
        trends = model.build_trends(iterations)
        self.assertEqual(len(trends[0]['trends']['status_delta'][1]),
                         len([x for x in dg.stream_interactions() if x[2] == "+"]))
