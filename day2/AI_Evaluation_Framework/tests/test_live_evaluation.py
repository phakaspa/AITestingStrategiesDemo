from executor import generate_response
from evaluator import evaluate_response

def test_france_capital_response():    
    question = "What is the capital of France?"    
    context = "The capital of France is Paris."    
    expected = "Paris is the capital of France."   
    actual = generate_response(question, context)    
    evaluation = evaluate_response(question=question, context=context, expected=expected, actual=actual,)    
    assert evaluation["Relevancy Pass"], (evaluation["Relevancy Reason"])   
    assert evaluation["Faithfulness Pass"], (evaluation["Faithfulness Reason"])