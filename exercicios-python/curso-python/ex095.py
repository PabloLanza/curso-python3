def notas(* nts, sit=False):
    """ 
        notas(8 nts, sit=False)

        param * nts: Vai receber várias notas
        param: sit: Caso True vai mostrar a situação da média da turma
        A função vai adicionar em um dicionário o total de notas cadastradas,
        a maior e a menor nota e caso a sit=True, irá adcionar também a 
        situação da turma. 

    """
    dic = dict()
    dic['total'] = len(nts)
    dic['maior'] = max(nts)
    dic['menor'] = min(nts)
    dic['media'] = sum(nts) / len(nts)
    if sit == True:
        if dic['media'] < 6.5:
            dic['situacao'] = 'RUIM'
        if dic['media'] >= 6.5 and dic['media'] <= 7.5:
            dic['situacao'] = 'RAZOÁVEL'
        if dic['media'] > 7.5:
            dic['situacao'] = 'BOA'
    print(dic)



notas(6.0, 10.0, 7.0, 9.0)
