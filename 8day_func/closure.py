def knight2(saying):
    """
    클로저 개념 이해
    :param saying: 입력한 스트링값
    :return: 내부함수가 클로저 개념을 이용해 결과값 반환
    """
    def inner(*args, **kwargs):
        return "we are the knight! %s" %saying
    return inner()

print(knight2("ghahahahah"))


