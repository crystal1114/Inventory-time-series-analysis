#  _________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright (c) 2014 Sandia Corporation.
#  Under the terms of Contract DE-AC04-94AL85000 with Sandia Corporation,
#  the U.S. Government retains certain rights in this software.
#  This software is distributed under the BSD License.
#  _________________________________________________________________________
#
# ad: Annotated with location of stochastic rhs entries
#       for use with pysp2smps conversion tool.

import itertools
import random

from pyomo.core import *
from pyomo.pysp.annotations import (PySP_ConstraintStageAnnotation,
                                    PySP_StochasticRHSAnnotation)

#
# Define the probability table for the stochastic parameters
#
demand=[0，110.2848,123.4493,108.7793,111.7802,120.6422]
y_start=101.38

d1_rhs_table=\
[-0.000857745,-0.004360359,0.006247019,-0.007466512,-0.005190053,
0.003739198,-0.000281543,-0.01775575,0.00521002,0.002557547,
0.003315072,0.008304421,-2.209539,-0.5987525,0.6191887,
4.866312,-0.01349693,1.377007,-0.6311139,2.350632,
0.5359557,1.159893,1.646791,-1.402757,-2.018934,
3.587489,0.04279932,-0.8683697,4.851779,0.7572866,
-1.262768,-2.717473,2.686227,-2.43172,-2.64504,
0.406923,-0.9558075,-2.79891,-3.523102,-5.197554,
-1.106004,-0.3417804,6.252632,2.106569,0.1870523,
1.089157,-2.945359,3.39181,-2.86756,-0.9906556,
6.519179,2.175354,-0.5513542,1.097396,-4.053061,
2.083399,4.809785,1.185102,2.337311,5.029688,
-8.733815]


num_scenarios = len(d1_rhs_table)
scenario_data = dict(('Scenario'+str(i), (d1val))
                      for i, (d1val) in
                     enumerate(d1_rhs_table, 1))

#
# Define the reference model
#

model = ConcreteModel()

# these annotations are required for using this
# model with the SMPS conversion tool
model.constraint_stage = PySP_ConstraintStageAnnotation()
model.stoch_rhs = PySP_StochasticRHSAnnotation()

# use mutable parameters so that the constraint
# right-hand-sides can be updated for each scenario
model.d1_rhs = Param(mutable=True, initialize=0.0)

# first-stage variables
model.delta1 = Var(bounds=(0,300))
model.delta2 = Var(bounds=(0,300))
model.delta3 = Var(bounds=(0,300))
model.delta4 = Var(bounds=(0,300))
# model.delta5 = Var(bounds=(0,300))

# second-stage variables

model.y1 = Var(within=NonNegativeReals)
model.z1 = Var(within=NonNegativeReals)
model.x1 = Var(within=NonNegativeReals)

model.y2 = Var(within=NonNegativeReals)
model.z2 = Var(within=NonNegativeReals)
model.x2 = Var(within=NonNegativeReals)

model.y3 = Var(within=NonNegativeReals)
model.z3 = Var(within=NonNegativeReals)
model.x3 = Var(within=NonNegativeReals)

model.y4 = Var(within=NonNegativeReals)
model.z4 = Var(within=NonNegativeReals)
model.x4 = Var(within=NonNegativeReals)

model.y5 = Var(within=NonNegativeReals)
model.z5 = Var(within=NonNegativeReals)
model.x5 = Var(within=NonNegativeReals)

totalCost = model.x1+model.x2+model.x3+model.x4+model.x5+3*(model.z1+model.z2+model.z3+model.z4+model.z5)


# stage-cost expressions
model.FirstStageCost = \
    Expression(initialize=0)
model.SecondStageCost = \
    Expression(initialize=(totalCost))

#
# this model has two first-stage constraints
#

# model.s1 = Constraint(expr= model.x1 - 0.5*model.x2 >= 0)
# model.constraint_stage.declare(model.s1, 1)

# model.s2 = Constraint(expr= model.x1 + model.x2 <= 200)
# model.constraint_stage.declare(model.s2, 1)

#
# this model has four second-stage constraints
#



model.s11 = Constraint(expr= model.y1 == y_start)
model.constraint_stage.declare(model.s11, 2)

model.s12 = Constraint(expr= model.x1 >= model.y1-demand[1]-model.d1_rhs)
model.constraint_stage.declare(model.s12, 2)
model.stoch_rhs.declare(model.s12)

model.s13 = Constraint(expr= model.z1 >= demand[1]+model.d1_rhs - model.y1)
model.constraint_stage.declare(model.s13, 2)
model.stoch_rhs.declare(model.s13)
############################################################################

