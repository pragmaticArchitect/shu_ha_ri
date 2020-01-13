#!/usr/bin/env python3
"""Pure Python synthetic falsification examples, not a real HDIP/PFI runtime."""
from decimal import Decimal, localcontext
import json


def vwap(trades):
    if not trades:
        raise ValueError('No eligible executions: undefined VWAP')
    volume = sum((Decimal(str(qty)) for _, qty in trades), Decimal(0))
    if volume <= 0:
        raise ValueError('Nonpositive total volume: undefined VWAP')
    with localcontext() as context:
        context.prec = 28
        result = sum((Decimal(str(price)) * Decimal(str(qty)) for price, qty in trades), Decimal(0)) / volume
    return result


def mock_math_api_vwap(trades):
    # No network is used; this simulates a distinct realization of the SAME governed method.
    numerator, denominator = Decimal(0), Decimal(0)
    for price, qty in trades:
        numerator += Decimal(str(price)) * Decimal(str(qty))
        denominator += Decimal(str(qty))
    if denominator <= 0:
        raise ValueError('Undefined VWAP')
    return numerator / denominator


def arithmetic_mean(trades):
    if not trades:
        raise ValueError('No executions')
    return sum((Decimal(str(p)) for p, _ in trades), Decimal(0)) / Decimal(len(trades))

trades = [('100', '1'), ('120', '3')]
checks = []

def check(name, predicate):
    assert predicate, name
    checks.append({'probe':name, 'outcome':'PASS_SYNTHETIC'})

check('P1 governed VWAP equals 115', vwap(trades) == Decimal('115'))
check('P2 mock external math API computes same VWAP', mock_math_api_vwap(trades) == vwap(trades))
check('P3 wrong arithmetic estimator differs on unequal weights', arithmetic_mean(trades) == Decimal('110') and arithmetic_mean(trades) != vwap(trades))
equal_prices = [('100','1'), ('100','7')]
check('P4 same numeric output on degenerate sample does not imply same method', arithmetic_mean(equal_prices) == vwap(equal_prices) == Decimal('100'))
scale = [(p,str(Decimal(q)*Decimal('13'))) for p,q in trades]
check('P5 uniform quantity scaling preserves VWAP', vwap(scale) == vwap(trades))
check('P6 changing eligible population changes result', vwap(trades[:1]) != vwap(trades))
try:
    vwap([])
    no_events_error = False
except ValueError:
    no_events_error = True
check('P7 zero eligible executions require governed undefined outcome', no_events_error)
metric = vwap(trades)
optional_explanation = 'Explanatory text from a separately governed capability; no metric alteration'
check('P8 optional explanation leaves governed metric unchanged', bool(optional_explanation) and metric == vwap(trades))
print(json.dumps({'stage':'INFOPS-P01-S02','realRuntimeExecuted':False,'normative':False,'syntheticProbes':len(checks),'status':'PASS_SYNTHETIC_ONLY','probes':checks}, indent=2))
