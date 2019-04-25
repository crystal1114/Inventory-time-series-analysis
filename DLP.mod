# parameters
var x1, >= 0;
var x2, >= 0;
var x3, >= 0;
var x4, >= 0;
var x5, >= 0;
var y1, >= 0;
var y2, >= 0;
var y3, >= 0;
var y4, >= 0;
var y5, >= 0;
var z1, >= 0;
var z2, >= 0;
var z3, >= 0;
var z4, >= 0;
var z5, >= 0;
var d2, >= 0;
var d3, >= 0;
var d4, >= 0;
var d5, >= 0;
var D1, == 103.05;

minimize object: x1+x2+x3+x4+x5+3*(z1+z2+z3+z4+z5);
minimize object: sum{i in 1..N} v[i]*y[i];
                                         
s.t. c1: y1 = 106.0461;
s.t. c2: -y1 + x1 >= -104.6734;
s.t. c3: y1 + z1 >= 104.6734;

s.t. c4: y2 = x1 + d2;
s.t. c5: -y2 + x2 >= -89.2025;
s.t. c6: y2 + z2 >= 89.2025;

s.t. c7: y3 = x2 + d3;
s.t. c8: -y3 + x3 >= -116.6163;
s.t. c9: y3 + z3 >= 116.6163;

s.t. c10: y4 = x3 + d4;
s.t. c11: - y4 + x4 >= -110.6412;
s.t. c12: y4 + z4 >= 110.6412;

s.t. c13: y5 = x4 + d5;
s.t. c14: - y5 + x5 >= -110.7723;
s.t. c15: y5 + z5 >= 110.7723;

s.t. c16: x1 in max(0,y1-D1);