model.s21 = Constraint(expr= model.y2 == model.x1+ model.delta1)
model.constraint_stage.declare(model.s21, 2)

model.s22 = Constraint(expr= model.x2 >= model.y2-demand[2]-model.d1_rhs)
model.constraint_stage.declare(model.s22, 2)
model.stoch_rhs.declare(model.s22)

model.s23 = Constraint(expr= model.z2 >= demand[2]+model.d1_rhs - model.y2)
model.constraint_stage.declare(model.s23, 2)
model.stoch_rhs.declare(model.s23)
############################################################################
model.s31 = Constraint(expr= model.y3 == model.x2+ model.delta2)
model.constraint_stage.declare(model.s31, 2)

model.s32 = Constraint(expr= model.x3 >= model.y3-demand[3]-model.d1_rhs)
model.constraint_stage.declare(model.s32, 2)
model.stoch_rhs.declare(model.s32)

model.s33 = Constraint(expr= model.z3 >= demand[3]+model.d1_rhs - model.y3)
model.constraint_stage.declare(model.s33, 2)
model.stoch_rhs.declare(model.s33)
#############################################################################
model.s41 = Constraint(expr= model.y4 == model.x3+ model.delta3)
model.constraint_stage.declare(model.s41, 2)

model.s42 = Constraint(expr= model.x4 >= model.y4-demand[4]-model.d1_rhs)
model.constraint_stage.declare(model.s42, 2)
model.stoch_rhs.declare(model.s42)

model.s43 = Constraint(expr= model.z4 >= demand[4]+model.d1_rhs - model.y4)
model.constraint_stage.declare(model.s43, 2)
model.stoch_rhs.declare(model.s43)
###########################################################################
model.s51 = Constraint(expr= model.y5 == model.x4+ model.delta4)
model.constraint_stage.declare(model.s51, 2)

model.s52 = Constraint(expr= model.x5 >= model.y5-demand[5]-model.d1_rhs)
model.constraint_stage.declare(model.s52, 2)
model.stoch_rhs.declare(model.s52)

model.s53 = Constraint(expr= model.z5 >= demand[5]+model.d1_rhs - model.y5)
model.constraint_stage.declare(model.s53, 2)
model.stoch_rhs.declare(model.s53)
#
# these one constraints have stochastic right-hand-sides
#
# model.d1 = Constraint(expr = 3.1470 + 0.046*model.x1 + 0.184*model.x2 - model.y1 - model.y2 >=model.d1_rhs)
# model.constraint_stage.declare(model.d1, 2)
# model.stoch_rhs.declare(model.d1)

# always define the objective as the sum of the stage costs
model.obj = Objective(expr=model.FirstStageCost + model.SecondStageCost)

def pysp_scenario_tree_model_callback():
    from pyomo.pysp.scenariotree.tree_structure_model import \
        CreateConcreteTwoStageScenarioTreeModel

    st_model = CreateConcreteTwoStageScenarioTreeModel(num_scenarios)

    first_stage = st_model.Stages.first()
    second_stage = st_model.Stages.last()

    # First Stage
    st_model.StageCost[first_stage] = 'FirstStageCost'
    st_model.StageVariables[first_stage].add('delta1')
    st_model.StageVariables[first_stage].add('delta2')
    st_model.StageVariables[first_stage].add('delta3')
    st_model.StageVariables[first_stage].add('delta4')
    #st_model.StageVariables[first_stage].add('delta5')

    # Second Stage
    st_model.StageCost[second_stage] = 'SecondStageCost'
    st_model.StageVariables[second_stage].add('y1')
    st_model.StageVariables[second_stage].add('y2')
    st_model.StageVariables[second_stage].add('y3')
    st_model.StageVariables[second_stage].add('y4')
    st_model.StageVariables[second_stage].add('y5')

    st_model.StageVariables[second_stage].add('z1')
    st_model.StageVariables[second_stage].add('z2')
    st_model.StageVariables[second_stage].add('z3')
    st_model.StageVariables[second_stage].add('z4')
    st_model.StageVariables[second_stage].add('z5')

    st_model.StageVariables[second_stage].add('x1')
    st_model.StageVariables[second_stage].add('x2')
    st_model.StageVariables[second_stage].add('x3')
    st_model.StageVariables[second_stage].add('x4')
    st_model.StageVariables[second_stage].add('x5')
    return st_model

def pysp_instance_creation_callback(scenario_name, node_names):

    #
    # Clone a new instance and update the stochastic
    # parameters from the sampled scenario
    #

    instance = model.clone()

    d1_rhs_val = scenario_data[scenario_name]
    instance.d1_rhs.value = d1_rhs_val

    return instance
